#!/usr/bin/env python3
"""Offline shortlist preflight of host-attested facts. Does not browse or judge prose."""
import argparse
import datetime as dt
import json
import math
import pathlib
import re
import sys
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

OFFICIAL = {'employer', 'ats'}
STATUSES = {'present', 'closed', 'inaccessible', 'not_checked'}
MATCHES = {'supported', 'partial', 'gap', 'unknown'}


def text(value):
    return isinstance(value, str) and bool(value.strip())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def timestamp(value):
    require(text(value), 'timestamp must be an ISO string with timezone')
    try:
        result = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        raise ValueError('invalid ISO timestamp') from None
    require(result.tzinfo is not None and result.utcoffset() is not None, 'timestamp needs timezone')
    return result


def job_key(url):
    """Only explicit ATS identities or conservative URL equality; no title-only merging."""
    require(text(url), 'canonical_url required')
    u = urlsplit(url)
    require(u.scheme == 'https' and u.hostname and not u.username and not u.password,
            'vacancy URLs must be HTTPS without credentials')
    host = u.hostname.lower()
    path = u.path.rstrip('/')
    if host in {'boards.greenhouse.io', 'job-boards.greenhouse.io', 'job-boards.eu.greenhouse.io'}:
        m = re.fullmatch(r'/([^/]+)/jobs/(\d+)', path)
        if m:
            region = 'eu' if '.eu.' in host else 'global'
            return 'greenhouse:' + region + ':' + ':'.join(m.groups())
    if host in {'jobs.lever.co', 'jobs.eu.lever.co'}:
        m = re.fullmatch(r'/([^/]+)/([A-Za-z0-9-]+)(?:/apply)?', path)
        if m:
            region = 'eu' if '.eu.' in host else 'global'
            return 'lever:' + region + ':' + ':'.join(m.groups())
    if host == 'jobs.ashbyhq.com':
        m = re.fullmatch(r'/([^/]+)/([A-Za-z0-9-]+)(?:/application)?', path)
        if m:
            return 'ashby:' + ':'.join(m.groups())
    query = [(k, v) for k, v in parse_qsl(u.query, keep_blank_values=True)
             if not k.lower().startswith('utm_') and k.lower() not in {'gclid', 'fbclid', 'gh_src'}]
    return 'url:' + urlunsplit(('https', u.netloc.lower(), path or '/', urlencode(query), ''))


def load(path):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'duplicate JSON key: ' + key)
            result[key] = value
        return result
    def bad_constant(value):
        raise ValueError('non-JSON numeric constant: ' + value)
    def finite_float(value):
        number = float(value)
        require(math.isfinite(number), 'non-finite JSON number')
        return number
    return json.loads(pathlib.Path(path).read_text(encoding='utf-8'),
                      object_pairs_hook=object_pairs, parse_constant=bad_constant, parse_float=finite_float)


def validate(data):
    require(isinstance(data, dict), 'input must be an object')
    require(data.get('mode') in {'live', 'fictional'}, 'mode must be live or fictional')
    require(text(data.get('profile_id')), 'profile_id required; use a nonidentifying label')
    as_of = timestamp(data.get('as_of'))
    hard = data.get('hard_constraints')
    require(isinstance(hard, list) and all(text(k) for k in hard) and len(set(hard)) == len(hard),
            'hard_constraints must list unique nonblank names')
    require(isinstance(data.get('records'), list), 'records must be a list (empty is allowed)')
    ids = set()
    for row in data['records']:
        require(isinstance(row, dict), 'each record must be an object')
        for key in ('id', 'employer', 'title'):
            require(text(row.get(key)), key + ' must be nonblank')
        require(row['id'] not in ids, 'capture record IDs must be unique')
        ids.add(row['id'])
        job_key(row.get('canonical_url'))
        host = urlsplit(row['canonical_url']).hostname.lower()
        if data['mode'] == 'live':
            require(host not in {'example.com', 'example.org', 'example.net', 'localhost'}
                    and not host.endswith(('.invalid', '.test', '.example', '.localhost')),
                    'reserved/example URLs cannot represent live vacancies')
        source = row.get('source')
        require(isinstance(source, dict), 'source must be an object')
        require(source.get('kind') in OFFICIAL | {'aggregator', 'fictional'}, 'invalid source kind')
        require(not (data['mode'] == 'live' and source['kind'] == 'fictional'), 'fictional source in live input')
        require(source.get('status') in STATUSES, 'invalid source status')
        job_key(source.get('url'))
        if data['mode'] == 'live':
            source_host = urlsplit(source['url']).hostname.lower()
            require(source_host not in {'example.com', 'example.org', 'example.net', 'localhost'}
                    and not source_host.endswith(('.invalid', '.test', '.example', '.localhost')),
                    'reserved/example source URLs cannot represent live observations')
        checked = timestamp(source.get('checked_at'))
        require(checked <= as_of, 'checked_at cannot be later than as_of')
        require(text(source.get('evidence')), 'source evidence/availability note required')
        checks = row.get('constraint_checks')
        require(isinstance(checks, dict) and set(checks) == set(hard), 'every hard constraint needs exactly one check')
        for name, check in checks.items():
            require(isinstance(check, dict) and check.get('status') in {'met', 'unmet', 'unknown'}
                    and text(check.get('reason')), name + ': explicit status and reason required')
        requirements = row.get('requirements')
        require(isinstance(requirements, list), 'requirements must be a list')
        require(bool(requirements) or source['status'] != 'present' or source['kind'] not in OFFICIAL,
                'present official listing needs requirement checks')
        for requirement in requirements:
            require(isinstance(requirement, dict) and text(requirement.get('criterion'))
                    and requirement.get('importance') in {'essential', 'preferred'}
                    and requirement.get('match') in MATCHES
                    and text(requirement.get('candidate_evidence')) and text(requirement.get('job_evidence')),
                    'requirement needs criterion, importance, match and both evidence notes')
        require(isinstance(row.get('conflicts'), list) and all(text(x) for x in row['conflicts']),
                'conflicts must be a list of nonblank notes')
    return as_of


