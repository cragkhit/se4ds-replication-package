"""
analysis_utils.py
-----------------
Shared constants and helper functions used across all RQ analysis scripts.

Paper: "Adoption of Software Engineering Practices in Data Science Projects:
        Practitioners' Perspective"
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# File path
# ---------------------------------------------------------------------------
# The script searches for the CSV in these locations (in order):
#   1. The same directory as this file
#   2. An 'uploads/' subfolder next to this file
#   3. The literal string below (override by setting DATA_PATH yourself)
import os as _os

# __file__ is not defined when running inside a Jupyter notebook,
# so we fall back to the current working directory in that case.
try:
    _HERE = _os.path.dirname(_os.path.abspath(__file__))
except NameError:
    _HERE = _os.getcwd()

_CANDIDATES = [
    _os.path.join(_HERE, 'se4ds-cleaned-30bccbed-filtered.csv'),
    _os.path.join(_HERE, 'uploads', 'se4ds-cleaned-30bccbed-filtered.csv'),
    'se4ds-cleaned-30bccbed-filtered.csv',  # fallback: cwd
]
DATA_PATH = next((p for p in _CANDIDATES if _os.path.isfile(p)), _CANDIDATES[0])

# ---------------------------------------------------------------------------
# Thai → English / numeric value mappings
# ---------------------------------------------------------------------------

# CRISP-DM phase frequency (0–5 scale)
FREQ_MAP = {
    '0 - ไม่ได้ทำเลย': 0,
    '1 - ทำน้อยที่สุด': 1,
    '2 - ทำน้อย': 2,
    '3 - ทำปานกลาง': 3,
    '4 - ทำบ่อย': 4,
    '5 - ทำบ่อยที่สุด': 5,
}

# DS-process challenge severity (0–5 scale)
CHALLENGE_MAP = {
    '0 - ไม่พบปัญหา': 0,
    '1 - พบปัญหาน้อยที่สุด': 1,
    '2 - พบปัญหาน้อย': 2,
    '3 - พบปัญหาปานกลาง': 3,
    '4 - พบปัญหาบ่อย': 4,
    '5 - พบปัญหาบ่อยมากที่สุด': 5,
}

# DS experience (ordinal)
DS_EXP_MAP = {
    'น้อยกว่า 1 ปี': 1,
    '1-5 ปี': 2,
    '6-10 ปี': 3,
    'มากกว่า 10 ปี': 4,
}

# SE experience (ordinal, includes "no experience")
SE_EXP_MAP = {
    'ไม่มีประสบการณ์': 0,
    'น้อยกว่า 1 ปี': 1,
    '1-5 ปี': 2,
    '6-10 ปี': 3,
    'มากกว่า 10 ปี': 4,
}

# Role (English labels)
ROLE_MAP = {
    'Data scientist': 'Data Scientist',
    'Data analyst': 'Data Analyst',
    'Data engineer': 'Data Engineer',
    'Machine learning engineer': 'ML Engineer',
    'Programmer / Software developer': 'Programmer/SW Dev.',
    'Project manager': 'Project Manager',
    'อื่นๆ (โปรดระบุ)': 'Others',
}

# SE method usage values (Thai)
CURRENT_TH = 'ใช้อยู่ในปัจจุบัน'
PAST_TH    = 'เคยใช้ในอดีต (แต่ปัจจุบันไม่ได้ใช้)'
PLAN_TH    = 'วางแผนจะใช้ในอนาคต'

# ---------------------------------------------------------------------------
# Column name sets
# ---------------------------------------------------------------------------

FREQ_COLS = [
    'freq_data_understanding',
    'freq_business_understanding',   # aliased by header col
    'freq_data_preparation',
    'freq_modeling',
    'freq_evaluation',
    'freq_deployment',
]

DS_CHALLENGE_COLS = [
    'challenge_misunderstanding_ds_users_[bu]',
    'challenge_new_unplanned_features_requests_[bu]',
    'challenge_data_cleansing_[dp]',
    'challenge_data_inconsistency_behaviour_drift_[dp]',
    'challenge_incomplete_data_[dp_du]',
    'challenge_learning_curve_data_exploration_[du]',
    'challenge_data_assertion_observability_monitoring_[dpm]',
    'challenge_model_monitoring_[dpm]',
    'challenge_fix_model_bug_[mod]',
]

DS_CHALLENGE_LABELS = {
    'challenge_misunderstanding_ds_users_[bu]':                    'Misunderstanding DS/users [BU]',
    'challenge_new_unplanned_features_requests_[bu]':              'New/unplanned feature requests [BU]',
    'challenge_data_cleansing_[dp]':                               'Data cleansing [DP]',
    'challenge_data_inconsistency_behaviour_drift_[dp]':           'Data inconsistency/drift [DP]',
    'challenge_incomplete_data_[dp_du]':                           'Incomplete data [DP/DU]',
    'challenge_learning_curve_data_exploration_[du]':              'Learning curve in data exploration [DU]',
    'challenge_data_assertion_observability_monitoring_[dpm]':     'Data assertion/observability [DP/M]',
    'challenge_model_monitoring_[dpm]':                            'Model monitoring [DP/M]',
    'challenge_fix_model_bug_[mod]':                               'Fixing model bugs [MOD]',
}

SE_CHALLENGE_COLS = [
    'challenge_many_stakeholders',
    'challenge_no_integration_load_testing',
    'challenge_requirement_changes',
    'challenge_requirements_gathering',
    'challenge_no_version_control',
    'challenge_code_maintenance_reuse',
]

SE_CHALLENGE_LABELS = {
    'challenge_many_stakeholders':           'Many stakeholders (hard to manage)',
    'challenge_no_integration_load_testing': 'No integration/load testing',
    'challenge_requirement_changes':         'Requirement changes mid-project',
    'challenge_requirements_gathering':      'Requirements gathering issues',
    'challenge_no_version_control':          'No version control',
    'challenge_code_maintenance_reuse':      'Code maintenance and reuse',
}

RATING_COLS = {
    'se_tool_ratings_header_rating_requirement_tools': 'Requirement tools',
    'rating_design_tools':        'Design tools',
    'rating_construction_tools':  'Construction tools',
    'rating_testing_tools':       'Testing tools',
    'rating_maintenance_tools':   'Maintenance tools',
    'rating_config_mgmt_tools':   'Config. management tools',
    'rating_se_mgmt_tools':       'SE management tools',
    'rating_process_tools':       'Process tools',
    'rating_quality_tools':       'Quality tools',
    'rating_knowledge_tools':     'Knowledge management tools',
    'rating_meeting_tools':       'Meeting tools',
    'rating_social_tools':        'Social/collaboration tools',
    'rating_misc_tools':          'Miscellaneous tools',
}

METHOD_COLS = {
    'se_methods_usage_header_method_scrum_kanban': 'Scrum/Kanban',
    'method_standup':              'Daily stand-up meetings',
    'method_sprints':              'Sprint/iteration planning',
    'method_code_review':          'Code review',
    'method_coding_convention':    'Coding conventions/standards',
    'method_devops':               'DevOps practices',
    'method_effort_estimation':    'Effort estimation',
    'method_requirements_analysis':'Requirements analysis',
    'method_exit_criteria':        'Exit criteria / DoD',
    'method_integration_testing':  'Integration testing',
    'method_model_testing':        'Model testing',
    'method_uat':                  'User acceptance testing (UAT)',
    'method_unit_testing':         'Unit testing',
    'method_use_case':             'Use case / user story',
    'method_containerization':     'Containerisation',
}

# ---------------------------------------------------------------------------
# Data loading helper
# ---------------------------------------------------------------------------

def load_data(path=DATA_PATH):
    """
    Load and pre-process the SE4DS survey CSV.

    Returns a cleaned DataFrame with:
      - flattened column names
      - sub-header row removed
      - numeric conversions for frequency, challenge, and experience columns
      - binary columns for SE challenge selection
      - 'role', 'ds_exp', 'se_exp' helper columns
    """
    df = pd.read_csv(path, header=[0, 1])

    # Flatten multi-level column names
    df.columns = [
        '_'.join([str(c).strip() for c in col if 'Unnamed' not in str(c)]).strip('_')
        or f'col_{i}'
        for i, col in enumerate(df.columns)
    ]

    # Remove the sub-header row (first data row duplicates column names)
    df = df[df.iloc[:, 0] != df.columns[0]].reset_index(drop=True)

    # Demographic helpers
    df['role']   = df['current_position_Response'].map(ROLE_MAP)
    df['ds_exp'] = df['data_science_experience_Response'].map(DS_EXP_MAP)
    df['se_exp'] = df['software_engineering_experience_Response'].map(SE_EXP_MAP)

    # Numeric conversions: CRISP-DM phase frequencies
    freq_raw_cols = [c for c in df.columns if c.startswith('freq_')]
    for c in freq_raw_cols:
        df[c] = df[c].map(FREQ_MAP)

    # Also handle the header column alias for Business Understanding
    bu_col = 'phase_frequency_header_freq_business_understanding'
    if bu_col in df.columns:
        df[bu_col] = df[bu_col].map(FREQ_MAP)

    # Numeric conversions: DS challenge severity
    for c in DS_CHALLENGE_COLS:
        if c in df.columns:
            df[c] = df[c].map(CHALLENGE_MAP)

    # Binary columns: SE challenges (1 = selected, 0 = not)
    for c in SE_CHALLENGE_COLS:
        if c in df.columns:
            df[c + '_bin'] = df[c].notna().astype(int)

    # Numeric ratings for SE tool categories
    not_used_th = 'ไม่ได้ใช้งาน'
    for c in RATING_COLS:
        if c in df.columns:
            df[c + '_used'] = (df[c] != not_used_th) & df[c].notna()
            df[c + '_num']  = pd.to_numeric(df[c], errors='coerce')

    # SE method adoption binary columns
    for c in METHOD_COLS:
        if c in df.columns:
            df[c + '_curr'] = (df[c] == CURRENT_TH).astype(int)
            df[c + '_plan'] = (df[c] == PLAN_TH).astype(int)
            df[c + '_past'] = (df[c] == PAST_TH).astype(int)

    # Overall SE adoption score
    curr_cols = [c + '_curr' for c in METHOD_COLS if c in df.columns]
    df['adoption_score'] = df[curr_cols].sum(axis=1)

    # Drop rows where future_se_methods and dream_tool_description are identical
    # (only when the shared answer is more than 3 words — single-word or very short
    # answers that happen to match are not treated as duplicates).
    df = _drop_cross_col_duplicates(
        df,
        col_a='future_se_methods_open_ended_response',
        col_b='dream_tool_description_open_ended_response',
        min_words=4,
    )

    # Drop rows where the same long answer appears more than once within either
    # open-ended column (keep only the first occurrence).
    for _col in ('future_se_methods_open_ended_response',
                 'dream_tool_description_open_ended_response'):
        df = _drop_within_col_duplicates(df, col=_col, min_words=4)

    return df


def _drop_cross_col_duplicates(df, col_a, col_b, min_words=4):
    """
    Remove rows where *col_a* and *col_b* contain exactly the same text,
    provided that text is at least *min_words* words long.  When multiple
    rows share the same (col_a, col_b) pair that meets the threshold, only
    the first occurrence is kept.

    Parameters
    ----------
    df : pd.DataFrame
    col_a, col_b : str   Column names to compare.
    min_words : int      Minimum word count for the match to count (default 4,
                         i.e. "more than 3 words").

    Returns
    -------
    pd.DataFrame with duplicate rows removed and the index reset.
    """
    if col_a not in df.columns or col_b not in df.columns:
        return df

    a = df[col_a].fillna('').astype(str).str.strip()
    b = df[col_b].fillna('').astype(str).str.strip()

    # Identify rows where both columns are identical (case-insensitive) and long enough
    same_text   = a.str.lower() == b.str.lower()
    long_enough = a.str.split().str.len() > min_words - 1   # > 3 words means >= 4
    is_suspect  = same_text & long_enough & (a != '')

    # Among suspect rows, mark all but the first occurrence for removal
    # We use the text itself as the dedup key so truly independent identical
    # responses (same person re-submitting) are collapsed.
    suspect_idx = df.index[is_suspect]
    dup_key = a[is_suspect]
    first_seen = set()
    to_drop = []
    for idx, key in zip(suspect_idx, dup_key):
        if key in first_seen:
            to_drop.append(idx)
        else:
            first_seen.add(key)

    if to_drop:
        df = df.drop(index=to_drop).reset_index(drop=True)

    return df


def _drop_within_col_duplicates(df, col, min_words=4):
    """
    Remove rows where *col* contains a repeated long answer, keeping only the
    first occurrence.  Comparison is case-insensitive and ignores trailing
    punctuation so minor formatting differences (e.g. a missing full stop) are
    treated as the same response.

    Parameters
    ----------
    df : pd.DataFrame
    col : str    Column name to check for duplicates.
    min_words : int  Minimum word count for the match to count (default 4).

    Returns
    -------
    pd.DataFrame with duplicate rows removed and the index reset.
    """
    if col not in df.columns:
        return df

    import re as _re

    def _normalise(text):
        """Lowercase and strip trailing punctuation/whitespace."""
        return _re.sub(r'[\s\W]+$', '', str(text).strip().lower())

    normed = df[col].fillna('').astype(str).apply(_normalise)
    long_enough = normed.str.split().str.len() >= min_words

    seen = set()
    to_drop = []
    for idx in df.index:
        if not long_enough[idx]:
            continue
        key = normed[idx]
        if key in seen:
            to_drop.append(idx)
        else:
            seen.add(key)

    if to_drop:
        df = df.drop(index=to_drop).reset_index(drop=True)

    return df
