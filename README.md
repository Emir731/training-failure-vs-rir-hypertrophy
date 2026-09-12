Training to Failure vs. Repetitions-in-Reserve: Effects on Muscle Hypertrophy in Resistance-Trained Individuals

Systematic Review & Exploratory Quantitative Synthesis



ðŸš§ Status: In progress â€” initial quantitative synthesis completed from 3 studies; citation verification, full-text retrieval, risk-of-bias assessment, and additional data extraction are ongoing.



Overview

This repository documents an ongoing systematic review investigating whether resistance-training sets performed to momentary muscular failure produce greater muscle hypertrophy than sets terminated with repetitions in reserve (RIR).


The primary research question is:



Does training to momentary muscular failure produce greater muscle hypertrophy than stopping sets before failure?



This is an established question in exercise science and has been examined in multiple randomized and within-subject trials, as well as several systematic reviews and meta-analyses.


Relevant published reviews include work by Grgic et al. (2021/2022), Vieira et al. (2021), Refalo et al. (2023), and Robinson et al. (2024).


Rather than attempting to reproduce these large-scale meta-analyses, this project aims to:



identify and verify relevant primary studies;

organize study-level hypertrophy data;

examine failure versus non-failure/RIR outcomes;

investigate training status as a potential moderator;

maintain a transparent, reproducible extraction dataset; and

determine whether sufficient data are available for a formal meta-analysis.


Research Question

Primary Question

Among adults performing resistance training, does training to momentary muscular failure produce greater muscle hypertrophy than training performed short of failure?


Secondary Question

Does participant training status influence the relationship between proximity to failure and muscle hypertrophy?


Methodology

Databases

The current literature search uses:



PubMed

Google Scholar


Additional databases may be added as the review develops.


Planned Inclusion Criteria

Studies are considered potentially eligible when they:



compare resistance training to momentary failure with non-failure/RIR training;

use a randomized or within-subject experimental design;

include healthy adult participants;

have an intervention duration of at least 6 weeks; and

report at least one measurable muscle-hypertrophy outcome.


Eligible hypertrophy outcomes include measures such as:



muscle cross-sectional area (CSA);

muscle thickness;

ultrasound-derived muscle measurements; or

other validated measures of skeletal-muscle hypertrophy.


Studies measuring only strength, power, hormonal responses, or other non-hypertrophy outcomes are excluded from the hypertrophy synthesis.


Planned Risk-of-Bias / Quality Assessment

The planned methodological-quality assessment includes:



TESTEX (Smart et al., 2015)

and/or a modified Downs-and-Black checklist


The final assessment procedure will be documented before the quality assessment is completed.


Study Identification and Verification

A major part of the current project has been citation and outcome verification.


A study being related to resistance training or training to failure is not sufficient for inclusion. The study must also provide a qualifying muscle-hypertrophy outcome.


Several candidate studies were confirmed as genuine peer-reviewed research but did not measure muscle hypertrophy.


Excluded â€” No Hypertrophy Outcome

The following studies are currently excluded because they do not provide a qualifying hypertrophy outcome:



Drinkwater et al. (2005) â€” strength/power outcomes only

Folland et al. (2002) â€” strength outcomes

Izquierdo et al. (2006) â€” strength, power, and hormonal outcomes

Rooney et al. (1994) â€” likely strength-only; final verification pending


These studies are not included in the hypertrophy synthesis.


Full Numeric Data Extracted

The following studies currently provide usable per-condition hypertrophy data.


Lasevicius et al. (2019)

Four resistance-training groups were compared across high- and low-load conditions.


Reported quadriceps CSA changes:



High-load failure: +8.1%

High-load non-failure: +7.7%

Low-load failure: +7.8%

Low-load non-failure: +2.8%


The population consisted of physically active but untrained men, meaning it does not strictly match the "resistance-trained" population specified in the project title.


Martorelli et al. (2017)

Young active women performed resistance training with repetitions to failure or non-failure protocols.


Reported muscle-thickness changes at 10 weeks:



Failure: +17.5%

Non-failure, equal-volume: +8.5%

Non-failure: +2.1%


The population was not specifically resistance-trained.


Santanielo et al. (2020)

This study is particularly relevant to the intended population because it examined resistance-trained individuals.


Reported vastus-lateralis CSA changes at 10 weeks:



Failure: +13.5%

Non-failure: +18.1%


Both conditions significantly increased hypertrophy, with no statistically significant difference between conditions.


Partial Data

NÃ³brega et al. (2018)

The study reported hypertrophy outcomes for four experimental conditions.


