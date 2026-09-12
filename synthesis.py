"""
Simplified quantitative synthesis: resistance training to failure vs.
non-failure/RIR, effect on muscle hypertrophy.

METHODOLOGICAL NOTE (read before citing this analysis anywhere):
This is a SIMPLIFIED synthesis, not a full inverse-variance-weighted
random-effects meta-analysis. A rigorous SMD-based meta-analysis would
require raw group means, SDs, and exact per-arm sample sizes, which are
not available from the published abstracts for these studies. What is
computed here is the difference in reported percentage hypertrophy
change between the failure and non-failure/RIR conditions of each
study, averaged both unweighted and weighted by approximate sample
size. This is transparent about what it is: a coarse, real-data-only
synthesis suitable for an exploratory student project, not a
publication-grade meta-analysis.

Two studies with usable hypertrophy data (Nobrega et al. 2018, Sampson
et al. 2016) are EXCLUDED from this quantitative synthesis because
their abstracts report only a pooled/range result across all study
arms, not a per-arm breakdown - there is nothing to compute a
failure-vs-non-failure difference from. They are discussed narratively
in the README instead.

Every number below is sourced from data/extraction_table.csv, which
lists where it was found. Nothing here is estimated or invented.
"""

import matplotlib.pyplot as plt

# Real data extracted from published abstracts/open-access full text.
# See data/extraction_table.csv for exact source (DOI/PMID) of every number.
comparisons = [
    {
        "study": "Lasevicius et al. 2019 (High-load)",
        "population": "untrained men",
        "failure_pct": 8.1,
        "nonfailure_pct": 7.7,
        "n": 32,
    },
    {
        "study": "Lasevicius et al. 2019 (Low-load)",
        "population": "untrained men",
        "failure_pct": 7.8,
        "nonfailure_pct": 2.8,
        "n": 32,
    },
    {
        "study": "Martorelli et al. 2017 (RF vs. equal-volume RNFV)",
        "population": "untrained women",
        "failure_pct": 17.5,
        "nonfailure_pct": 8.5,
        "n": 89,
    },
    {
        "study": "Santanielo et al. 2020",
        "population": "resistance-trained individuals",
        "failure_pct": 13.5,
        "nonfailure_pct": 18.1,
        "n": 14,
    },
]

for c in comparisons:
    c["difference_pp"] = round(c["failure_pct"] - c["nonfailure_pct"], 1)

diffs = [c["difference_pp"] for c in comparisons]
simple_average = sum(diffs) / len(diffs)
weighted_average = sum(c["difference_pp"] * c["n"] for c in comparisons) / sum(
    c["n"] for c in comparisons
)

if __name__ == "__main__":
    print("Study-by-study difference (failure %change minus non-failure %change):")
    for c in comparisons:
        sign = "+" if c["difference_pp"] >= 0 else ""
        print(
            f"  {c['study']} [{c['population']}, n~{c['n']}]: "
            f"{sign}{c['difference_pp']} percentage points"
        )

    print(f"\nUnweighted average difference: {simple_average:+.2f} percentage points")
    print(f"Sample-size-weighted average:  {weighted_average:+.2f} percentage points")
    print(
        "\nInterpretation: differences range from about -4.6 to +9.0 percentage "
        "points across studies (i.e. the sign flips), and the pooled average is "
        "small. This is directionally consistent with the larger published "
        "meta-analyses (Grgic et al. 2021/22; Refalo et al. 2023), which also "
        "found no robust hypertrophy advantage for training to failure."
    )

    fig, ax = plt.subplots(figsize=(9, 4.5))
    studies = [c["study"] for c in comparisons]
    colors = ["#2b6cb0" if d >= 0 else "#c53030" for d in diffs]
    ax.barh(studies, diffs, color=colors)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Difference in % hypertrophy change (failure minus non-failure/RIR)")
    ax.set_title(
        "Training to Failure vs. Non-Failure/RIR: Hypertrophy Outcome by Study\n"
        "(simplified synthesis of real extracted data - see README for method & limits)"
    )
    plt.tight_layout()
    plt.savefig("../figures/effect_sizes.png", dpi=150)
    print("\nFigure saved to figures/effect_sizes.png")
