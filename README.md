<picture>
  <source media="(prefers-color-scheme: dark)" srcset="header-dark.svg">
  <img alt="Every one of them says what did not hold. Precision against 200 blind hand-coded posts: obligation 0.52, self-criticism 0.94, against a preregistered threshold of 0.70." src="header-light.svg">
</picture>

Economics from UW–Madison, May 2026. Machine learning evaluation, quantitative
finance and healthcare analytics.

Write-ups with figures live at [abhaymettu.com/research](https://www.abhaymettu.com/research/).

### Machine learning systems

| | |
|---|---|
| [judge-reliability](https://github.com/abhaymettu/judge-reliability) | An LLM judge agrees with the human majority 85.5% of the time against an 88.2% human ceiling, and only 14.9 points above a rule that reads none of the text and picks the longer answer. |
| [retrieval-ablation](https://github.com/abhaymettu/retrieval-ablation) | Hybrid retrieval beats BM25 by 0.204 nDCG@10 on fiqa. A cross encoder over the top 100 makes all three BEIR datasets worse, and Recall@100 caps what any reranker could recover. |
| [drift-guard](https://github.com/abhaymettu/drift-guard) | Four drift detectors scored on detection delay against false alarm rate. The automatic rollback fires on schedule and costs a further 0.0615 AUC, because it falls back to another pre-shift model. |

### Quantitative finance

| | |
|---|---|
| [factor-haircut](https://github.com/abhaymettu/factor-haircut) | Eight price and volume factors. One clears a costless t of 2.0 and none survive a multiple testing haircut. Momentum breaks even at 199 bps, 20x the headline cost, so it fails on significance rather than on cost. |
| [vol-horserace](https://github.com/abhaymettu/vol-horserace) | Gradient boosting beats HAR-RV on QLIKE at a one day horizon and is thrown out of the 90% model confidence set at 22 days. |
| [kalshi-calibration](https://github.com/abhaymettu/kalshi-calibration) | Kalshi prices are calibrated. What a naive backtest reads as edge is 65% bid-ask spread, and fees consume 86% of what survives. |

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
| [clinvar-acmg-cohort](https://github.com/abhaymettu/clinvar-acmg-cohort) | ACMG reportable variants over 9M ClinVar rows. Only 3.9% have a usable frequency, so every prevalence is a lower bound. |

### Psychology and population health

| | |
|---|---|
| [reddit-selfdistance](https://github.com/abhaymettu/reddit-selfdistance) | Preregistered. One of two dictionaries missed its own validation threshold, so the hypothesis resting on it was downgraded. |
| [population-mental-health](https://github.com/abhaymettu/population-mental-health) | Cox models on MIDUS and NHANES, including a correction to a hazard ratio I first reported wrong. |
| [ews-mood](https://github.com/abhaymettu/ews-mood) | Critical-slowing-down indicators for mood transitions. A nominally 5% test rejected 28 to 43% under the null. |

### Engineering and tools

| | |
|---|---|
| [paper-lecture](https://github.com/abhaymettu/paper-lecture) | Turns a paper PDF into a narrated lecture and an Anki deck. Local TTS, no API keys. |
| [scaffold](https://github.com/abhaymettu/scaffold) | External executive function: an Obsidian second brain and a Telegram bot that nudges on a 30-minute cadence. |

Analyst and research roles where the job is to build the number and then find
out whether it holds. Washington State, Chicago, Boston or Madison WI, and I
will move.
[abhaymettu.com](https://www.abhaymettu.com) · abhaymettu12@gmail.com
