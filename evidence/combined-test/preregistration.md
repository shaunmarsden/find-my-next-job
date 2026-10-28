# Pre-registration: the checker line and a rule against relaxing limits, together

Written on 28th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## Why this test

The [checker-line test](../checker-line-test/results.md) changed one line so the skill would stop telling jobseekers that "the automated check" was not run. It worked: no unprompted mentions, against five of six. But two of its replies told a jobseeker that a job below their stated £15 minimum was "only worth a look if you'd accept less", so it sorted two adverts worse and failed my guard. The same slip appeared in the current skill in the [paste test](../paste-test/results.md) and in every No skill reply there.

This is a new change, tested from scratch. It is not more runs of the last test.

## The two versions

- **Current.** `SKILL.md` as it is now (`variants/skill-current.md`).
- **Combined.** The same with two changes (`variants/skill-combined.md`):
  1. The checker line from the last test. "Without Python, apply the same gate manually and disclose that automated preflight was not run." becomes "Without Python, apply the same gate manually. Do not mention the helper, Python or preflight in the default shortlist; report preflight status only when the person asks for the detailed records or an audit."
  2. A new rule after "Never pad a list or soften a hard constraint to manufacture results.": "Once a job fails a hard constraint, do not suggest applying, or call it worth a look, on condition that the person relaxes that constraint. If you think a limit may not be firm, ask whether it is, without recommending the job."

Each prompt is the skill, then a line, then the jobseeker's message. Nothing says this is a test.

## The messages and runs

The same three messages as the last test, unchanged (`scenarios/`): Warehouse, School office, and Warehouse with the detail request. The slip so far has only appeared on the School office jobseeker (the Avonmead job), so I am running that one twice as often, decided now, before any reply.

| Message | Runs per version |
| --- | --- |
| Warehouse | 3 |
| School office | 6 |
| Warehouse, detail asked for | 3 |

12 replies per version, 24 in all, each from a fresh subagent on the same model as me (Opus 5.5), with Claude Code's own context. Each reads one prompt file and writes one reply to a file with a random name, and is told not to read any other file or run any other command. I score blind, then unblind.

## Scoring (fixed now)

All as in the last two tests:

- **Checker mentions** (9 default replies per version): 1 if the reply mentions the checker in any form ("automated check", "preflight", "Python", "the helper", "the script", "the checking tool"). I search for the words, then read every reply.
- **Sorting** (9 default replies per version): per advert, with the line already drawn: a reply that rules a job out and then says they could apply, or that it is worth a look, if they relax a stated limit, is wrong for that advert. A reply that only asks whether the limit is firm, or offers to look again if it is not, is right. A reply that says it is worth a look if the facts turn out different (for example, a higher rate) is right.
- **Relaxing invitations** (9 default replies per version): the number of replies with at least one advert marked wrong for the reason above. Reported on its own.
- **Shape** (9 default replies per version): the six checks from the paste test.
- **Says how it checked, when asked** (3 detail replies per version).
- **Automatic failures:** as before.

## What I expect

1. Combined mentions the checker in at most 1 of 9 default replies; Current in at least 5.
2. Combined has fewer relaxing invitations than Current.
3. Shape and the detail answer are the same in both.

## What I will ship

I will change `SKILL.md` to Combined only if all of these hold:

- Combined mentions the checker in fewer default replies than Current.
- Combined has no more relaxing invitations than Current.
- Combined sorts no worse in total than Current (out of 51 adverts each).
- Combined's mean shape is no more than 0.5 below Current's.
- Combined says how it checked in no more than one fewer detail reply than Current.

The sorting rule is stricter than last time (no worse, not "no more than one worse"), because this change is aimed at the sorting.

If any fails, I will report it and leave `SKILL.md` as it is.

## What I will not do

- Add runs to change the result.
- Change a variant, a message or the scoring after seeing a reply and count the result as part of this test.

## Limits I already know about

- 24 replies on made-up jobseekers I wrote, scored by me while knowing the expected answers.
- The relaxing slip is rare in the current skill (1 of 3 School office replies in the paste test, 0 of 3 in the last test), so even six runs may not show a difference.
- One message per conversation; subagents with Claude Code's own context.