The available abstract reports:



approximately 3.0â€“4.6% CSA increase at 6 weeks

approximately 6.1â€“7.5% CSA increase at 12 weeks


No significant differences were detected between protocols.


However, the available information provides a range across the four groups rather than exact per-group values.


Therefore, this study is currently discussed narratively rather than included in the quantitative synthesis.


Sampson et al. (2016)

The study reported an overall CSA increase of approximately 11.4% across all groups, with no detected between-group differences.


However, the available abstract does not provide exact per-group hypertrophy changes.


Therefore, it is not currently possible to calculate a precise failure-versus-non-failure difference from the available data.


On-Topic but Currently Missing Usable Numbers

Lacerda et al. (2020)

This study directly investigated failure versus non-failure resistance training and measured quadriceps hypertrophy.


The available abstract reports that the conditions were similarly effective on average and discusses substantial individual variability.


However, the abstract does not provide the exact group-level hypertrophy values required for the current quantitative synthesis.


Next step: obtain the full text/results tables and extract the relevant numerical data.


Studies Requiring Verification

The following citations require additional verification or clarification:



Karsten et al. (2021) â€” citation appears to correspond to a supplement/conference format; full study status needs confirmation.

Kramer et al. (1997) â€” hypertrophy outcome not yet confirmed.

Pareja-Blanco et al. (2017) â€” exact paper/citation needs clarification.

Bergamasco et al. (2020) â€” not located under the current citation.

Held et al. (2021) â€” not located under the current citation.

Sanborn et al. (2000) â€” not located under the current citation.

Vieira et al. (2019) â€” not located under the current citation.

Terada et al. â€” publication year discrepancy requires resolution.


The extraction table explicitly records unresolved citations rather than treating them as confirmed evidence.


Scope Decision: Training Status

The original concept of the project was to focus specifically on resistance-trained individuals.


However, restricting inclusion exclusively to resistance-trained participants would currently leave only one study with usable numerical data:



Santanielo et al. (2020), n = 14



This would not provide enough evidence for a meaningful synthesis.


Therefore, the current review retains studies across different training statuses and treats training status as a subgroup/moderator variable.


Training status is explicitly recorded in:


data/extraction_table.csv

This distinction is important because most of the currently usable numerical evidence comes from populations that are not strictly resistance-trained.


The project therefore does not assume that results from untrained participants are equivalent to results from resistance-trained individuals.


Quantitative Synthesis

The current exploratory synthesis is generated by:


analysis/synthesis.py

Four comparisons from three studies currently have sufficient per-condition percentage-change data.


Study	Population	Failure	Non-failure	Difference
Lasevicius et al. (2019), high-load	Untrained men	+8.1%	+7.7%	+0.4 pp
Lasevicius et al. (2019), low-load	Untrained men	+7.8%	+2.8%	+5.0 pp
Martorelli et al. (2017)	Untrained women	+17.5%	+8.5%	+9.0 pp
Santanielo et al. (2020)	Resistance-trained	+13.5%	+18.1%	âˆ’4.6 pp

Where:



Difference = failure % change âˆ’ non-failure % change



Preliminary Summary

Unweighted Mean

+2.45 percentage points


Sample-Size-Weighted Mean

+5.45 percentage points


The observed direction is inconsistent across comparisons.


The study-level differences range from:



âˆ’4.6 to +9.0 percentage points



Notably, the currently available resistance-trained study favors the non-failure condition numerically, although it reported no statistically significant difference between conditions.


Given the very small number of comparisons, these values should be interpreted as descriptive exploratory results rather than evidence of a definitive pooled effect.


The preliminary pattern is broadly compatible with larger published reviews suggesting that training to momentary failure does not produce a robust or consistent hypertrophy advantage over training close to failure.


Statistical Limitations

The current analysis is not a formal meta-analysis.


The calculation uses differences in reported percentage change because sufficient data for a conventional effect-size meta-analysis are not currently available for all studies.


The current dataset does not consistently contain:



raw per-arm means;

standard deviations;

change-score standard deviations;

standard errors; and

complete exact per-arm sample sizes.


Therefore, the current analysis does not perform:



inverse-variance weighting;

standardized mean-difference calculations;

random-effects modeling;

heterogeneity estimation;

confidence intervals around a pooled effect; or

formal statistical tests of the pooled effect.


The sample-size-weighted value is therefore not equivalent to a conventional meta-analytic pooled estimate.


If sufficient full-text data become available, a formal meta-analysis will be considered.


The current work should therefore be described as:



