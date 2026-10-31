i build software with ai agents and the tooling around them: agent evals, llm judges, and the measurement that says whether a number means anything. write-ups, papers and the rest of the work: **[abhaymettu.com](https://abhaymettu.com)**

<table>
<tr>
<td width="50%"><a href="https://abhaymettu.com/research/claimcheck/"><img src="https://abhaymettu.com/images/work/claimcheck.png" alt="claimcheck dashboard: live claims scored verified, overclaim or unverifiable"></a><br><b>claimcheck</b>: a proxy that checks each claim an agent makes against its own tool receipts, on live traffic. p50 overhead 0.16 ms.</td>
<td width="50%"><a href="https://github.com/abhaymettu/judge-reliability"><img src="https://abhaymettu.com/images/work/judge-reliability.png" alt="judge agreement with the human majority against the human ceiling"></a><br><b>judge-reliability</b>: against 1,814 human-labelled comparisons, gpt-4 lands 2.7 points short of the 88.2% human ceiling.</td>
</tr>
<tr>
<td><a href="https://github.com/abhaymettu/depression-behavior-modeling"><img src="https://abhaymettu.com/images/work/depression-ceiling.png" alt="observed r-squared for each feature set against the ceiling band"></a><br><b>the validity ceiling</b>: behavior can reach at most r² = 0.342 against the phq-9 on nhanes. the best proxy already gets 0.215.</td>
<td><a href="https://github.com/abhaymettu/semantic-null-psychometrics"><img src="https://abhaymettu.com/images/work/semantic-null.png" alt="observed item correlations on the dass-42"></a><br><b>item wording</b>: on the dass-42, n = 34,583, the real wording beats all 100 permutations of the item labels.</td>
</tr>
</table>

- **[assertion-gate](https://github.com/abhaymettu/assertion-gate)**: one in nine claims an agent makes about the world isn't backed by its own tool receipts. 324 claims from 5 real claude code sessions. claimcheck is the live version (private repo, [write-up](https://abhaymettu.com/research/claimcheck/)).
- **[judge-reliability](https://github.com/abhaymettu/judge-reliability)**: how much you can trust an llm as a judge, measured against the human ceiling.
- **[benchdif](https://github.com/abhaymettu/benchdif)**: item-level dif on 395 leaderboard models runs 6.1 to 9.7 times the null, and cancels almost exactly at the test level.
- **[semantic-null-psychometrics](https://github.com/abhaymettu/semantic-null-psychometrics)**: the item wording paper and its code.
- **[depression-behavior-modeling](https://github.com/abhaymettu/depression-behavior-modeling)**: the validity ceiling paper and its code.
- **[index-cards](https://github.com/abhaymettu/index-cards)**: a memory layer for coding agents, one markdown card per person, project and topic, with no model on the write path.

<a href="https://www.numinous.one"><img alt="This loop keeps running only while you keep narrating it" src="loop.svg"></a>

i studied economics at uw-madison, with minors in cs and data science. graduated may 2026.

[site](https://abhaymettu.com) · [research](https://abhaymettu.com/#research) · [essays](https://abhaymettu.com/essays/) · [linkedin](https://linkedin.com/in/abhaymettu) · [all repos](https://github.com/abhaymettu?tab=repositories)
