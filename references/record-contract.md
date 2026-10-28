# Offline preflight record contract

Use only when the host can execute Python. This is a gate on the agent's declared facts, not a job search/matching engine. Incorrect extraction or an omitted essential criterion can still pass. A human must inspect source and candidate evidence.

Top-level JSON fields:

| Field | Meaning |
| --- | --- |
| `mode` | `live` or `fictional`; always preserve in reports |
| `profile_id` | Sanitised local reference such as A, not a full personal identity |
| `as_of` | ISO date/time with timezone for this evaluation; use the actual check session, not a stale invented date |
| `hard_constraints` | Unique names of all declared dealbreakers; an empty list is allowed only if there are none |
| `records` | List of vacancy observations; an empty list is valid |

Each record needs `id` (unique capture ID), `employer`, `title`, `canonical_url`, `source`, `constraint_checks`, `requirements`, `conflicts`.

- `source`: `kind` (`employer`, `ats`, `aggregator`, `fictional`); `url`; `status` (`present`, `closed`, `inaccessible`, `not_checked`); `checked_at` with timezone; nonblank `evidence` (short observation or access note). Official origin/presence are host attestations, not verified by Python.
- `constraint_checks`: exactly one entry per named hard constraint, each with `status` (`met`, `unmet`, `unknown`) and a concrete `reason`. Convert salary/hours facts into these checks honestly; the helper does not compute or verify them.
- `requirements`: one entry for every essential criterion and relevant preference, with `criterion`, `importance` (`essential`, `preferred`), `match` (`supported`, `partial`, `gap`, `unknown`), `candidate_evidence`, `job_evidence`. State absent evidence explicitly instead of filling an empty string. Present official records require at least one check; the helper cannot prove the list is exhaustive.
- `conflicts`: list of unresolved source conflicts; use `[]` if none.

The helper outputs `recommend`, `review` (preferred gaps), `hold` (hard/essential uncertainty, conflicts or observations older than 24 hours), `exclude`, or `unverified`. These are screening buckets, not legal eligibility or employer selection decisions. Fictional-mode output must never be presented as live.

Exact ATS identity is namespaced by provider/region/board/ID for supported Greenhouse, Lever and Ashby URLs. An aggregator needs an explicitly resolved original `canonical_url`; titles alone do not establish identity. Employer URLs retain meaningful query parameters and discard only known tracking parameters. Different requisitions stay separate and may be flagged as possible duplicates. Source observations and capture IDs survive merging. Contradictory annotations or official states hold the group in either input order.

The 24-hour threshold is a conservative recheck reminder, not a guarantee of freshness within 24 hours. It is evaluated relative to `as_of`; historical replay remains historical. Recheck on a new session even if a saved JSON report once passed.

## Commands and permissions

```sh
python3 scripts/preflight.py --input examples/fictional-shortlist.json
python3 scripts/preflight.py --input records.json --out new-preflight.json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Exit 0 means preflight completed, including when every job is held/excluded. Exit 2 means invalid data or I/O error: correct it before presenting a shortlist. JSON keys must be unique; nonfinite numbers are rejected. HTTPS URLs cannot contain credentials. Reserved example URLs cannot be used in live mode. `--out` creates a new file exclusively and never overwrites an input/existing file.

Standard-library Python 3.9+. No network calls, API keys, shell commands or automatic tracking in the helper. It reads the selected JSON and writes stdout, plus an optional user-chosen new file. Use temporary sanitised records by default; save personal data/history only on explicit request in the chosen location. No need for a database, cloud account or local service.