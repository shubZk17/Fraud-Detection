from fastapi import FastAPI
from api.schemas import (
    SinglePredictionRequest,
    BatchPredictionRequest,
    PredictionResult,
    BatchPredictionResponse
)
from api.inference import predict_one, predict_batch


# -----------------------------
# App Initialization
# -----------------------------

app = FastAPI(
    title="Fraud Detection Decision API",
    description=(
        "End-to-end fraud detection system that returns "
        "risk levels and human-readable reasons using "
        "machine learning and explainable AI."
    ),
    version="1.0.0"
)


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}


# -----------------------------
# Single Transaction Prediction
# -----------------------------

@app.post(
    "/predict",
    response_model=PredictionResult,
    summary="Predict fraud risk for a single transaction"
)
def predict_single(request: SinglePredictionRequest):
    """
    Predict fraud risk for a single transaction.
    """
    result = predict_one(request.dict())
    return result


# -----------------------------
# Batch Transaction Prediction
# -----------------------------

@app.post(
    "/predict/batch",
    response_model=BatchPredictionResponse,
    summary="Predict fraud risk for a batch of transactions"
)
def predict_batch_endpoint(request: BatchPredictionRequest):
    """
    Predict fraud risk for a batch of transactions.
    """
    results = predict_batch(
        [txn.dict() for txn in request.transactions]
    )
    return {"results": results}
