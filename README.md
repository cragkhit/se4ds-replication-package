# Replication Package

**Paper:** *Software Engineering Practices in Data Science Projects: Adoption Patterns, Challenges, and Gaps from the Practitioner's Perspective*

This package contains the survey data, coded interview material, analysis notebooks, and helper scripts needed to reproduce every quantitative and figure-based result reported in the paper.

## Contents

```
replication-package/
├── README.md                                         (this file)
├── LICENSE                                           (MIT, for code)
├── LICENSE-DATA                                      (CC BY 4.0, for data)
├── CITATION.cff                                      (machine-readable citation)
├── requirements.txt                                  (Python dependencies)
├── analysis_utils.py                                 (shared helpers used by all RQ notebooks)
├── analysis_demographic.ipynb                        (sample demographics, Table 4-8 area)
├── analysis_preliminary_study.ipynb                  (interview thematic counts, Appendix B)
├── analysis_preliminary_study_kappa.ipynb            (inter-coder reliability, Cohen's kappa)
├── analysis_rq1.ipynb                                (RQ1: framework, phase, tool adoption)
├── analysis_rq2.ipynb                                (RQ2: DS and SE challenges)
├── analysis_rq3.ipynb                                (RQ3: SE tool and practice adoption)
├── analysis_rq4.ipynb                                (RQ4: planned adoption and dream tools)
├── se4ds-cleaned-30bccbed-filtered.csv               (main survey dataset, N=112)
├── coding_results.xlsx                               (preliminary-study coded interviews, 12 participants)
├── data_science_dream_tools_thematic_analysis.csv    (manual thematic coding behind Appendix C)
├── dream_tool_responses.csv                          (cached export of open-ended dream-tool answers)
└── future_se_methods.csv                             (cached export of open-ended future-SE answers)
```

## Datasets

### `se4ds-cleaned-30bccbed-filtered.csv` (N = 112)
The main survey dataset. Each row is one anonymous practitioner response. The CSV has a two-level header: the first row holds question text, the second holds a sub-key (option label or scale anchor). `analysis_utils.load_data()` flattens this into single-level column names, drops the duplicate sub-header row, maps Thai Likert labels to numeric scores, and constructs derived helper columns (`role`, `ds_exp`, `se_exp`, `*_curr`, `*_plan`, `*_past`, `*_used`, `*_num`, `adoption_score`).

Data collection ran from 27 September 2023 to 17 June 2024. 117 raw responses were collected; 5 duplicates were removed during cleaning, leaving 112 valid responses. The survey was administered in Thai and English; Thai Likert anchors are preserved in the CSV and converted by the loader.

**Privacy.** The published CSV has been scrubbed: the SurveyMonkey-supplied `ip_address` and `email_address` columns were removed before release (the email column was already empty). The remaining metadata columns (`source`, `respondent_id`, `collector_id`, `start_date`, `end_date`) hold SurveyMonkey-internal identifiers and timestamps and contain no externally meaningful PII. No names, contact details, or free-text fields that could re-identify a respondent are included.

### `coding_results.xlsx`
The reflexive thematic coding sheet from the preliminary interview study (12 DS practitioners). The notebook `analysis_preliminary_study.ipynb` reads the `All-Sum` sheet and produces the per-theme code counts in Appendix B. `analysis_preliminary_study_kappa.ipynb` recomputes Cohen's kappa for inter-coder agreement.

### `data_science_dream_tools_thematic_analysis.csv`
The exact-text dream-tool responses with their manually assigned themes. This is the source data behind the categorization in Appendix C.

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
| `analysis_demographic.ipynb`              | (demographics) | Sample summary: counts and percentages by role, education, DS/SE experience, organization type and size. Generates `ds-se-counts-heatmap.pdf` and the framework awareness/used pie charts. |
| `analysis_preliminary_study.ipynb`        | Preliminary study  | Per-theme code counts from the 12 interviews; produces the thematic-map and the consolidated table behind Appendix B.                                                                       |
| `analysis_preliminary_study_kappa.ipynb`  | Preliminary study  | Cohen's kappa between the two interview coders, per question and overall.                                                                                                                  |
| `analysis_rq1.ipynb`                      | RQ1     | DS framework awareness and adoption (Microsoft TDSP, CRISP-DM, others); CRISP-DM phase frequencies (Figure: `phase_frequencies_violin.pdf`); phase-frequency correlations; per-role phase frequencies; Kruskal-Wallis H and Dunn's post-hoc tests; tool-usage figure (`tool-usage-diverging.pdf`). |
| `analysis_rq2.ipynb`                      | RQ2     | DS-process challenge severity ranking, SE challenge frequencies (`fig_se_challenge_pct.pdf`), role-based Kruskal-Wallis tests, Spearman correlations with experience, SE-challenge co-occurrence matrix. |
| `analysis_rq3.ipynb`                      | RQ3     | SE-tool category usefulness ratings; current SE-practice adoption per item; bimodal adoption-score distribution (`fig_adoption_score_hist.pdf`); Spearman correlations with DS and SE experience; Kruskal-Wallis across roles and framework knowledge. |
| `analysis_rq4.ipynb`                      | RQ4     | Planned SE-practice adoption ranking; open-ended future-SE-methods exports (`future_se_methods.csv`); open-ended dream-tool exports (`dream_tool_responses.csv`).                            |

### 4. Expected outputs

Running all notebooks end-to-end regenerates every figure and statistical result quoted in the paper. The PDF figures land in the notebook's working directory; you can move them to the LaTeX source folder if you also want to recompile the paper. Statistical numbers (means, medians, H statistics, p-values, Spearman rho, etc.) are printed in the notebook output cells.

### 5. Tips and troubleshooting

- **Loader path resolution.** `analysis_utils.load_data()` searches for `se4ds-cleaned-30bccbed-filtered.csv` in (a) the same directory as `analysis_utils.py`, (b) an `uploads/` subdirectory, and (c) the current working directory. Keeping every file in this single folder is the most robust setup.
- **Thai locale fonts.** A few cells render Thai survey labels. If matplotlib falls back to a glyph-less font, install a Thai-capable font such as `fonts-thai-tlwg` (Debian/Ubuntu) or `tlwg` via Homebrew on macOS, then add `plt.rcParams['font.family'] = 'TH Sarabun New'` (or another installed Thai font) in the cell that errors.
- **Kappa notebook prerequisites.** `analysis_preliminary_study_kappa.ipynb` additionally depends on `scikit-learn`, which is pinned in `requirements.txt`.
- **Reproducibility.** No notebook calls any random-number generator, so reruns produce bit-identical numeric output for a given pandas / numpy version pair. Figure-level differences (e.g., DPI, font kerning) may appear depending on the matplotlib backend.

## License

- **Code** (notebooks, `analysis_utils.py`): MIT License, see `LICENSE`.
- **Data** (CSV, XLSX, and any aggregated derivatives): Creative Commons Attribution 4.0 International (CC BY 4.0), see `LICENSE-DATA`.

## Contact

Please direct questions, bug reports, or replication issues to the corresponding author listed in the paper.
