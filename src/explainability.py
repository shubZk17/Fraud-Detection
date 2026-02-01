import pandas as pd
from typing import List

from src.model_loader import (
    load_explainer,
    load_feature_columns,
    load_reason_map
)


# -----------------------------
# Constants
# -----------------------------

GENERIC_V_REASON = "Unusual behavioral pattern detected"


# -----------------------------
# Core Explanation Logic
# -----------------------------

def generate_reason_codes(
    feature_row: pd.Series,
    shap_values_row,
    top_k: int = 3
) -> List[str]:
    """
    Convert SHAP values into stable, human-readable reason codes.

    Parameters
    ----------
    feature_row : pd.Series
        Feature values for a single transaction
    shap_values_row : array-like
        SHAP values for the same transaction
    top_k : int
        Maximum number of reasons to return

    Returns
    -------
    List[str]
        List of reason strings
    """

    feature_cols = load_feature_columns()
    reason_map = load_reason_map()

    shap_series = pd.Series(shap_values_row, index=feature_cols)
    shap_series = shap_series.sort_values(ascending=False)

    reasons = []
    used_generic_v = False

    for feature, contribution in shap_series.items():
        if contribution <= 0:
            continue

        # Priority 1: Interpretable features
        if feature in reason_map:
            reason = reason_map[feature]
            if reason not in reasons:
                reasons.append(reason)

        # Priority 2: V-features (only once)
        elif feature.startswith("V") and not used_generic_v:
            reasons.append(GENERIC_V_REASON)
            used_generic_v = True

        if len(reasons) == top_k:
            break

    return reasons


# -----------------------------
# Public API
# -----------------------------

def explain_transaction(
    feature_df: pd.DataFrame,
    row_index: int = 0,
    top_k: int = 3
) -> List[str]:
    """
    Generate explanation reasons for a single transaction.

    Parameters
    ----------
    feature_df : pd.DataFrame
        Feature-engineered DataFrame (must include all model features)
    row_index : int
        Index of the row to explain
    top_k : int
        Maximum number of reasons

    Returns
    -------
    List[str]
        Human-readable explanation reasons
    """

    explainer = load_explainer()
    feature_cols = load_feature_columns()

    X = feature_df[feature_cols]
    shap_values = explainer.shap_values(X)

    shap_row = shap_values[row_index]
    feature_row = X.iloc[row_index]

    return generate_reason_codes(
        feature_row=feature_row,
        shap_values_row=shap_row,
        top_k=top_k
    )
