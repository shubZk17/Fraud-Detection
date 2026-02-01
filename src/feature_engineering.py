import pandas as pd
import numpy as np




def build_features(
    input_df: pd.DataFrame,
    history_df: pd.DataFrame | None = None
) -> pd.DataFrame:
    """
    Build model features from raw transaction input.

    Parameters
    ----------
    input_df : pd.DataFrame
        Raw input transactions (single or batch)
    history_df : pd.DataFrame | None
        Optional historical transactions for context
        (used in batch / production; None for demo)

    Returns
    -------
    pd.DataFrame
        Feature-engineered DataFrame ready for model inference
    """

    df = input_df.copy()

    df["uid"] = df["card1"].astype(str) + "_" + df["addr1"].astype(str)

  
    if history_df is None:
        history_df = df.copy()

    history_df = history_df.sort_values("TransactionDT")

    history_df["uid_txn_count"] = history_df.groupby("uid").cumcount()

    df = df.merge(
        history_df[["TransactionID", "uid_txn_count"]],
        on="TransactionID",
        how="left"
    )

    
    history_df["uid_avg_amt"] = (
        history_df.groupby("uid")["TransactionAmt"]
        .expanding()
        .mean()
        .shift()
        .reset_index(level=0, drop=True)
    )

    history_df["amt_vs_uid_avg"] = (
        history_df["TransactionAmt"] / history_df["uid_avg_amt"]
    )

    df = df.merge(
        history_df[
            ["TransactionID", "uid_avg_amt", "amt_vs_uid_avg"]
        ],
        on="TransactionID",
        how="left"
    )

    history_df["uid_prev_dt"] = (
        history_df.groupby("uid")["TransactionDT"].shift()
    )

    history_df["uid_time_since_last"] = (
        history_df["TransactionDT"] - history_df["uid_prev_dt"]
    )

    df = df.merge(
        history_df[
            ["TransactionID", "uid_time_since_last"]
        ],
        on="TransactionID",
        how="left"
    )

    # -------------------------------------------------
    # Identity presence flag
    # -------------------------------------------------
    df["has_identity"] = (
        df["DeviceType"].notna() | df["DeviceInfo"].notna()
    ).astype(int)

    # -------------------------------------------------
    # M-features (if present)
    # -------------------------------------------------
    m_cols = [c for c in df.columns if c.startswith("M")]
    for c in m_cols:
        df[c] = df[c].map({"T": 1, "F": 0}).fillna(-1)

    # -------------------------------------------------
    # Device encoding
    # -------------------------------------------------
    for c in ["DeviceType", "DeviceInfo"]:
        if c in df.columns:
            df[c] = df[c].astype("category").cat.codes

    return df
