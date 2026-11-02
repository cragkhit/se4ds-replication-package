# Theme Review Log

This file records the review of the code-to-theme mapping from the preliminary interview study (Section 3.2.1 of the paper).

## Process

1. The first author built the themes from the consensus codes that were applied at least once (78 codes, 100 mentions). The top-level categories of the codebook gave a first grouping, which was then revised code by code through iterative sorting, splitting, and merging.
2. The second author reviewed the themes and the assignment of every code to a theme. The review was added during the first revision of the paper; in the original submission, the first author built the themes alone.
3. The two authors discussed every disagreement. The first author accepted all of the second author's suggestions.

Files:

- `code_to_theme_mapping_suggestion.csv.xlsx`: the mapping with the second author's suggestions and his notes on the changes (column "Notes on changes").
- `code_to_theme_mapping.csv`: the final mapping after the review, used in Table 3 of the paper and in Supplement S1.

## Changes made during the review

### 1. Theme 3b split into 3b and 3c

| Before | After |
|---|---|
| 3b: Requirements, communication & maintainability (7 codes, 7 mentions) | 3b: Requirements and communication (4 codes, 4 mentions) |
| | 3c: Maintainability and analytic engineering practice (3 codes, 3 mentions) |

Codes in the new 3c: No documentation, Analytic engineering, DBT.

**Reason:** Requirements and communication problems come before the product is built. Once the product is built, these problems should already be solved, and maintainability problems arise instead. This follows the order of the DS and SE life cycle, which also separates data preparation, modeling, and evaluation.

### 2. Dream tools moved from Theme 6 to Theme 5

| Before | After |
|---|---|
| Theme 5: Future / desired SE practices (4 codes, 4 mentions), no sub-themes | Theme 5: Future (12 codes, 13 mentions) |
| | 5a: Desired SE practices (4 codes, 4 mentions) |
| 6e: Dream tools (automation, monitoring & integration) (8 codes, 9 mentions) | 5b: Dream tools (automation, monitoring & integration) (8 codes, 9 mentions) |

**Reason:** Dream tools do not exist yet. They are what participants wish for, not tools they use, so they belong with the other wishes for the future rather than with the tools in use.

### 3. Theme 6 renamed

| Before | After |
|---|---|
| Theme 6: Tools: usage, challenges & dream tools (39 codes, 51 mentions; RQ3, RQ4) | Theme 6: Tools: usage and challenges (31 codes, 42 mentions; RQ1, RQ3) |

**Reason:** Follows from change 2. Without the dream tools, Theme 6 covers only the tools in use and their challenges. Sub-themes 6a to 6d are unchanged. Theme 6 no longer motivates RQ4, and it motivates RQ1 (the DS tools in use) as well as RQ3 (the SE tools).

## Unchanged

Themes 1, 2, and 4 and their sub-themes, the assignment of every other code, and the totals (78 codes, 100 mentions).
