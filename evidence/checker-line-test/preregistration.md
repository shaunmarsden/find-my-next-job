# Pre-registration: can the skill stop talking about the checker?

Written on 28th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

In the [paste test](../paste-test/results.md), eleven of the twelve skill replies told the jobseeker something like "I didn't run the automated check, so I applied the same checks by hand." The automated check is the Python helper in `scripts/`, which cannot run in a chat. To a jobseeker, the sentence means nothing.

It comes from one line in `SKILL.md`: "Without Python, apply the same gate manually and disclose that automated preflight was not run." Does changing that line stop the sentence, without making the sorting or the shape worse, and without stopping the skill from saying how it checked when someone asks?

## The two versions

- **Current.** `SKILL.md` as it is now (`variants/skill-current.md`).
- **Fixed.** The same, with that one sentence replaced by: "Without Python, apply the same gate manually. Do not mention the helper, Python or preflight in the default shortlist; report preflight status only when the person asks for the detailed records or an audit." (`variants/skill-fixed.md`). Nothing else changes.

Each prompt is the skill, then a line, then the jobseeker's message. Nothing says this is a test.

## The three messages

- **Warehouse** and **School office**: the same two messages as the paste test, unchanged (`scenarios/`).
- **Warehouse, detail asked for**: the Warehouse message with one sentence added after "Which should I go for?": "Please also show me the detailed checks, and tell me exactly how you checked them."

3 messages x 2 versions x 3 runs = 18 replies, each from a fresh subagent on the same model as me (Opus 5.5), with Claude Code's own context. Each reads one prompt file and writes one reply to a file with a random name, and is told not to read any other file or run any other command. I score blind, then unblind.

## Scoring (fixed now)

### Main measure: mentions of the checker (Warehouse and School office, 12 replies)

1 if the reply mentions the checker in any form: "automated check", "automated preflight", "preflight", "Python", "the helper", "the script" or "the tool that comes with this skill". 0 if not.

### Second measure: saying how it checked, when asked (Warehouse, detail asked for, 6 replies)

1 if the reply says in some form that the checks were done by reading and judging, not by an automated tool or script. Plain words ("I read each advert and checked it by hand") count. 0 if it gives detailed checks but says nothing about how they were done.

### Guards (Warehouse and School office, 12 replies)

Sorting and shape, scored exactly as in the paste test (see its [pre-registration](../paste-test/preregistration.md)), including the line drawn there for jobs ruled out with an offer to relax a limit. Automatic failures counted as there.

## What I expect

1. Current mentions the checker in at least 4 of its 6 default replies; Fixed in at most 1.
2. Fixed sorts and shapes about as well as Current.
3. On the detail request, both versions say how they checked in most replies.

## What I will ship

I will change `SKILL.md` to the Fixed version only if all of these hold:

- Fixed mentions the checker in fewer default replies than Current.
- Fixed sorts no more than one advert worse in total than Current, out of 33.
- Fixed's mean shape is no more than 0.5 below Current's.
- Fixed says how it checked in no more than one fewer detail reply than Current.

If any fails, I will report it and leave `SKILL.md` as it is.

## What I will not do

- Add runs to change the result.
- Change a variant, a message or the scoring after seeing a reply and count the result as part of this test.

## Limits I already know about

- 18 replies on made-up jobseekers I wrote, scored by me. I know the expected answers while scoring.
- One message per conversation. In real use, someone would ask for the detail in a second message, after seeing the shortlist.
- The detail request names "how you checked them", which makes the second measure easy to pass. It tests that the fix does not suppress the answer when asked, not that the skill volunteers it.
- Subagents with Claude Code's own context, which may differ from a plain chat window.
