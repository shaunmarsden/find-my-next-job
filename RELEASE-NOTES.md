# Buyer experience candidate 2.0.1-rc.2

Derived from the preserved 2.0.1-rc.1 release candidate. CV/plain-language intake and agent-owned technical preparation are explicit. Default results are a compact shortlist with suitable, conditional and unverified sections; detailed checks are available on request. Questions are limited to missing search-critical facts. Browsing and attachment failures are explained plainly.

Python helper, its 36 unit tests, JSON example and record contract are unchanged. Source verification, requirements, salary, geography and duplicate gates remain in force. No fictional candidate or vacancy has been added to the reusable instructions. The prior release notes remain preserved inside the original release-candidate archive.

Run host-side checks from the extracted root when maintaining the package:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/preflight.py --input examples/fictional-shortlist.json
```

These are maintainer/agent commands, not customer steps. Current run results and the fresh fictional interaction are recorded in the accompanying BUYER-EXPERIENCE-NOTES.md and validation evidence. They do not establish Agensi compatibility, human sign-off or willingness to pay. Nothing has been published.