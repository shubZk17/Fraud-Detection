import joblib
import shap
from pathlib import Path


# -----------------------------
# Paths (Single Source of Truth)
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"


# -----------------------------
# Singleton Containers
# -----------------------------

_model = None
_feature_cols = None
_reason_map = None
_explainer = None


# -----------------------------
# Loaders
# -----------------------------

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(ARTIFACTS_DIR / "xgb_model_v1.pkl")
    return _model


def load_feature_columns():
    global _feature_cols
    if _feature_cols is None:
        _feature_cols = joblib.load(ARTIFACTS_DIR / "xgb_features_v1.pkl")
    return _feature_cols


def load_reason_map():
    global _reason_map
    if _reason_map is None:
        _reason_map = joblib.load(ARTIFACTS_DIR / "reason_map.pkl")
    return _reason_map


def load_explainer():
    """
    SHAP TreeExplainer is heavy.
    Load once and reuse for all requests.
    """
    global _explainer
    if _explainer is None:
        model = load_model()
        _explainer = shap.TreeExplainer(model)
    return _explainer
