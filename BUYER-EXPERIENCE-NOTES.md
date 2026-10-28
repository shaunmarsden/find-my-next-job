# Buyer experience notes: 2.0.1-rc.2

This is a narrow onboarding/presentation adjustment to the existing release candidate. It is not a new search engine or an approved paid release. The proposed £7 price has not been validated by this work.

## Changes

- SKILL.md explicitly accepts a readable CV, work-history summary or ordinary description, reuses provided information and asks only for essential missing search facts. Unsupported attachment formats get an honest request for relevant pasted text.
- Technical preparation belongs to the agent. The customer is never required to create JSON, run Python or manage helper files. Existing manual screening remains available when optional Python execution is absent.
- The default template now uses short role descriptions, links, fit reasons and key questions. Suitable leads, conditional opportunities and unverified listings stay distinct. Full evaluation tables and supporting records are available on request in the working context; personal records are not saved by default.
- README gives a conversational first step and plain host requirements. A short observed interaction example is included. Version metadata and release notes identify this candidate.

Already-supported safeguards were retained rather than reimplemented: source inspection, essential/preferred and alternative/additional requirements, hard constraints, actual versus FTE/OTE pay, source status, duplicate identity, human application decisions and no unrequested external action. Python helper, unit tests, JSON example, record contract and search/verification reference are byte-identical to the prior release candidate.

## Tested

- All 36 existing unit tests passed, with no test changes.
- All 20 frozen scenarios passed against the unchanged helper. Frozen profiles, answer key and prior results were not edited.
- Skill-format validation and package-relative resource checks passed. ZIP integrity, root SKILL.md, complete resource inclusion and fresh-extraction execution were checked in the accompanying validation evidence.
- One fresh-context Codex agent received a fictional natural-language work-history request. It inferred role families, made four live search queries and attempted six original vacancy sources. Three employer descriptions were readable; the other three returned 403, 404 or a JavaScript-only shell.
- Its customer response contained three conditional opportunities and no fully cleared suitable lead. It explained the empty cleared shortlist and access limitations without asking the customer to handle files or commands. The optional helper ran under agent control, exit 0, with three holds and three unverified identities. Exit 0 is processing success, not source or fit verification.
- Detailed source/requirement records were kept separate from the customer response. Two distinct roles from one employer were not merged. No applications, accounts, employer contact, paid services or publication occurred.

The fresh test is one execution, not a success-rate estimate, human review or comparative commercial validation. Exact runtime model/settings were unavailable. The reviewer had a fresh context with a limited read allowlist, but shared filesystem access was not hard-isolated. An evidence-building TypeError was corrected by the agent; it did not affect the helper or require customer action. Its recorded timing began after the first input read, so no complete latency or time-saving claim is made.

## Intended or still untested

CV ingestion depends on the host's attachment-reading capability; this run used typed work history, not a CV upload. A missing-information intake branch, fully unavailable browsing, Python-unavailable operation and a customer's request for the detailed record were specified but not separately exercised in this single test. The complete suitable-lead path was not demonstrated because essential questions remained; no screening rule was relaxed to fill it.

The host must load SKILL.md and supporting files. Live discovery needs web search and readable employer/ATS pages, including JavaScript support where required. Optional automated preflight needs file access and Python 3.9+ with only the standard library; the agent manages those steps. Without these capabilities, the agent must explain the relevant limitation plainly and must not claim verified live discovery.

Actual Agensi installation/execution and observed nontechnical buyer use remain untested. Human sign-off remains pending. The prior commercial comparison is preserved; this presentation adjustment does not overturn its finding that a sufficient paid advantage was not demonstrated. No price, buyer satisfaction or time saving has been established.

## Files

The buyer ZIP has SKILL.md at its root, README, release notes, these notes, three reference files, two examples, unchanged helper and unchanged unit suite. A separate validation folder preserves the complete fresh response, request, evidence, test records and exact execution output. All pre-existing output files were hash-checked unchanged.