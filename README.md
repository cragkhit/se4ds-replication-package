# Replication Package

**Paper:** *Software Engineering Practices in Data Science Projects: Adoption Patterns, Challenges, and Gaps from the Practitioner's Perspective*

This package contains the survey data, coded interview material, analysis notebooks, and helper scripts needed to reproduce every quantitative and figure-based result reported in the paper.

## Contents

```
replication-package/
├── README.md                                         (this file)
├── LICENSE                                           (MIT, for code)
├── LICENSE-DATA                                      (CC BY 4.0, for data)
├── requirements.txt                                  (Python dependencies)
├── analysis_utils.py                                 (shared helpers used by all RQ notebooks)
├── analysis_demographic.ipynb                        (sample demographics, Table 4-8 area)
├── analysis_preliminary_study.ipynb                  (interview thematic counts, Supplement S1)
├── analysis_preliminary_study_kappa.ipynb            (inter-coder reliability, Cohen's kappa)
├── analysis_rq1.ipynb                                (RQ1: framework, phase, tool adoption)
├── analysis_rq2.ipynb                                (RQ2: DS and SE challenges)
├── analysis_rq3.ipynb                                (RQ3: SE tool and practice adoption)
├── analysis_rq4.ipynb                                (RQ4: planned adoption and dream tools)
├── analysis_multiple_comparisons.ipynb               (all 42 hypothesis tests with Benjamini-Hochberg q-values)
├── multiple_comparisons.csv                          (output of the notebook above: test, statistic, p, q, verdict)
├── online_questionnaire.pdf                          (the full survey instrument as administered, 29 pages)
├── supplementary_material.pdf                        (Supplements S1–S3: code-to-theme mapping, dream-tool categorization, codebooks)
├── supplementary_material.tex                        (LaTeX source of the supplementary material)
├── code_to_theme_mapping.csv                         (machine-readable version of Supplement S1)
├── code_to_theme_mapping_suggestion.csv.xlsx         (second author's review of the mapping, with notes)
├── code_to_theme_mapping_log.md                      (changes made in the theme review and their reasons)
├── codebook.csv                                      (machine-readable version of Supplement S3)
├── se4ds-cleaned-30bccbed-filtered.csv               (main survey dataset, N=112)
├── coding_results.xlsx                               (preliminary-study coded interviews, 12 participants)
├── data_science_dream_tools_thematic_analysis.csv    (manual thematic coding behind Supplement S2)
├── dream_tool_responses.csv                          (cached export of open-ended dream-tool answers)
├── future_se_methods.csv                             (cached export of open-ended future-SE answers)
└── figures/                                          (all figures written by the notebooks; see "Expected outputs")
```

## Survey instrument

### `online_questionnaire.pdf`
A PDF export of the full online questionnaire as administered to participants, covering all six survey parts (consent, demographics, DS framework awareness and adoption, DS-process phase frequency and challenge frequency, SE challenges, SE tool adoption and usefulness, and SE practice adoption and future aspirations). The PDF preserves the exact question wording, answer options, Likert anchors, and skip logic that respondents saw, and matches the survey structure summarized in Table 1 of the paper (referenced in Appendix A). Use this file as the authoritative reference for how each column in `se4ds-cleaned-30bccbed-filtered.csv` was elicited.

## Supplementary material

### `supplementary_material.pdf` (source: `supplementary_material.tex`)
Three supplements that the paper points to. **Supplement S1** lists the full code-to-theme mapping from the thematic analysis of the 12 semi-structured interviews (78 codes, 100 mentions), organized by theme and sub-theme. **Supplement S2** lists the 55 substantive dream-tool responses (translated into English where the original was in Thai) with their assigned categories. **Supplement S3** lists the initial (154 codes in 12 top-level categories) and final (224 entries) codebooks of the interview coding, exported from NVivo.

### `code_to_theme_mapping.csv`
A machine-readable version of Supplement S1 with columns `theme`, `sub_theme`, `code`, and `mentions`.

### `code_to_theme_mapping_log.md` and `code_to_theme_mapping_suggestion.csv.xlsx`
The second author reviewed the themes and the assignment of every code. The spreadsheet holds the suggested mapping with the reviewer's notes. The log describes the review and each change to the themes, with its reason.

