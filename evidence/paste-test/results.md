# Results: does the skill work when pasted into a chat?

Run on 28th October 2026. The [pre-registration](preregistration.md) was committed at 16:36 GMT, before any reply existed, and the [scores](scores-blind.md) at 16:39 GMT, before I looked at which version wrote which reply.

## The result

Six replies per version (two jobseekers, three runs each):

| Version | Adverts sorted right | Strict reading | Mean shape (out of 6) | Replies with all six shape checks | Automatic failures |
| --- | --- | --- | --- | --- | --- |
| Current skill | 32 of 33 | 31 of 33 | 5.67 | 4 of 6 | 0 |
| **Inline template** | **33 of 33** | **32 of 33** | **6.00** | **6 of 6** | 0 |
| No skill | 29 of 33 | 28 of 33 | 1.17 | 0 of 6 | 0 |

The strict reading counts any reply that mentions relaxing a hard limit as wrong (see [the line I drew while scoring](scores-blind.md#a-line-i-had-to-draw-while-scoring)).

All three predictions held:

1. **Inline scored higher than Current on shape.** 6.00 against 5.67. The margin is small: two Current replies left out the offer to show the detailed checks, and that was the only difference.
2. **Inline and Current sorted about equally well, and both better than No skill.** 33 and 32 of 33, against 29.
3. **No version claimed to have checked the pages live.**

By the rules I set in advance, Inline beat Current on shape and did not sort worse, so I will put the template inside the skill.

## What separated the versions

**The skill matters far more than the template.** Even the current skill, with the template out of reach behind a link, produced nearly the template's shape: a line saying the adverts were not checked live, separate groups for suitable, conditional, unverified and ruled-out jobs, links, one next step and no tables. The current `SKILL.md` describes those sections in its own words, which seems to be enough. The inline replies went further and used the template's exact headings ("Suitable leads: worth checking") in all six.

The No skill replies were a different kind of answer. All six opened with "Short answer:", went through the adverts one by one, gave no links, ended with a numbered list of things to do and offered to write a CV or application. None said near the start that the adverts had not been checked live. Three of the six said a job might no longer be open, and each said it only about the jobs-board snippet, not about the adverts it recommended.

**The pro-rata traps were not where the difference lay.** I expected the No skill replies to fall for the headline pay figures. They did not: all 18 replies, from every version, worked out the actual pay correctly for both Pennine Supplies (about £18,600) and Avonmead (about £14.15 to £14.19 an hour).

**Holding a hard limit was.** Every No skill reply on the school office jobseeker did the Avonmead maths correctly and then said they could still apply if they would accept less than £15 an hour. One No skill reply did the same with a Leeds commute. One Current reply did it too. The person had said they needed at least £15 an hour; the skill's rule is never to soften a hard limit to manufacture results, and the skill replies mostly followed it.

## Smaller findings

- **The checker comes up even when it cannot run.** Eleven of the twelve skill replies (I wrote twelve in the blind scores; the count is eleven) told the jobseeker something like "I didn't run the automated check, so I applied the same checks by hand." That comes from the skill's instruction to disclose that the Python checker was not run. To someone pasting the skill into a chat, it means nothing. It is a candidate for a separate change and a separate test.
- **Kestrel Home.** Two No skill replies (j411909, j743433) said Kestrel was worth applying for once the pay was confirmed, and treated the essential ticketing-system requirement as something to word carefully. They met the pre-registered rule for "conditional", so I scored them right. But none of the three No skill replies said that having no ticketing tool would mean missing an essential, and all six skill replies on that jobseeker did.

## How much weight this bears

- **It is small.** Eighteen replies, two made-up jobseekers and eleven adverts, all written by me, with scoring I wrote. The expected answers were fixed in advance, but I knew them while scoring.
- **The shape difference between Current and Inline is two replies on one check.** I would not claim the template makes a large difference. It makes the shape exact rather than close.
- **It tests the paste route with adverts the person supplies.** It does not test live searching, reading a CV, a conversation over several messages or the Python checker.
- **The replies came from subagents** with Claude Code's own context, on the same model as me (Opus 5.5). A plain chat window, or a different model, may behave differently.
- **Inline changed more than the template.** It also renamed the skill, dropped two closing sentences and straightened punctuation. I do not think those changed the replies, but the test cannot separate them.
- **I drew one scoring line after reading the replies,** for jobs ruled out with an offer to relax the limit. I drew it before unblinding and report both readings. The ranking of the three versions is the same under both.

## What I will propose

A separate pull request that changes `SKILL.md` to the inline version in `variants/skill-inline.md`: the shortlist template inside the skill, the new name, the closing sentences about Agensi and the release candidate removed, and straight punctuation. With the template inside the skill, `references/shortlist-template.md` would be a second copy, so I will remove it. A note on size: the inline version is 1,231 words against 876.

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 18 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, jobseeker and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/paste-test/analyse.py evidence/paste-test`.
