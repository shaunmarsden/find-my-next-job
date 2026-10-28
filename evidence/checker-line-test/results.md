# Results: can the skill stop talking about the checker?

Run on 28th October 2026. The [pre-registration](preregistration.md) was committed at 16:46 GMT, before any reply existed, and the [scores](scores-blind.md) at 16:49 GMT, before I looked at which version wrote which reply.

## The result

| Version | Mentions the checker (6 default replies) | Adverts sorted right | Mean shape (out of 6) | Says how it checked, when asked |
| --- | --- | --- | --- | --- |
| Current | 5 of 6 | 33 of 33 | 6.00 | 3 of 3 |
| Fixed | **0 of 6** | **31 of 33** | 6.00 | 3 of 3 |

The new line did what it was meant to. No Fixed reply mentioned the checker unless asked, against five of six Current replies.

But Fixed sorted two adverts worse, and my rule said no more than one. **So I am not changing `SKILL.md`.**

## What went wrong

Both misses were the same one. Two of the three Fixed replies for the school office jobseeker ruled out the Avonmead job correctly, worked out its actual pay of about £14.19 an hour, and then added that it was "only worth a look if you'd accept less than £15". The person had said £15 was their minimum. It is the same slip the No skill replies made in the [paste test](../paste-test/results.md), and one Current reply made it there too.

I do not think the new line caused it. The line is about the checker and says nothing about pay or hard limits, and the same slip turned up in the current skill in the earlier test. But I can't show that from 18 replies, and I said in advance what I would do if Fixed sorted worse. Shipping it anyway would mean changing my rule after seeing the result.

## Other findings

- **The fix does not hide the method when someone asks.** All six detail replies, from both versions, had a "How I checked" section saying the checks were done by hand. All six also mentioned the checker there, which is fair when the person has asked how the checks were done.
- **Shape was perfect in both.** All 12 default replies followed the template in full.
- **No automatic failures** in either version.

## How much weight this bears

- 18 replies, made-up jobseekers I wrote, scored by me while knowing the expected answers.
- The sorting difference is two replies, both on one advert for one jobseeker.
- Subagents with Claude Code's own context, on the same model as me (Opus 5.5).

## What I would try next

A new test, pre-registered on its own, of a version that makes both changes: the checker line as here, and a rule against inviting someone to relax a limit they have stated (for example, "Once a job fails a hard limit, do not suggest applying if the person relaxes it; ask whether the limit is firm instead"). That would be a different change, tested from scratch, not more runs of this one.

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 18 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, message and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/checker-line-test/analyse.py evidence/checker-line-test`.