### `codebook.csv`
A machine-readable version of Supplement S3: one row per entry of the final codebook, in NVivo order, with columns `level` (0 = top-level category), `name`, `kind` (`category` or `code`), `in_initial_codebook` (whether the entry was already in the initial codebook), and `path`.

## Datasets

### `se4ds-cleaned-30bccbed-filtered.csv` (N = 112)
The main survey dataset. Each row is one anonymous practitioner response. The CSV has a two-level header: the first row holds question text, the second holds a sub-key (option label or scale anchor). `analysis_utils.load_data()` flattens this into single-level column names, drops the duplicate sub-header row, maps Thai Likert labels to numeric scores, and constructs derived helper columns (`role`, `ds_exp`, `se_exp`, `*_curr`, `*_plan`, `*_past`, `*_used`, `*_num`, `adoption_score`, `reached_part3`, `answered_practices`).

**Reporting base.** All percentages use the 112 respondents as the base, and a blank in a multiple-select or practice item counts as "not selected / not used / not current". Ratings of phases and DS-process challenges cover the respondents who answered each item (n = 84–87). 25 respondents submitted the questionnaire without answering any item in Parts 3–6. `load_data()` marks this with two boolean columns: `reached_part3` (the 87 respondents who answered at least one CRISP-DM phase item) and `answered_practices` (the 68 respondents who answered at least one SE-practice row). `analysis_rq3.ipynb` (section 3b) repeats the adoption-score summary on the 68 who answered the practice question as a robustness check.

Data collection ran from 27 September 2023 to 17 June 2024. 117 raw responses were collected; 5 duplicates were removed during cleaning, leaving 112 valid responses. The survey was administered in Thai and English; Thai Likert anchors are preserved in the CSV and converted by the loader.

**Privacy.** The published CSV has been scrubbed: the SurveyMonkey-supplied `ip_address` and `email_address` columns were removed before release (the email column was already empty). The remaining metadata columns (`source`, `respondent_id`, `collector_id`, `start_date`, `end_date`) hold SurveyMonkey-internal identifiers and timestamps and contain no externally meaningful PII. No names, contact details, or free-text fields that could re-identify a respondent are included.

### `coding_results.xlsx`
The thematic coding sheet from the preliminary interview study (12 DS practitioners). The notebook `analysis_preliminary_study.ipynb` reads the `All-Sum` sheet and produces the per-theme code counts in Supplement S1 of `supplementary_material.pdf`. `analysis_preliminary_study_kappa.ipynb` recomputes Cohen's kappa for inter-coder agreement.

### `data_science_dream_tools_thematic_analysis.csv`
The exact-text dream-tool responses with their manually assigned themes. This is the source data behind the categorization in Supplement S2 of `supplementary_material.pdf`.

### `multiple_comparisons.csv`
One row per hypothesis test reported in the paper (42 rows): section, test, variables, n, statistic, raw p, Benjamini-Hochberg q, and verdict (significant / exploratory / not significant). Produced by `analysis_multiple_comparisons.ipynb`.

### `dream_tool_responses.csv` and `future_se_methods.csv`
Cached exports of two open-ended survey questions, produced by `analysis_rq4.ipynb`. They are included so reviewers can inspect the raw responses without re-running the notebook.

## How to run the analysis

### 1. Set up the Python environment

We recommend Python 3.10 or newer in a clean virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Launch Jupyter

```bash
jupyter lab        # or: jupyter notebook
```

Open any of the analysis notebooks in this folder. All notebooks expect the data files to sit in the same directory and are otherwise self-contained. To rerun a notebook from a clean state, use *Kernel → Restart & Run All*.

### 3. Mapping notebooks to paper sections

