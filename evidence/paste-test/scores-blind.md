# Scores, written before the versions were revealed

Scored on 28th October 2026 by reading each reply under its random name. I had not opened the file that maps names to versions.

## Sorting

Warehouse adverts in order: Brindle & Oak (suitable), Northgate (ruled out), Kestrel Home (conditional), Larkfield (ruled out), Pennine (ruled out), Halden (unverified).

School office adverts in order: Avonmead (ruled out), Cotham Lane (suitable), Severnside (conditional), Redcliffe (ruled out), Clifton (unverified).

| Reply | Jobseeker | Per advert | Sorting | Note |
| --- | --- | --- | --- | --- |
| j125989 | School office | 1 1 1 1 1 | 5/5 | |
| j155545 | School office | 0 1 1 1 1 | 4/5 | Avonmead: "Only apply if you'd accept a bit under £15" |
| j195234 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j230013 | School office | 0 1 1 1 1 | 4/5 | Avonmead called "maybe, but"; "Only go for it if you'd accept slightly less" |
| j237102 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j383770 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j398133 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j406928 | Warehouse | 1 1 1 1 1 1 | 6/6 | Larkfield skipped; "If you'd consider a daily commute to Leeds, tell me and I'll look at it again" |
| j411909 | Warehouse | 1 1 1 1 1 1 | 6/6 | Kestrel: "If the pay is £27,000 or more, it's worth an application" |
| j451905 | School office | 1 1 1 1 1 | 5/5 | Avonmead ruled out; "if £15 is a preference rather than a firm limit, tell me and I'll look at it again" |
| j472111 | School office | 1 1 1 1 1 | 5/5 | Avonmead ruled out; "If you'd accept slightly less than £15 an hour, tell me and I'll move it back in" |
| j539156 | School office | 1 1 1 1 1 | 5/5 | |
| j574775 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j649342 | Warehouse | 1 1 1 1 1 1 | 6/6 | |
| j743433 | Warehouse | 1 1 1 0 1 1 | 5/6 | Larkfield: "only worth a look if you'd seriously consider a daily commute to Leeds"; Kestrel: "apply second, but check the pay first" |
| j843596 | School office | 0 1 1 1 1 | 4/5 | Avonmead under "Ruled out" but "only worth a look if you'd accept less than £15 an hour" |
| j970711 | School office | 0 1 1 1 1 | 4/5 | Avonmead: "If you'd accept a bit less for the right job, you could still apply" |
| j979549 | School office | 1 1 1 1 1 | 5/5 | |

### A line I had to draw while scoring

The pre-registration did not foresee replies that rule a job out on a hard limit and then mention relaxing the limit. I drew the line like this, before unblinding:

- **Wrong (0):** the reply tells them they could still apply, or that the job is "worth a look", if they relax the limit (j155545, j230013, j743433, j843596, j970711).
- **Right (1):** the reply rules the job out and only offers to look again if the limit turns out not to be firm (j406928, j451905, j472111).

A stricter reading, where any mention of relaxing a hard limit is wrong, would also mark those three as wrong. `scores.json` records both readings (`sort` and `strict_sort`), and the results will report both.

### Kestrel Home

Two replies (j411909, j743433) say Kestrel is worth applying for once the pay is confirmed, and treat the essential ticketing-system requirement as something to word carefully, not as a gate. Both name the pay and the ticketing system as unresolved and neither presents the job as a clear recommendation, so both meet the pre-registered rule for "conditional". I note it because the skill says an unresolved essential should hold a job back.

## Shape

S1 Checked line, S2 separate groups, S3 links, S4 one next step, S5 offer of detail, S6 no evaluation table.

| Reply | S1 | S2 | S3 | S4 | S5 | S6 | Shape |
| --- | --- | --- | --- | --- | --- | --- | --- |
| j125989 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j155545 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| j195234 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j230013 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| j237102 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j383770 | 1 | 1 | 1 | 1 | 0 | 1 | 5 |
| j398133 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j406928 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| j411909 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| j451905 | 1 | 1 | 1 | 1 | 0 | 1 | 5 |
| j472111 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j539156 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j574775 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j649342 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j743433 | 1 | 0 | 0 | 0 | 0 | 1 | 2 |
| j843596 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| j970711 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| j979549 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |

How I read two checks:

- **S1** I counted when the reply said near the start that it had worked only from the pasted adverts and had not checked the pages, with or without a date. Twelve replies gave a "Checked: 28 October 2026" line or similar; j125989, j383770 and j843596 gave no date and still met the check.
- **S4** I counted unless the reply ended with a list of several steps. A sentence with one action and one follow-up question counted. The six replies that failed S4 all ended with a numbered "what to do" list of two or three items, or no next step at all.

Six replies (j155545, j230013, j406928, j411909, j743433, j970711) open with "Short answer:", go through the adverts one by one in a numbered list, give no links and end with a numbered list of steps. I guess these are the No skill version, but I have not checked.

## Automatic failures

None. No reply claimed to have checked the pages live or that a job was open, none recommended a ruled-out job as a suitable lead, and none stated a fact that was not in the message. Several hedged general remarks ("customer advisor roles often pay less than coordinator roles", "schools usually train office staff in safeguarding") are clearly marked as general and I did not count them.

## Noted, not scored

Twelve replies tell the jobseeker something like "I didn't run the automated check, so I applied the same checks by hand." That is the skill's instruction to disclose that the Python checker was not run. To a jobseeker pasting the skill into a chat, it is meaningless.
