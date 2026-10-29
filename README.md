# Find My Next Job

A free AI skill that sorts job adverts against your experience and your limits, and tells you which are worth applying for, which need a question answered first, and which to skip.

You tell it what you have done and what you need: hours, where you can work, the least you can be paid. It reads the adverts, checks each essential requirement against your experience, and gives you a short list with links and reasons. It never applies for jobs or contacts employers for you, and it does not promise you a job or an interview.

## Use it

The quickest way needs no install.

1. Open [SKILL.md](SKILL.md), click **Raw**, and copy the whole file.
2. Paste it into any AI chat (ChatGPT, Claude, Gemini, Copilot or similar).
3. Underneath, tell it about your work and what you need, then paste in the adverts you want checked. For example:

   > Help me find my next job. I've spent four years coordinating a small warehouse in Manchester. I plan rotas, answer customer emails and keep our stock spreadsheets in Excel. I need full-time hours, Manchester or remote within the UK, and at least £27,000 a year. Here are some adverts I found.

If your AI tool can search the web, you can ask it to look for jobs instead of pasting adverts. It should tell you which pages it could and could not open.

### Or install it

If you use an AI tool that loads skills from a folder, such as Claude Code or Codex, download this repository (the green **Code** button, then **Download ZIP**) and install the whole folder. Installed this way, the skill can also read its search guide in `references/` and run the optional checker in `scripts/`.

## What you get back

- A line saying what it checked, and whether it could open the employers' own pages.
- **Suitable leads:** jobs that meet everything you said you need, with the link, why they may suit you and anything to check before applying.
- **Conditional:** jobs that look promising but have one essential thing still to confirm, with the exact question to ask.
- **Unverified:** adverts it could not read in full, and what to find out.
- One next step.

Jobs that fail one of your limits are kept off the list, usually with a short reason. Ask "show me the detailed checks" to see how it judged each requirement.

Here is [an example reply](examples/first-interaction.md) for a made-up jobseeker.

## Things to know

- **Leave out personal details.** Your work history is enough. Don't paste your address, phone number, date of birth or ID numbers.
- **Check before you apply.** Adverts close and change. A job the skill calls suitable still needs you to open the employer's own page and read it.
- **Pay is taken as written.** If an advert gives a full-time figure for a part-time job, the skill does not treat that figure as your pay; where the advert gives the hours, it works out what you would actually get. If an advert says "competitive", it treats the pay as unknown.
- **It won't act for you.** It does not apply, message employers, set up alerts or pay for anything.

## What I have tested

I pasted the skill into a chat with two made-up jobseekers and eleven made-up adverts, some with traps, and compared it with asking the same question with no skill. With version 2.1.0 of the skill, 33 of 33 adverts were sorted correctly and all six replies came back in the shape above. Without it, 29 of 33 were right: on one jobseeker, every reply invited them to apply for a job below the pay they had said they needed. The full test, its limits and every reply are in [evidence/paste-test](evidence/paste-test/results.md).

The skill sometimes made the same slip, less often, so version 2.2.0 tells it to ask whether a limit is firm instead of suggesting you relax it. It also stops it mentioning an "automated check" that can't run in a chat. In a second test with the same jobseekers, 2.2.0 sorted 48 of 48 adverts correctly against 45 of 48 for 2.1.0, and never suggested relaxing a limit. See [evidence/combined-test](evidence/combined-test/results.md).

It is a small test that I designed and scored. It does not show that the skill helps anyone find a job faster or get more interviews, and I make no such claim. Live web search, reading a CV and longer conversations are not tested.

## For developers

The optional checker in `scripts/preflight.py` checks the records an AI tool writes about each job: that every limit has a check, that unknown essentials hold a job back, and that duplicate listings are matched. It needs Python 3.9 or later and no other packages. It does not open web pages and cannot tell whether a job is real or a good fit. The record format is in [references/record-contract.md](references/record-contract.md).

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/preflight.py --input examples/fictional-shortlist.json
```

## Licence

MIT. See [LICENSE](LICENSE).
