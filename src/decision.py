

def risk_bucket(prob: float) -> str:
    """
    Convert fraud probability into human-readable risk level.

    Parameters
    ----------
    prob : float
        Fraud probability output by the model

    Returns
    -------
    str
        Risk level
    """

    if prob >= 0.85:
        return "Very High Risk"
    elif prob >= 0.65:
        return "High Risk"
    elif prob >= 0.35:
        return "Medium Risk"
    else:
        return "Low Risk"


# -----------------------------
# Action Mapping
# -----------------------------

def recommended_action(risk_level: str) -> str:
    """
    Map risk level to recommended business action.

    Parameters
    ----------
    risk_level : str

    Returns
    -------
    str
        Recommended action
    """

    if risk_level == "Very High Risk":
        return "Block transaction and initiate investigation"
    elif risk_level == "High Risk":
        return "Hold transaction and request verification"
    elif risk_level == "Medium Risk":
        return "Allow transaction with step-up authentication"
    else:
        return "Allow transaction"