def gate(row, as_of):
    source = row['source']
    if source['kind'] not in OFFICIAL:
        return 'unverified', ['no official listing attested; a repost badge is not verification']
    if source['status'] == 'closed':
        return 'exclude', ['official/source page reports closure']
    if source['status'] != 'present':
        return 'unverified', ['no present official listing attested']
    if row['conflicts']:
        return 'hold', list(row['conflicts'])
    if as_of - timestamp(source['checked_at']) > dt.timedelta(hours=24):
        return 'hold', ['official observation older than 24 hours; recheck']
    unmet = [name for name, c in row['constraint_checks'].items() if c['status'] == 'unmet']
    gaps = [r['criterion'] for r in row['requirements'] if r['importance'] == 'essential' and r['match'] == 'gap']
    if unmet or gaps:
        return 'exclude', ['hard constraint unmet: ' + k for k in unmet] + ['essential gap: ' + k for k in gaps]
    unknown = [name for name, c in row['constraint_checks'].items() if c['status'] == 'unknown']
    partial = [r['criterion'] for r in row['requirements'] if r['importance'] == 'essential' and r['match'] in {'partial', 'unknown'}]
    if unknown or partial:
        return 'hold', ['hard constraint unknown: ' + k for k in unknown] + ['essential evidence unresolved: ' + k for k in partial]
    preferred = [r['criterion'] for r in row['requirements'] if r['importance'] == 'preferred' and r['match'] != 'supported']
    if preferred:
        return 'review', ['preferred criterion unresolved: ' + k for k in preferred]
    return 'recommend', ['declared checks clear; human review still required']


def annotation_signature(row):
    return (tuple(sorted((k, c['status']) for k, c in row['constraint_checks'].items())),
            tuple(sorted((r['criterion'], r['importance'], r['match']) for r in row['requirements'])))


def assess(data):
    as_of = validate(data)
    groups = {}
    for row in data['records']:
        groups.setdefault(job_key(row['canonical_url']), []).append(row)
    results = []
    for key, rows in groups.items():
        # Prefer an official observation, but never hide contradictory duplicates.
        chosen = max(rows, key=lambda r: (r['source']['kind'] in OFFICIAL, timestamp(r['source']['checked_at'])))
        decision, reasons = gate(chosen, as_of)
        official_states = {r['source']['status'] for r in rows if r['source']['kind'] in OFFICIAL}
        identity = {(r['employer'].casefold().strip(), r['title'].casefold().strip()) for r in rows}
        conflict = len(official_states) > 1 or len(identity) > 1 or len({annotation_signature(r) for r in rows}) > 1
        if conflict:
            decision, reasons = 'hold', ['duplicate records disagree; preserve evidence and recheck, do not choose a favourable result']
        results.append({'key': key, 'employer': chosen['employer'], 'title': chosen['title'],
                        'canonical_url': chosen['canonical_url'], 'decision': decision, 'reasons': reasons,
                        'capture_ids': [r['id'] for r in rows], 'source_observations': [r['source'] for r in rows]})
    names = {}
    for row in results:
        names.setdefault((row['employer'].casefold().strip(), row['title'].casefold().strip()), []).append(row['key'])
    return {'scope': 'offline preflight of host-attested data; does not verify pages or candidate truth',
            'mode': data['mode'], 'as_of': data['as_of'], 'profile_id': data['profile_id'],
            'human_review_required': True, 'verification_performed_by_script': False,
            'record_count': len(data['records']), 'unique_jobs': len(results), 'results': results,
            'possible_duplicates_not_merged': [keys for keys in names.values() if len(keys) > 1]}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', help='Optional new JSON file; existing files are never overwritten')
    args = ap.parse_args()
    try:
        result = assess(load(args.input))
        encoded = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
        if args.out:
            with open(args.out, 'x', encoding='utf-8') as f:
                f.write(encoded)
        print(encoded, end='')
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print('Input error: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