A small-scale exploratory quantitative synthesis of newly collated data.



It should not be presented as a publication-grade meta-analysis comparable to larger systematic reviews such as Refalo et al. (2023).


Figure

The current visual summary is located at:


figures/effect_sizes.png

It is generated by:


analysis/synthesis.py

Run:


python analysis/synthesis.py

to reproduce the numerical output and figure.


Reproducibility

The project is structured so that the current quantitative results can be traced from extracted study data to the analysis script.


Current workflow:


Literature search
       â†“
Study identification
       â†“
Citation verification
       â†“
Eligibility assessment
       â†“
Data extraction
       â†“
data/extraction_table.csv
       â†“
analysis/synthesis.py
       â†“
Quantitative synthesis
       â†“
figures/effect_sizes.png

The extraction table contains the source and verification status for the study-level information used in the analysis.


The analysis script contains the explicit numerical values used in the current synthesis and calculates the study-level differences programmatically.


No numerical values are intentionally estimated to fill missing information.


Fields that have not been verified are marked accordingly in the extraction dataset.


Data

The main extraction dataset is:


data/extraction_table.csv

It currently records:



study identifier;

citation;

DOI/PMID where available;

study design;

sample size;

population;

intervention duration;

groups compared;

hypertrophy outcome;

quantitative results;

verification status; and

notes regarding unresolved questions or limitations.


The dataset is a work in progress and will be updated as additional studies are verified.


AI-Assisted Research Process

AI-assisted tools were used during parts of the literature-search, citation-verification, and data-organization process.


AI assistance was used to help with:



literature discovery;

citation organization;

initial data organization; and

identifying potentially relevant studies.


However:


All inclusion/exclusion decisions, interpretation, and final review of the extracted information are performed and confirmed by the author.


AI-generated information is not treated as primary evidence.


Quantitative claims are checked against the underlying published literature, and information that has not yet been verified is explicitly marked as such rather than being presented as confirmed data.


Current Limitations

The project currently has several important limitations:



Only a small number of studies have usable per-condition numerical data.

Several citations remain unresolved.

Some studies are currently available only through abstracts.

Some studies report pooled or range-based results rather than per-arm values.

Full-text verification is incomplete for some studies.

Risk-of-bias assessment has not yet been completed.

The current synthesis is not an inverse-variance-weighted meta-analysis.

Participant training status varies substantially between studies.

The current quantitative dataset is too small to support strong conclusions.

The literature search and screening process is still ongoing.


These limitations are reported explicitly rather than hidden because transparent reporting of uncertainty is essential to a reproducible research process.


Next Steps

1. Resolve Remaining Citations

Verify:



Bergamasco et al.

Held et al.

Sanborn et al.

Vieira et al.

Terada et al.

Karsten et al.

Kramer et al.

Pareja-Blanco et al.


2. Obtain Full Text

Retrieve the full text/results tables for studies where the abstract does not provide sufficient numerical data, particularly:



Lacerda et al. (2020)

NÃ³brega et al. (2018)

Sampson et al. (2016)


3. Risk-of-Bias Assessment

Complete the planned TESTEX and/or Downs-and-Black assessment.


4. Expand the Quantitative Dataset

Add additional study-level comparisons when complete means, SDs, and sample sizes become available.


5. Conduct a Formal Meta-Analysis

If sufficient data become available, consider:



standardized effect-size calculation;

inverse-variance weighting;

random-effects modeling;

95% confidence intervals;

heterogeneity statistics;

sensitivity analyses; and

subgroup/moderator analysis based on training status.


6. PRISMA Documentation

Add:



PRISMA flow diagram;

complete database search strategy;

search dates;

screening log; and

detailed exclusion reasons.


7. Final Manuscript

Develop the completed review into a short research paper/manuscript.


Repository Structure

training-failure-vs-rir-hypertrophy/
â”‚
â”œâ”€â”€ README.md
â”‚
â”œâ”€â”€ data/
â”‚   â””â”€â”€ extraction_table.csv
â”‚
â”œâ”€â”€ analysis/
â”‚   â””â”€â”€ synthesis.py
â”‚
â””â”€â”€ figures/
    â””â”€â”€ effect_sizes.png

Author

Sanjar Osmanov


Independent student research project in exercise science.


The project uses AI-assisted tools for parts of the literature-search and data-organization process. Final study verification, inclusion/exclusion decisions, analysis decisions, and interpretation are the responsibility of the author.



Project Status

ðŸš§ Active research project


The dataset and analysis are expected to change as additional studies are verified and full-text data become available.


Last updated: September 2026

