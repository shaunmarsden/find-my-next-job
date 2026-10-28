# How Do I Find My Next Job?

A downloadable AI agent skill that helps jobseekers explore public job vacancies, match opportunities against their stated experience, and understand which roles deserve a closer look.

This repository contains the source of the **Job Match Finder** skill, whose internal identifier remains `job-match-finder`.

## Quick start

1. Download the repository ZIP (the green **Code** button, then **Download ZIP**).
2. Install the files in an AI agent that supports `SKILL.md` skills and referenced resources. Keep the directory structure intact.
3. Ask: **"Help me find my next job. Here is my work history. I live in Manchester and want full-time work."**
4. Provide location and other non-negotiable constraints if not already supplied. The agent should return promising leads, conditional matches and unverified vacancies separately.

You don't need to create JSON or run Python. A compatible agent handles the workflow.

## What it does

- Searches publicly accessible opportunities when the host has browsing capabilities.
- Looks beyond exact job titles to consider adjacent duties and transferable experience.
- Reviews essential requirements, geography, working pattern and advertised salary basis.
- Distinguishes confirmed evidence, uncertainty and hard mismatches.
- Produces a concise shortlist with direct links, reasons and remaining checks.
- Does **not** apply for jobs, contact employers or guarantee a job or interview.

## Compatibility and limitations

This is an **agent skill**, not a plug-in that works inside every LLM chat. It requires a host that supports loading `SKILL.md` plus its relative reference files. Live discovery requires web search and the ability to open employer/ATS pages. A browser may be unable to access some sites. Attachment/CV reading depends on host support. Without browsing, it can assess vacancies provided by the user, but cannot claim to have verified them live.

The optional `scripts/preflight.py` uses Python 3.9+ standard library and validates AI-annotated records, **not** whether employer pages or candidate evidence are true. The agent can use manual screening when code execution is unavailable.

**Status:** Buyer-experience release candidate `2.0.1-rc.2`. Mechanical tests and fictional scenarios passed during development, but Agensi installation, nontechnical buyer testing and commercial demand were not demonstrated as of 28 October 2026. This project makes no claim of increased job-finding success or time savings.

## Developer checks

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/preflight.py --input examples/fictional-shortlist.json
```

For design details see `SKILL.md`, `references/`, and `BUYER-EXPERIENCE-NOTES.md`. Fictional demonstrations are explicitly labelled.

## Licensing and distribution

Open-source under the MIT License, see [LICENSE](LICENSE). The same source may be distributed through Agensi as a convenience package. Buying an Agensi copy does not grant exclusive rights over this open-source code.

## Privacy and safety

Use a sanitised work history where possible. Do not provide identity documents or private employer information. The agent should not submit applications, contact employers or persist personal information without explicit approval. Job information can be incomplete or outdated, and users must verify details before applying.