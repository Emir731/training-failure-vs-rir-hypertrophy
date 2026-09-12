# Training to Failure vs. Repetitions-in-Reserve: Effects on Muscle Hypertrophy in Resistance-Trained Individuals

**Status:** 🚧 In progress — first quantitative synthesis complete on 3 studies; several citations still need verification (see below)

## Overview

This repository documents an ongoing systematic review examining whether training sets to momentary muscular failure produces greater muscle hypertrophy than stopping sets with repetitions-in-reserve (RIR), specifically in resistance-trained individuals.

This is an active, well-studied question in exercise science. Several major meta-analyses already exist on this or closely related questions (Grgic et al., 2021/22, *J Sport Health Sci*; Vieira et al., 2021, *J Strength Cond Res*; Refalo et al., 2023, *Sports Med*; Robinson et al., 2024, *Sports Med*). This project aims to either (a) update the evidence base with studies published after the most recent major review, or (b) focus specifically on the resistance-trained subgroup, rather than duplicate existing work.

## Methodology (current state)

- **Databases:** PubMed, Google Scholar
- **Planned inclusion criteria:** randomized (or within-subject) trials comparing RT to failure vs. non-failure/RIR, ≥6 weeks duration, reporting a muscle hypertrophy outcome (CSA, muscle thickness, etc.), healthy adult participants
- **Planned quality/risk-of-bias tools:** TESTEX (Smart et al., 2015) and/or a modified Downs-and-Black checklist — both used in prior meta-analyses in this exact literature
- **Data extraction:** see `data/extraction_table.csv`

## Current status of the candidate studies

Verification turned up an important finding: being a real, peer-reviewed study on "training to failure" is **not** sufficient for inclusion — several candidate studies turned out to measure only strength/power/hormonal outcomes, with no muscle hypertrophy measure at all. These are excluded even though they are genuine studies.

- **Excluded — no hypertrophy outcome measured:** Drinkwater et al. 2005, Folland et al. 2002, Izquierdo et al. 2006 (confirmed via abstract/secondary source); Rooney et al. 1994 (likely, pending final check)
- **Full numeric data extracted (real, sourced numbers):** Lasevicius et al. 2019, Martorelli et al. 2017, Santanielo et al. 2020
- **Partial numeric data (pooled/range only, not per-arm):** Nóbrega et al. 2018 (range across 4 groups), Sampson et al. 2016 (pooled across 3 groups)
- **Confirmed on-topic, still no usable hypertrophy numbers:** Lacerda et al. 2020 (abstract reports only qualitative individual-variability findings, no group means/%)
- **Needs verification/clarification:** Karsten et al. 2021 (possibly a conference abstract, not a full study), Kramer et al. 1997, Pareja-Blanco et al. 2017 (exact paper unclear)
- **Not located under the given citation:** Bergamasco et al. 2020, Held et al. 2021, Sanborn et al. 2000, Vieira et al. 2019; Terada et al. has a year discrepancy (2020 vs. 2022)

## Scope decision: training status as a subgroup variable

Restricting to only resistance-trained participants would leave a single usable study (Santanielo et al., n=14) — not enough for any meaningful synthesis. Instead, following the approach used in existing published meta-analyses on this exact topic (e.g., Grgic et al. 2021/22), this review includes studies across training statuses and treats **training status as a subgroup/moderator variable** rather than a strict inclusion filter. Where a study's population doesn't match "resistance-trained," this is flagged explicitly in the data (see `Population` column).

## Quantitative synthesis (real data, simplified method)

`analysis/synthesis.py` computes the difference in reported hypertrophy % change between failure and non-failure/RIR conditions for the 4 comparisons (from 3 studies) where a per-arm breakdown is available:

| Study | Population | Failure % | Non-failure % | Difference (pp) |
|---|---|---|---|---|
| Lasevicius 2019 (high-load) | untrained men | +8.1% | +7.7% | +0.4 |
| Lasevicius 2019 (low-load) | untrained men | +7.8% | +2.8% | +5.0 |
| Martorelli 2017 (RF vs. RNFV) | untrained women | +17.5% | +8.5% | +9.0 |
| Santanielo 2020 | resistance-trained | +13.5% | +18.1% | -4.6 |

**Unweighted average: +2.45 percentage points. Sample-size-weighted average: +5.45 percentage points.** The sign flips across studies and the pooled effect is small — directionally consistent with the larger published meta-analyses (Grgic et al. 2021/22; Refalo et al. 2023), which likewise found no robust hypertrophy advantage for training to failure.

Nóbrega et al. 2018 and Sampson et al. 2016 have confirmed hypertrophy data but only as a pooled/range result across all arms (no per-arm breakdown in the abstract) — they are discussed narratively rather than included in the quantitative synthesis; both are directionally consistent (small, non-significant between-condition differences).

See `figures/effect_sizes.png` for the visual summary, and `analysis/synthesis.py` for the fully reproducible calculation — every number traces to a specific source in `data/extraction_table.csv`.

**Important limitation to state plainly in any write-up:** this is a simplified synthesis (difference in reported % change), not an inverse-variance-weighted random-effects meta-analysis — that would require raw means/SDs per arm, which aren't available from the abstracts alone. With only 3-4 comparisons and 2 studies contributing text-only support, this project's honest framing is "a small-scale exploratory synthesis of newly-collated data," not a comprehensive meta-analysis on par with Refalo et al. 2023.

See `data/extraction_table.csv` for the row-by-row status of every study, including exact citations, links, and open questions.

## Process note

Literature search, citation verification, and data organization for this project were conducted with AI-assisted tools (Claude, Anthropic), with all inclusion/exclusion judgment calls, interpretation, and final review performed and confirmed by the author. No data in this repository is fabricated or estimated — fields not yet verified from a primary source are explicitly marked `TBD` or `NOT CONFIRMED` rather than filled with placeholder numbers.

## Next steps

1. Resolve remaining unverified citations (Bergamasco, Held, Sanborn, Vieira, Terada) and unclear ones (Karsten, Kramer, Pareja-Blanco)
2. Get full text / results tables for Lacerda 2020 (no usable numbers yet) to add to the quantitative synthesis
3. Conduct risk-of-bias / quality assessment (TESTEX) on all included studies
4. Expand the synthesis as more studies resolve; consider a proper inverse-variance-weighted meta-analysis if raw means/SDs become available
5. Add a PRISMA flow diagram and full search log
6. Write up findings as a short paper

## Repository structure

```
├── README.md
├── data/
│   └── extraction_table.csv     # study-level extraction table (work in progress)
├── analysis/
│   └── synthesis.py             # reproducible calculation of the quantitative synthesis
└── figures/
    └── effect_sizes.png         # visual summary of the 4 study-level comparisons
```

## Author

[Your name] — systematic review conducted as an independent study project, with AI-assisted literature search and data organization tools.
