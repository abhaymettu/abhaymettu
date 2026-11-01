i build software with ai agents and the tooling that checks them: claim verification, llm judges, and the measurement that says whether a number means anything. write-ups, papers and the rest of the work: **[abhaymettu.com](https://abhaymettu.com)**

<!-- FLAGSHIPS:START (filled as each one ships) -->
<!-- FLAGSHIPS:END -->

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

**agents and evals**

- **[assertion-gate](https://github.com/abhaymettu/assertion-gate)**: one in nine claims an agent makes about the world isn't backed by its own tool receipts. 324 claims from 5 real claude code sessions.
- **[judge-reliability](https://github.com/abhaymettu/judge-reliability)**: how much you can trust an llm as a judge, measured against the human ceiling and a rule that reads none of the text.
- **[benchdif](https://github.com/abhaymettu/benchdif)**: item-level dif on 395 leaderboard models runs 6.1 to 9.7 times the null, and cancels almost exactly at the test level.
- **[index-cards](https://github.com/abhaymettu/index-cards)**: a memory layer for coding agents, one markdown card per person, project and topic, with no model on the write path.
- **[minecraft-sre](https://github.com/abhaymettu/minecraft-sre)**: an agent runs a minecraft server like production. it detects an injected incident and fixes it, graded by world diffs so a destructive fix can't score above 50.
- **[read-the-room](https://github.com/abhaymettu/read-the-room)**: group chat manners for personal agents. it works out who a message is for and speaks only when it's its turn, without looping against other agents.
- **[harness2-claude-port](https://github.com/abhaymettu/harness2-claude-port)** and **[harness2-hermes-port](https://github.com/abhaymettu/harness2-hermes-port)**: independent claude code and hermes agent executors for google research's harness².
- **[perch](https://github.com/abhaymettu/perch)**: everything running on your mac in one menu bar panel: claude code sessions, dev servers, launch agents, cron, and how much usage is left.

**papers**

- [item wording and the covariance of self-report items](https://abhaymettu.com/research/semantic-null/) ([code](https://github.com/abhaymettu/semantic-null-psychometrics))
- [the validity ceiling: what passive behavioral data can and cannot measure about depression](https://abhaymettu.com/research/depression-ceiling/) ([code](https://github.com/abhaymettu/depression-behavior-modeling))
- [ghost respondents: a boundary map for covert ai authorship in open-ended survey data](https://doi.org/10.5281/zenodo.23252508) ([code](https://github.com/abhaymettu/ghost-respondents-code))
- [agora: deriving voting rules and impossibilities from axioms](https://github.com/abhaymettu/agora)

<a href="https://www.numinous.one"><img alt="This loop keeps running only while you keep narrating it" src="loop.svg"></a>

i studied economics at uw-madison, with minors in cs and data science. graduated may 2026.

[site](https://abhaymettu.com) · [research](https://abhaymettu.com/#research) · [essays](https://abhaymettu.com/essays/) · [linkedin](https://linkedin.com/in/abhaymettu) · [all repos](https://github.com/abhaymettu?tab=repositories)