| Notebook                                  | RQ      | What it produces                                                                                                                                                                            |
|-------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `analysis_demographic.ipynb`              | (demographics) | Sample summary: counts and percentages by role, education, DS/SE experience, organization type and size; Kendall's τ_b between DS and SE experience. Generates `figures/ds-se-counts-heatmap.pdf` and the framework awareness/used pie charts. |
| `analysis_preliminary_study.ipynb`        | Preliminary study  | Per-theme code counts from the 12 interviews; produces the thematic-map and the consolidated table behind Supplement S1.                                                                       |
| `analysis_preliminary_study_kappa.ipynb`  | Preliminary study  | Cohen's kappa between the two interview coders, per question and overall.                                                                                                                  |
| `analysis_rq1.ipynb`                      | RQ1     | DS framework awareness and adoption (Microsoft TDSP, CRISP-DM, others); CRISP-DM phase frequencies (`figures/phase_frequencies_violin.pdf`); phase-frequency correlations; per-role phase frequencies (`figures/phase_frequencies_by_role_violin.pdf`); Kruskal-Wallis H and Dunn's post-hoc tests; tool-usage figure (`figures/tool-usage-diverging.pdf`). |
| `analysis_rq2.ipynb`                      | RQ2     | DS-process challenge frequency ranking, SE challenge frequencies (`figures/fig_se_challenge_pct.pdf`), role-based Kruskal-Wallis tests, Spearman correlations with experience, SE-challenge co-occurrence matrix. |
| `analysis_rq3.ipynb`                      | RQ3     | SE-tool category adoption and usefulness ratings; current SE-practice adoption per item and per type of practice (section 2b); SE adoption-score distribution (`figures/fig_adoption_score_hist.pdf`), with a robustness check over the 68 who answered the practice question (section 3b); Spearman correlations with DS and SE experience; Kruskal-Wallis across roles, organization type and framework knowledge. |
| `analysis_rq4.ipynb`                      | RQ4     | Planned SE-practice adoption ranking; open-ended future-SE-methods exports (`future_se_methods.csv`); open-ended dream-tool exports (`dream_tool_responses.csv`).                            |
| `analysis_multiple_comparisons.ipynb`    | §3.5, RQ1–RQ3 | Recomputes all 42 hypothesis tests reported in the paper and controls the false discovery rate over the whole family (Benjamini-Hochberg); writes `multiple_comparisons.csv`. A result is significant only if q < 0.05, exploratory if p < 0.05 but q ≥ 0.05. |

### 4. Expected outputs

Running all notebooks end-to-end regenerates every figure and statistical result quoted in the paper. All figures are written to the `figures/` subfolder of this package (it is created if missing); copy them to the LaTeX source folder if you also want to recompile the paper. Statistical numbers (means, medians, H statistics, p-values, Spearman rho, etc.) are printed in the notebook output cells.

### 5. Tips and troubleshooting

- **Loader path resolution.** `analysis_utils.load_data()` searches for `se4ds-cleaned-30bccbed-filtered.csv` in (a) the same directory as `analysis_utils.py`, (b) an `uploads/` subdirectory, and (c) the current working directory. Keeping every file in this single folder is the most robust setup.
- **Thai locale fonts.** A few cells render Thai survey labels. If matplotlib falls back to a glyph-less font, install a Thai-capable font such as `fonts-thai-tlwg` (Debian/Ubuntu) or `tlwg` via Homebrew on macOS, then add `plt.rcParams['font.family'] = 'TH Sarabun New'` (or another installed Thai font) in the cell that errors.
- **Kappa notebook prerequisites.** `analysis_preliminary_study_kappa.ipynb` additionally depends on `scikit-learn`, which is pinned in `requirements.txt`.
- **Reproducibility.** No notebook calls any random-number generator, so reruns produce bit-identical numeric output for a given pandas / numpy version pair. Figure-level differences (e.g., DPI, font kerning) may appear depending on the matplotlib backend.

## Citing this replication package

If you use this package, please cite the paper and this archive. Once archived on Zenodo, the package will receive a permanent DOI; please cite that DOI for any subsequent use.

## License

- **Code** (notebooks, `analysis_utils.py`): MIT License, see `LICENSE`.
- **Data** (CSV, XLSX, and any aggregated derivatives): Creative Commons Attribution 4.0 International (CC BY 4.0), see `LICENSE-DATA`.

## Contact

Please direct questions, bug reports, or replication issues to the corresponding author listed in the paper.
