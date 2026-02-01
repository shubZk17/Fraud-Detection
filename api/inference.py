import pandas as pd
import numpy as np
from typing import List

from src.model_loader import (
    load_model,
    load_feature_columns
)
from src.feature_engineering import build_features
from src.explainability import explain_transaction
from src.decision import risk_bucket, recommended_action


# -----------------------------
# Internal Core Logic
# -----------------------------

def _predict_dataframe(df_input: pd.DataFrame) -> List[dict]:
    """
    Core prediction logic for both single and batch inference.

    Parameters
    ----------
    df_input : pd.DataFrame
        Raw input transactions

    Returns
    -------
    List[dict]
        List of decision results
    """

    model = load_model()
    feature_cols = load_feature_columns()

    feature_df = build_features(df_input)


    
    for col in feature_cols:
        if col not in feature_df.columns:
            feature_df[col] = np.nan

    X = feature_df[feature_cols]
    probs = model.predict_proba(X)[:, 1]

    results = []

  
    for i, prob in enumerate(probs):
        risk = risk_bucket(prob)
        action = recommended_action(risk)

        reasons = explain_transaction(
            feature_df=feature_df,
            row_index=i,
            top_k=3
        )

        results.append({
            "TransactionID": df_input.iloc[i]["TransactionID"],
            "risk_level": risk,
            "reasons": reasons,
            "recommended_action": action
        })

    return results




def predict_one(transaction: dict) -> dict:
    """
    Run fraud prediction for a single transaction.

    Parameters
    ----------
    transaction : dict
        Raw transaction input

    Returns
    -------
    dict
        Fraud decision result
    """

    df = pd.DataFrame([transaction])
    result = _predict_dataframe(df)

    return result[0]


def predict_batch(transactions: List[dict]) -> List[dict]:
    """
    Run fraud prediction for a batch of transactions.

    Parameters
    ----------
    transactions : List[dict]
        List of raw transaction inputs

    Returns
    -------
    List[dict]
        List of fraud decision results
    """

    df = pd.DataFrame(transactions)
    return _predict_dataframe(df)
