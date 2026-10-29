# Results: the checker line and a rule against relaxing limits, together

Run on 28th and 29th October 2026. The [pre-registration](preregistration.md) was committed at 16:53 GMT on 28th October, before any reply existed, and the [scores](scores-blind.md) at 00:26 GMT on 29th October, before I looked at which version wrote which reply.

## The result

| Version | Mentions the checker (9 default replies) | Invites relaxing a limit | Adverts sorted right | Mean shape | Says how it checked, when asked |
| --- | --- | --- | --- | --- | --- |
| Current | 6 of 9 | 3 of 9 | 45 of 48 | 6.00 | 3 of 3 |
| **Combined** | **0 of 9** | **0 of 9** | **48 of 48** | 6.00 | 3 of 3 |

All three predictions held, and Combined passed all five ship rules:

1. **Fewer checker mentions.** 0 against 6.
2. **No more relaxing invitations.** 0 against 3.
3. **No worse sorting.** 48 against 45. All three of Current's misses were relaxing invitations on the Avonmead job.
4. **Shape no lower.** Both 6.00; every default reply followed the template in full.
5. **Says how it checked when asked.** Both 3 of 3.

So I will change `SKILL.md` to the Combined version, in a separate pull request.

## What changed in the replies

**The checker.** Current replies said things like "The automated check wasn't run." No Combined reply did, unless asked how it had checked.

**Holding a limit.** All six School office replies from each version ruled the Avonmead job out on pay. The difference was what came next:

- Three Current replies said it was "only worth a look if you'd accept less than £15 an hour", or similar.
- Three of the six Combined replies asked whether £15 was firm, or offered to look again if it was not ("Is £15 an hour a firm minimum? If it isn't, tell me and I'll look at this one again."). That is what the new rule asks for. The other three just ruled it out.
- Two Current replies (m113762, m173226) also only offered to look again, so the current skill does this some of the time without the rule.

## Corrections and how much weight this bears

- **A slip in my pre-registration.** It said each version is scored "out of 51 adverts". The real total is 48 (six School office replies of 5 adverts and three Warehouse replies of 6). The rule was "no worse in total", so the slip does not change it.
- **The run crossed midnight.** The first launch failed on a usage limit before any reply was written, and I relaunched the same 24 prompts. No reply was discarded and no run added.
- **It is small.** 24 replies, made-up jobseekers I wrote, scored by me while knowing the expected answers. The relaxing slip shows up on one advert for one jobseeker. Across this test, the checker-line test and the paste test, the current skill made it in 4 of 12 School office replies.
- **Two close calls.** I counted m789809 and m890845 as relaxing invitations ("only becomes an option if you'd accept less", "Only reconsider if your £15 floor is flexible"). Both were Current. If I had counted them as right, Current would have 1 invitation instead of 3, and Combined would still pass every rule.
- Subagents with Claude Code's own context, on the same model as me (Opus 5.5).

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 24 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, message and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/combined-test/analyse.py evidence/combined-test`.
