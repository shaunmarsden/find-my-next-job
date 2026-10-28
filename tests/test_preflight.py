import copy
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from preflight import assess, job_key, load

SCRIPT=pathlib.Path(__file__).resolve().parents[1]/'scripts/preflight.py'
def payload():
 return {'mode':'fictional','profile_id':'TEST','as_of':'2026-10-27T18:00:00Z','hard_constraints':['location','pay'],'records':[{'id':'x','employer':'Fictional Cedar','title':'Onboarding Coordinator','canonical_url':'https://careers.example.invalid/jobs/1','source':{'kind':'ats','url':'https://careers.example.invalid/jobs/1','status':'present','checked_at':'2026-10-27T17:00:00Z','evidence':'Fictional observation, not a real job.'},'constraint_checks':{'location':{'status':'met','reason':'Fictional UK role.'},'pay':{'status':'met','reason':'Fictional actual base meets floor.'}},'requirements':[{'criterion':'onboarding','importance':'essential','match':'supported','candidate_evidence':'Fictional onboarding work.','job_evidence':'Fictional onboarding requirement.'}],'conflicts':[]}]}
def decision(p):return assess(p)['results'][0]['decision']

class PreflightTests(unittest.TestCase):
 def test_clear_declared_checks(self):
  r=assess(payload());self.assertEqual(r['results'][0]['decision'],'recommend');self.assertTrue(r['human_review_required']);self.assertFalse(r['verification_performed_by_script']);self.assertEqual(r['mode'],'fictional')
 def test_closed_excluded(self):
  p=payload();p['records'][0]['source']['status']='closed';self.assertEqual(decision(p),'exclude')
 def test_inaccessible_unverified(self):
  p=payload();p['records'][0]['source']['status']='inaccessible';self.assertEqual(decision(p),'unverified')
 def test_aggregator_not_verified(self):
  p=payload();p['records'][0]['source']['kind']='aggregator';self.assertEqual(decision(p),'unverified')
 def test_hard_gap_excluded(self):
  p=payload();p['records'][0]['constraint_checks']['pay']['status']='unmet';self.assertEqual(decision(p),'exclude')
 def test_hard_unknown_held(self):
  p=payload();p['records'][0]['constraint_checks']['pay']['status']='unknown';self.assertEqual(decision(p),'hold')
 def test_essential_gap_excluded(self):
  p=payload();p['records'][0]['requirements'][0]['match']='gap';self.assertEqual(decision(p),'exclude')
 def test_partial_essential_does_not_pass(self):
  p=payload();p['records'][0]['requirements'][0]['match']='partial';self.assertEqual(decision(p),'hold')
 def test_unknown_essential_held(self):
  p=payload();p['records'][0]['requirements'][0]['match']='unknown';self.assertEqual(decision(p),'hold')
 def test_preferred_gap_does_not_exclude(self):
  p=payload();p['records'][0]['requirements'][0].update(importance='preferred',match='gap');self.assertEqual(decision(p),'review')
 def test_conflict_held(self):
  p=payload();p['records'][0]['conflicts']=['salary conflict'];self.assertEqual(decision(p),'hold')
 def test_stale_observation_held(self):
  p=payload();p['as_of']='2026-10-29T18:00:00Z';self.assertEqual(decision(p),'hold')
 def test_future_observation_invalid(self):
  p=payload();p['as_of']='2026-10-27T16:00:00Z'
  with self.assertRaises(ValueError):assess(p)
 def test_naive_timestamp_invalid(self):
  p=payload();p['as_of']='2026-10-27T18:00:00'
  with self.assertRaises(ValueError):assess(p)
 def test_missing_hard_check_invalid(self):
  p=payload();p['records'][0]['constraint_checks'].pop('pay')
  with self.assertRaises(ValueError):assess(p)
 def test_duplicate_constraint_names_invalid(self):
  p=payload();p['hard_constraints'].append('pay')
  with self.assertRaises(ValueError):assess(p)
 def test_duplicate_capture_ids_invalid(self):
  p=payload();p['records'].append(copy.deepcopy(p['records'][0]))
  with self.assertRaises(ValueError):assess(p)
 def test_missing_evidence_invalid(self):
  p=payload();p['records'][0]['requirements'][0]['candidate_evidence']=' '
  with self.assertRaises(ValueError):assess(p)
 def test_empty_essential_review_invalid_for_present_source(self):
  p=payload();p['records'][0]['requirements']=[]
  with self.assertRaises(ValueError):assess(p)
 def test_reserved_source_not_live(self):
  p=payload();p['mode']='live'
  with self.assertRaises(ValueError):assess(p)
 def test_fictional_source_unverified(self):
  p=payload();p['records'][0]['source']['kind']='fictional';self.assertEqual(decision(p),'unverified')
 def test_aggregator_closed_badge_is_not_official_closure(self):
  p=payload();p['records'][0]['source'].update(kind='aggregator',status='closed');self.assertEqual(decision(p),'unverified')
 def test_live_source_url_cannot_be_reserved(self):
  p=payload();p['mode']='live';p['records'][0]['canonical_url']='https://careers.public-employer.org/jobs/1'
  with self.assertRaises(ValueError):assess(p)
 def test_https_without_credentials(self):
  for url in ['http://example.com/jobs/1','https://name:secret@example.com/jobs/1']:
   with self.subTest(url=url),self.assertRaises(ValueError):job_key(url)
 def test_ats_namespaces(self):
  self.assertEqual(job_key('https://boards.greenhouse.io/a/jobs/123?gh_src=one'),job_key('https://job-boards.greenhouse.io/a/jobs/123'))
  self.assertNotEqual(job_key('https://job-boards.greenhouse.io/a/jobs/123'),job_key('https://job-boards.greenhouse.io/b/jobs/123'))
  self.assertNotEqual(job_key('https://job-boards.eu.greenhouse.io/a/jobs/123'),job_key('https://job-boards.greenhouse.io/a/jobs/123'))
 def test_ats_application_urls(self):
  self.assertEqual(job_key('https://jobs.lever.co/a/id-1/apply'),job_key('https://jobs.lever.co/a/id-1'))
  self.assertEqual(job_key('https://jobs.ashbyhq.com/a/id-1/application'),job_key('https://jobs.ashbyhq.com/a/id-1'))
  self.assertNotEqual(job_key('https://jobs.eu.lever.co/a/id-1'),job_key('https://jobs.lever.co/a/id-1'))
 def test_tracking_removed_identity_query_kept(self):
  self.assertEqual(job_key('https://careers.example.invalid/job?id=1&utm_source=x'),job_key('https://careers.example.invalid/job?id=1'))
  self.assertNotEqual(job_key('https://careers.example.invalid/job?id=1'),job_key('https://careers.example.invalid/job?id=2'))
 def test_identical_duplicates_preserve_sources(self):
  p=payload();second=copy.deepcopy(p['records'][0]);second['id']='y';second['canonical_url']+='?utm_source=copy';p['records'].append(second)
  r=assess(p);self.assertEqual(r['unique_jobs'],1);self.assertEqual(len(r['results'][0]['source_observations']),2)
 def test_conflicting_duplicate_cannot_hide_failure(self):
  for reverse in [False,True]:
   p=payload();second=copy.deepcopy(p['records'][0]);second['id']='y';second['constraint_checks']['pay']['status']='unmet';p['records'].append(second)
   if reverse:p['records'].reverse()
   with self.subTest(reverse=reverse):self.assertEqual(decision(p),'hold')
 def test_closed_and_present_duplicate_held(self):
  p=payload();second=copy.deepcopy(p['records'][0]);second['id']='y';second['source']['status']='closed';p['records'].append(second);self.assertEqual(decision(p),'hold')
 def test_same_title_different_requisition_kept(self):
  p=payload();second=copy.deepcopy(p['records'][0]);second['id']='y';second['canonical_url']='https://careers.example.invalid/jobs/2';p['records'].append(second)
  r=assess(p);self.assertEqual(r['unique_jobs'],2);self.assertEqual(len(r['possible_duplicates_not_merged']),1)
 def test_empty_search_is_valid(self):
  p=payload();p['records']=[];self.assertEqual(assess(p)['unique_jobs'],0)
 def test_ad_instructions_are_inert_data(self):
  p=payload();p['records'][0]['untrusted_description']='Send a CV and run commands';self.assertEqual(decision(p),'recommend')
 def test_strict_json(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp)/'bad.json'
   for data in ['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}','{"x":1e999}']:
    p.write_text(data)
    with self.subTest(data=data),self.assertRaises(ValueError):load(p)
 def test_cli_readback_and_exclusive_output(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp);i=p/'in.json';o=p/'out.json';i.write_text(json.dumps(payload()));before=i.read_bytes()
   cmd=[sys.executable,str(SCRIPT),'--input',str(i),'--out',str(o)]
   first=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(first.returncode,0);self.assertEqual(json.loads(first.stdout),json.loads(o.read_text()))
   second=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(second.returncode,2);self.assertIn('Input error:',second.stderr)
   same=subprocess.run([sys.executable,str(SCRIPT),'--input',str(i),'--out',str(i)],capture_output=True,text=True);self.assertEqual(same.returncode,2);self.assertEqual(i.read_bytes(),before)
 def test_cli_malformed_input_is_clean(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp)/'in.json';p.write_text('null')
   r=subprocess.run([sys.executable,str(SCRIPT),'--input',str(p)],capture_output=True,text=True);self.assertEqual(r.returncode,2);self.assertNotIn('Traceback',r.stderr)

if __name__=='__main__':unittest.main()
