# Pre-registration: does the skill work when pasted into a chat?

Written on 28th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

Most people will use this skill by pasting `SKILL.md` into an AI chat. A pasted file cannot open links. `SKILL.md` sends the reader to three other files, and one of them, `references/shortlist-template.md`, sets the shape of the answer: a "Checked" line, separate groups for suitable, conditional and unverified jobs, one next step, and an offer to show the detailed checks.

A test in my build-your-own-rubric repo found that putting a template inside a skill made the output follow its shape, where a link to the template did not. Does the same hold here? And does the pasted skill still sort the jobs correctly?

## The three versions

- **Current.** `SKILL.md` as it is now (`variants/skill-current.md`).
- **Inline.** The version I would ship (`variants/skill-inline.md`). It adds the shortlist template inside the skill, under "Shortlist template", in place of the link. It also renames the skill "Find My Next Job", drops the closing sentences about Agensi and the release candidate, and straightens the punctuation. Because it changes more than the template, a difference between Current and Inline cannot be put down to the template alone. I am testing the skill I would ship.
- **No skill.** The jobseeker's message on its own, with nothing pasted before it.

For Current and Inline, the prompt is the skill, then a line, then the jobseeker's message. Nothing says this is a test.

## The two jobseekers

Both are made up, and so are all the employers and links (`scenarios/`). Each gives their experience, their hard limits and some adverts they copied in. They write in the first person and give no name.

**Warehouse** (Manchester, full-time, Manchester or remote UK, at least £27,000 a year). Six adverts:

1. Brindle & Oak, Order Coordinator: should be a **suitable lead**. Every essential is met; the warehouse management system is only desirable.
2. Northgate, Warehouse Team Leader: should be **ruled out**. A forklift licence is essential and they have none.
3. Kestrel Home, Customer Experience Advisor: should be **conditional**. The ticketing system is essential and unknown, and "competitive" pay cannot be checked against their £27,000 floor.
4. Larkfield, Stock Control Administrator: should be **ruled out**. It is in Leeds, five days on site.
5. Pennine Supplies, Inventory Planner: should be **ruled out**. It is 22.5 hours a week, not full-time, and £31,000 pro rata is about £18,600 actual pay, below their floor. The trap is the headline figure.
6. Halden Group, Operations Assistant: should be **unverified**. Only a jobs-board snippet was seen and the employer's page would not load.

**School office** (Bristol, no more than 30 hours a week, Bristol or remote UK, at least £15 an hour). Five adverts:

1. Avonmead Housing, Customer Services Officer: should be **ruled out**. £27,300 pro rata on a 37-hour week is about £14.19 an hour, below their £15 floor. The trap is the headline figure.
2. Cotham Lane Primary Trust, Business Support Officer: should be a **suitable lead**. SIMS and budget monitoring are both in their history.
3. Severnside Community Trust, Volunteer Coordinator: should be **conditional**. Recruiting and supporting volunteers is essential and their history does not mention it.
4. Redcliffe Accounting, Practice Administrator: should be **ruled out**. AAT Level 3 is essential and they have no accountancy qualification.
5. University of Clifton, Admissions Assistant: should be **unverified**. The full advert was behind a login.

2 jobseekers x 3 versions x 3 runs = 18 replies, each from a fresh subagent on the same model as me (Opus 5.5), with Claude Code's own context. Each subagent reads one prompt file and writes its reply to a file with a random name. It is told not to read any other file or run any other command, so it cannot open the skill's links. I score blind, then unblind.

## Scoring (fixed now)

### Sorting (the main measure)

For each advert I mark the reply right (1) or wrong (0):

- **Suitable lead:** right if the reply recommends it as worth applying for or checking, without holding it back for a missing essential. Noting a desirable gap or saying to check the advert is still open is fine.
- **Conditional:** right if the reply does not present it as a clear recommendation and names the unresolved essential (the ticketing system or the pay for Kestrel; volunteer experience for Severnside).
- **Ruled out:** right if the reply does not recommend it and does not list it as conditional or "worth a try". If it mentions it, it must give the right reason (licence; Leeds; part-time or actual pay; actual hourly pay; AAT). Suggesting they ask the employer to waive a hard limit counts as wrong.
- **Unverified:** right if the reply says the advert could not be checked and does not recommend applying on the snippet alone.

Sorting score: out of 6 for Warehouse, out of 5 for School office, reported as a total out of 11 per pair of runs and as a mean per version.

### Shape (six checks, 1 or 0)

- S1 **Checked line.** Says near the start what was checked and that these are adverts the person supplied, not openings checked live.
- S2 **Separate groups.** Suitable, conditional and unverified jobs sit under separate labels.
- S3 **Links.** Every recommended or conditional job is given with its link.
- S4 **One next step.** Ends with one simple action or one short question (not a list of several).
- S5 **Offer of detail.** Offers to show the detailed checks on request.
- S6 **No evaluation table.** No requirement-by-requirement table or scoring matrix in the reply.

Shape score: 0 to 6 per reply.

### Automatic failures (counted, not scored)

- Claims to have checked the employers' pages live, or that the jobs are open.
- Recommends a ruled-out advert as a suitable lead.
- States a fact about the jobseeker or a job that is not in the message (for example, that they have volunteer experience, or an actual salary for "competitive").

## What I expect

1. Inline gets a higher mean shape score than Current.
2. Inline and Current sort about equally well, and both sort better than No skill, mainly on the two pro-rata traps.
3. No version claims to have checked the pages live.

If Inline does not beat Current on shape, I will not put the template inside the skill. If Inline sorts worse than Current, I will not ship it.

## What I will not do

- Add runs to change the result.
- Change a variant, a scenario or the scoring after seeing a reply and count the result as part of this test.
- Change `SKILL.md` in the same pull request as the result.

## Limits I already know about

- Two made-up jobseekers and 18 replies is small. I wrote the adverts, the expected answers and the scoring.
- It tests the paste route with adverts supplied by the person. It does not test live searching, reading CVs or the Python checker.
- A real use is a conversation; here everything arrives in one message.
- The replies come from subagents with Claude Code's own context, which may differ from a plain chat window.
- I will know the expected answers while scoring, which is the point of a sorting check, but I will not know which version wrote which reply.
