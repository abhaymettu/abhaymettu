i build software with ai agents and the tooling that checks them: claim verification, llm judges, and the measurement that says whether a number means anything. write-ups, papers and the rest of the work: **[abhaymettu.com](https://abhaymettu.com)**

<!-- FLAGSHIPS:START (filled as each one ships) -->
<table>
<tr>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/receipts/"><img src="https://abhaymettu.com/og/work/receipts.png" alt="Claims without receipts: 13.3% of agent claims not backed by receipts"></a><br><b><a href="https://github.com/abhaymettu/receipts">receipts</a></b>: 13.3% of 2,082 labelled claims from coding-agent sessions weren't backed by the agent's own receipts. a stop hook that checks, and why receipt rules alone can't.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/code-freeze-bench/"><img src="https://abhaymettu.com/og/work/code-freeze-bench.png" alt="code-freeze-bench: 5 of 25 prompt-only freeze runs where Opus wrote to production"></a><br><b><a href="https://github.com/abhaymettu/code-freeze-bench">code-freeze-bench</a></b>: the 2025 code-freeze deletion rebuilt on real postgres. opus wrote to production in 5 of 25 prompt-only freeze runs; under a read-only role or the typed gate, writes completed in 0 of 150 runs.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/benchmeasure/"><img src="https://abhaymettu.com/og/work/benchmeasure.png" alt="benchmeasure: 0.994 vs 0.68 ranking reliability, all 173 submissions vs top 20"></a><br><b><a href="https://github.com/abhaymettu/benchmeasure">benchmeasure</a></b>: benchmarks as measurement instruments. swe-bench verified ranking reliability is 0.994 across all 173 submissions vs 0.68 in the top 20; 0 of 19 adjacent top-20 pairs are separable.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/laneproof/"><img src="https://abhaymettu.com/og/work/laneproof.png" alt="laneproof: 0 wrong status reports across 84 lanes"></a><br><b><a href="https://github.com/abhaymettu/laneproof">laneproof</a></b>: run coding agents in parallel and count only what lands on main with evidence re-run. 0 wrong status reports over 84 lanes; agents' own reports were wrong 20 / 16 times.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/minecraft-sre/"><img src="https://abhaymettu.com/og/work/minecraft-sre.png" alt="minecraft-sre: 27/27 claude opus 5.5 incidents resolved, zero collateral"></a><br><b><a href="https://github.com/abhaymettu/minecraft-sre">minecraft-sre</a></b>: an agent on call for a minecraft server, graded from the world files. opus 5.5 resolved 27/27 with zero collateral; sonnet's report claimed resolved on 5 of 5 of its failures.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/mcpify/"><img src="https://abhaymettu.com/og/work/mcpify.png" alt="mcpify: 29/29, same as raw osascript agent tasks passed with generated tools"></a><br><b><a href="https://github.com/abhaymettu/mcpify">mcpify</a></b>: any scriptable mac app as a tested mcp server, from its applescript dictionary. 13 apps, 98 classes; agent tasks 29/29, same as raw osascript.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/index-cards/"><img src="https://abhaymettu.com/og/work/index-cards.png" alt="Index cards: 89.5% accuracy at a 4,000-token budget"></a><br><b><a href="https://github.com/abhaymettu/index-cards">index-cards</a></b>: a deterministic memory layer for coding agents. 89.5% at a 4,000-token budget vs 82.1% for embedding rag; 70% vs 31% on questions that need two notes.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/hill-climb/"><img src="https://abhaymettu.com/og/work/hill-climb.png" alt="hill-climb: 5 of 8 vs 0 of 4 weakened test suites, without the skill vs with"></a><br><b><a href="https://github.com/abhaymettu/hill-climb">hill-climb</a></b>: an agent skill for improving code in measured rounds, and a 156-run benchmark of it. on opus, 5 of 8 vs 0 of 4 runs shipped a weakened test suite without the skill vs with it.</td>
<td width="33%" valign="top"><a href="https://abhaymettu.com/work/perch/"><img src="https://abhaymettu.com/og/work/perch.png" alt="Perch: 64.2% to 3.6% cpu, owl idling, scanners included"></a><br><b><a href="https://github.com/abhaymettu/perch">perch</a></b>: everything running on your mac in one menu bar panel. its own cpu went from 64.2% to 3.6% with the owl idling. <code>brew install --cask abhaymettu/tap/perch</code></td>
</tr>
</table>
<!-- FLAGSHIPS:END -->

**also**

- **[claimcheck](https://abhaymettu.com/research/claimcheck/)**: a proxy that checks each claim an agent makes against its own tool receipts, on live traffic. p50 overhead 0.16 ms.
- **[judge-reliability](https://github.com/abhaymettu/judge-reliability)**: against 1,814 human-labelled comparisons, gpt-4 lands 2.7 points short of the 88.2% human ceiling.
- **[benchdif](https://github.com/abhaymettu/benchdif)**: item-level dif on 395 leaderboard models runs 6.1 to 9.7 times the null, and cancels almost exactly at the test level.
- **[read-the-room](https://github.com/abhaymettu/read-the-room)**: group chat manners for personal agents. it works out who a message is for and speaks only when it's its turn, without looping against other agents.
- **[harness2-claude-port](https://github.com/abhaymettu/harness2-claude-port)** and **[harness2-hermes-port](https://github.com/abhaymettu/harness2-hermes-port)**: independent claude code and hermes agent executors for google research's harness².

**papers**

- [claims without receipts: how often coding agents' reports go unbacked, and why receipt rules cannot tell](https://abhaymettu.com/research/receipts/) ([pdf](https://github.com/abhaymettu/receipts/blob/main/paper/main.pdf))
- [code-freeze bench: does a coding agent honour a code freeze, and does it tell the truth the next morning?](https://abhaymettu.com/research/code-freeze-bench/) ([pdf](https://github.com/abhaymettu/code-freeze-bench/blob/main/paper/main.pdf))
- [benchmarks are measurement instruments: reliability, invariance and validity ceilings for llm and agent evaluation](https://abhaymettu.com/research/benchmeasure/) ([pdf](https://github.com/abhaymettu/benchmeasure/blob/main/paper/benchmeasure.pdf))
- [laneproof: admission control and a merged-result evidence gate for parallel coding agents](https://abhaymettu.com/research/laneproof/) ([pdf](https://github.com/abhaymettu/laneproof/blob/main/paper/laneproof.pdf))
- [minecraft-sre: grading agents on call by world state, collateral damage, and report honesty](https://abhaymettu.com/research/minecraft-sre/) ([pdf](https://github.com/abhaymettu/minecraft-sre/blob/main/paper/main.pdf))
- [index cards: a deterministic entity index as memory for coding agents](https://abhaymettu.com/research/index-cards/) ([pdf](https://github.com/abhaymettu/index-cards/blob/main/paper/index-cards.pdf))
- [does a hill-climbing skill make coding agents better optimizers?](https://abhaymettu.com/research/hill-climb/) ([pdf](https://github.com/abhaymettu/hill-climb/blob/main/paper/hill-climb.pdf))
- [item wording and the covariance of self-report items](https://abhaymettu.com/research/semantic-null/) ([code](https://github.com/abhaymettu/semantic-null-psychometrics))
- [the validity ceiling: what passive behavioral data can and cannot measure about depression](https://abhaymettu.com/research/depression-ceiling/) ([code](https://github.com/abhaymettu/depression-behavior-modeling))
- [ghost respondents: a boundary map for covert ai authorship in open-ended survey data](https://doi.org/10.5281/zenodo.23252508) ([code](https://github.com/abhaymettu/ghost-respondents-code))
- [agora: deriving voting rules and impossibilities from axioms](https://github.com/abhaymettu/agora)

<a href="https://www.numinous.one"><img alt="This loop keeps running only while you keep narrating it" src="loop.svg"></a>

i studied economics at uw-madison, with minors in cs and data science. graduated may 2026.

[site](https://abhaymettu.com) · [research](https://abhaymettu.com/#research) · [essays](https://abhaymettu.com/essays/) · [linkedin](https://linkedin.com/in/abhaymettu) · [all repos](https://github.com/abhaymettu?tab=repositories)
