# Release notes

## 2.1.0 (28 October 2026)

- **One name.** The skill is now Find My Next Job (`find-my-next-job`), the same as the repository. It was Job Match Finder (`job-match-finder`).
- **Works when pasted into a chat.** The shortlist template is now inside `SKILL.md`, so a pasted copy follows it without opening another file. `references/shortlist-template.md` is removed, as it would have been a second copy. Tested in [evidence/paste-test](evidence/paste-test/results.md).
- **Free, and nothing more.** I removed the wording about selling the skill. It is MIT-licensed.
- **Made-up example.** The example in `examples/first-interaction.md` named real employers and linked to real job pages. It is now a reply from the paste test, with made-up employers.
- **Plain README.** Rewritten for the person looking for a job, with the paste route first.
- **Removed `BUYER-EXPERIENCE-NOTES.md`.** It described test records that were never published in this repository, so nobody could check them.

The checker in `scripts/preflight.py`, its 36 tests, `references/search-and-verification.md`, `references/record-contract.md` and `examples/fictional-shortlist.json` are unchanged.

## 2.0.1-rc.2 and earlier

Development versions. Their test records were not published here, so I make no claims from them.
