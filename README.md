<img alt="Python REPL: an assertion gate scores an agent turn and flags one unverified assertion, a link claimed reusable that the trace shows was never fetched" src="repl.svg">

Computer science and economics from UW–Madison, May 2026. Machine learning
with data across all fields, and agent infrastructure that takes care of the
tedious parts. The interesting parts get measured and written up as research.

Reports with figures live at [abhaymettu.com](https://www.abhaymettu.com).
Ideas that outgrow a commit message turn into
[essays](https://www.abhaymettu.com/essays/).

### Speech and realtime voice

| | |
|---|---|
| [expressive-s2s](https://github.com/abhaymettu/expressive-s2s) | A voice agent that hears how you sound and answers in a matching voice, median 558 ms against its own serial control at 895 ms. The whole downstream pipeline runs inside the endpointer's 350 ms hangover instead of after it, so emotion detection costs 0 ms once overlapped. The classifier still calls flat synthetic audio anger at 0.96 confidence. |
| [fullduplex-voice](https://github.com/abhaymettu/fullduplex-voice) | A tuned cascade answers in 386 ms. Moshi answers in 165 ms on the same laptop and stops 170 ms after you interrupt it, where the cascade talks over you for 1,173 ms. Cutting the endpointer hangover by 230 ms bought 19 ms, because every millisecond taken off it reappears as exposed pipeline work. |
| [turn-end-prediction](https://github.com/abhaymettu/turn-end-prediction) | An 80 ms silence threshold sits at the median pause a person takes while still speaking, so it misreads about half of them. A GRU over the trailing second of prosody reaches the same error rate 195 ms sooner, at 2.4 ms per decision. |
| [voice-aliveness-bench](https://github.com/abhaymettu/voice-aliveness-bench) | Five dimensions of whether a voice agent feels alive, measured. The response gap tracks reply length at rho 0.80 to 0.89 and not question difficulty, and four of the five dimensions floor at zero for every system tested, each with a positive control showing the detector would have fired. |
| [aliveness-threshold](https://github.com/abhaymettu/aliveness-threshold) | Built to price a non-verbal cue in milliseconds of tolerated latency. The data cannot produce that number: LLM judges move +2.19 on aliveness for a cue that was described to them and +0.16 per second of real silence, so they rate the description, not the timing. |
| [emotion-label-ceiling](https://github.com/abhaymettu/emotion-label-ceiling) | The same wav2vec2 predictions score 73.4% against what the actor was told to perform and 47.8% against what listeners heard. No model can exceed 72.7% against the crowd on audio-only CREMA-D, and four published results sit above that line. |
| [expressive-tts-audit](https://github.com/abhaymettu/expressive-tts-audit) | A neural TTS engine's four expressive presets are recovered from acoustics 49.3% of the time, a 1990s formant synthesiser's 95.8%. The neural engine has no pitch control, and pitch is where the signal lives. |
| [prosody-transplant](https://github.com/abhaymettu/prosody-transplant) | Piper has no pitch knob, so this builds one with WORLD resynthesis: preset recovery goes from 52.8% to 100% for 75 ms. Zero human raters, so 100% means separable, not that it sounds good. |

### Machine learning systems

| | |
|---|---|
| [judge-reliability](https://github.com/abhaymettu/judge-reliability) | An LLM judge agrees with the human majority 85.5% of the time against an 88.2% human ceiling, and only 14.9 points above a rule that reads none of the text and picks the longer answer. |
| [retrieval-ablation](https://github.com/abhaymettu/retrieval-ablation) | Hybrid retrieval beats BM25 by 0.204 nDCG@10 on fiqa. A cross encoder over the top 100 makes all three BEIR datasets worse, and Recall@100 caps what any reranker could recover. |
| [drift-guard](https://github.com/abhaymettu/drift-guard) | Four drift detectors scored on detection delay against false alarm rate. The automatic rollback fires on schedule and costs a further 0.0615 AUC, because it falls back to another pre-shift model. |
| [benchdif](https://github.com/abhaymettu/benchdif) | Differential item functioning for LLM benchmarks, validated to machine precision against statsmodels. Across 395 leaderboard models, item-level DIF between Mistral and Llama-2 families is 6 to 10x sampling noise and cancels at the test level. A 100-item subset does not cancel: it shifts the family gap by 0.5 to 0.95 on held-out models. |

### Quantitative finance

| | |
|---|---|
| [factor-haircut](https://github.com/abhaymettu/factor-haircut) | Eight price and volume factors. One clears a costless t of 2.0 and none survive a multiple testing haircut. Momentum breaks even at 199 bps, 20x the headline cost, so it fails on significance rather than on cost. |
| [vol-horserace](https://github.com/abhaymettu/vol-horserace) | Gradient boosting beats HAR-RV on QLIKE at a one day horizon and is thrown out of the 90% model confidence set at 22 days. |
| [kalshi-calibration](https://github.com/abhaymettu/kalshi-calibration) | Kalshi prices are calibrated. What a naive backtest reads as edge is 65% bid-ask spread, and fees consume 86% of what survives. |
| [treasury-curve-rv](https://github.com/abhaymettu/treasury-curve-rv) | Svensson residuals on 5,130 daily Treasury curves mean-revert at every tenor, which says nothing: for iid noise the reversion beta is exactly -1, so the no-signal benchmark is -1 and not 0. The real curves sit at -0.046 at one day, so residuals are persistent, not fast-reverting. |

### Real estate and markets

| | |
|---|---|
| [assessment-regressivity](https://github.com/abhaymettu/assessment-regressivity) | 39.6% of Dane County sales closing before the lien date carry an assessed value equal to the sale price to the dollar, against 1.0% after it. The obvious hedonic control is a trap that moves the regressivity estimate from -0.113 to -0.413; the uncontaminated one leaves -0.0626. |
| [comps-error](https://github.com/abhaymettu/comps-error) | Comparable-sales valuation misses by 19.4% at the median on 168,178 held-out New York sales, and loses to the market value the city publishes for free at 17.7%. Estimates were committed before the scoring code existed. |
| [permit-lifecycle](https://github.com/abhaymettu/permit-lifecycle) | Permit to completion runs 7 months for a single house and 23 for a 50-unit project, so there is no single lag. The never-built share does not generalise at all, 0.9% to 9.4% across six cities. |

### Commercial and category analytics

| | |
|---|---|
| [energy-category-share-shift](https://github.com/abhaymettu/energy-category-share-shift) | Category share from two issuers' SEC scanner exhibits. Cross-issuer disagreement is 2.16 share points, larger than most published shifts. |
| [energy-category-forecast](https://github.com/abhaymettu/energy-category-forecast) | A driver-based share forecast that lost to a no-change baseline on backtest, so the scenario range shipped instead of a point estimate. |

### Healthcare and payer analytics

| | |
|---|---|
| [msdrg-severity-capture](https://github.com/abhaymettu/msdrg-severity-capture) | Severity coding screened across 2,906 hospitals. The same code flags 1,000 hospitals or 70 depending on one defensible choice about suppressed cells, so the public file cannot settle it. |
| [hospital-margin-variance](https://github.com/abhaymettu/hospital-margin-variance) | Payer mix is the smallest of six drivers of hospital operating margin, and 68.7% of the variation is not explained by any of them. |
| [cms-inpatient-warehouse](https://github.com/abhaymettu/cms-inpatient-warehouse) | DuckDB star schema over 292,306 Medicare discharges, with a 35-check test suite proved by injecting faults rather than by passing. |
| [ncd-310-coverage-engine](https://github.com/abhaymettu/ncd-310-coverage-engine) | Medicare NCD 310.1 as a testable rules engine over 8,131 trials. 75% are undecidable from public fields, and that is the finding. |
| [clinic-overbooking-policy](https://github.com/abhaymettu/clinic-overbooking-policy) | A no-show model beats a flat rule by 0.4 clinician minutes, and does worse than no model once calibration drifts with AUC unchanged. |
| [ehr-data-quality-harness](https://github.com/abhaymettu/ehr-data-quality-harness) | 20 of 24 data quality checks fire zero times on clean data, so the deliverable is the fault injection that scores the scorecard. |
| [trial-budget-variance](https://github.com/abhaymettu/trial-budget-variance) | Price-volume-mix bridge on CMS fee schedules. 89% of a $99,498 gap is enrolment volume, and the five components reconcile exactly. |
| [brfss-vs-places](https://github.com/abhaymettu/brfss-vs-places) | CDC PLACES reproduces about 75% of the true between-area variance in the direct BRFSS estimate, so it ranks areas well and understates every gap. The thin-sample explanation does not hold: the compression is there at every area size. |
| [clinvar-acmg-cohort](https://github.com/abhaymettu/clinvar-acmg-cohort) | ACMG reportable variants over 9M ClinVar rows. Only 3.9% have a usable frequency, so every prevalence is a lower bound. |

### Psychology and population health

| | |
|---|---|
| [reddit-selfdistance](https://github.com/abhaymettu/reddit-selfdistance) | Preregistered. One of two dictionaries missed its own validation threshold, so the hypothesis resting on it was downgraded. |
| [population-mental-health](https://github.com/abhaymettu/population-mental-health) | Cox models on MIDUS and NHANES, including a correction to a hazard ratio I first reported wrong. |
| [phq9-measurement-invariance](https://github.com/abhaymettu/phq9-measurement-invariance) | PHQ-9 invariance fails across sex on one somatic item, and about 11% of the published sex gap is the instrument rather than the people. The race verdict flips on a modelling default nobody reports. |
| [ews-mood](https://github.com/abhaymettu/ews-mood) | Critical-slowing-down indicators for mood transitions. A nominally 5% test rejected 28 to 43% under the null. |
| [working-memory-diffusion](https://github.com/abhaymettu/working-memory-diffusion) | Drift rate is the behavioural measure that working-memory connectivity predicts best across 1,069 HCP subjects. It adds information beyond accuracy and RT only where its edge map diverges from accuracy's: r = 0.229 at 0-back, nothing at 2-back. |
| [covary](https://github.com/abhaymettu/covary) | Two survey variables can each have n in the thousands and a joint n of exactly zero, with no error and no warning. A CLI that says which dataset-years measured both on the same respondents, built after exactly that killed a design. |

### Engineering and tools

| | |
|---|---|
| [paper-lecture](https://github.com/abhaymettu/paper-lecture) | Turns a paper PDF into a narrated lecture and an Anki deck. Local TTS, no API keys. |
| [recap](https://github.com/abhaymettu/recap) | Records a successful computer-use agent run as a typed capability, replays it deterministically, and heals it when the UI moves. |
| [claude-desktop-to-code](https://github.com/abhaymettu/claude-desktop-to-code) | Routes work from a Claude Desktop chat into Claude Code, headless or handed to a real terminal with the session history intact. |
| [temporal-grounding](https://github.com/abhaymettu/temporal-grounding) | Claude skill that catches a date the user asserts against the date already in context. Built test first over about 40 isolated runs. |
| [writing-from-dated-sources](https://github.com/abhaymettu/writing-from-dated-sources) | Claude skill that stops a stale document being rewritten as fresh present-tense prose. Base rate measured over 613 real files. |
| [tcc-helper](https://github.com/abhaymettu/tcc-helper) | One signed macOS app holds your privacy grants, so CLI tools that move on every update stop losing them. TCC.db on this machine held separate grant sets for 14 Claude version paths. |
| [cate-dispatch](https://github.com/abhaymettu/cate-dispatch) | Rough thought in, spec'd Claude Code agent out, running in a Cate terminal panel and a git worktree, with a board of who is working, who needs you and who is done. |
| [claude-file-links](https://github.com/abhaymettu/claude-file-links) | Makes the files Claude Code sends you clickable in the terminal, as OSC 8 hyperlinks. One hook. |
| [conscious](https://github.com/abhaymettu/conscious) | A macOS daemon that takes the whole screen for twenty seconds at unpredictable intervals, one sentence and a breath, and will not let you click away. |

<a href="https://www.numinous.one"><img alt="This loop keeps running only while you keep narrating it" src="loop.svg"></a>

Analyst and research roles where the job is to build the number and then find
out whether it holds. Washington State, Chicago, Boston or Madison WI, and I
will move.
[abhaymettu.com](https://www.abhaymettu.com) · abhaymettu12@gmail.com