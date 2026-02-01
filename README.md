# 🚨 End-to-End Fraud Detection System (Banking & FinTech)

## 📌 Project Overview

This project is a **production-oriented, end-to-end fraud detection system** built using real-world banking data (IEEE-CIS Fraud Detection dataset).

Unlike notebook-only ML projects, this system focuses on:
- **Decision intelligence**
- **Explainability**
- **Deployment-ready architecture**

The system predicts fraud risk, explains *why* a transaction was flagged, and exposes results via a **FastAPI backend** with a **Streamlit UI** for non-technical users.

---

## 🧠 Key Features

- Large-scale fraud dataset (IEEE-CIS)
- Time-aware feature engineering (no data leakage)
- XGBoost model for highly imbalanced fraud data
- SHAP-based explainability with stable, human-readable reason codes
- Business-level risk bucketing & recommended actions
- FastAPI backend (single + batch inference)
- Streamlit UI for live demo and presentation
- Production-safe handling of missing real-time features

---



## 2. Dataset

**IEEE‑CIS Fraud Detection Dataset**

* Transaction‑level banking data (`train_transaction.csv`)
* Device and identity enrichment (`train_identity.csv`)
* Severe class imbalance (~3–4% fraud), realistic noise, high dimensionality

The dataset is intentionally split to simulate real banking systems where transaction data and identity data come from different sources.

---

## 3. Repository Structure

```
fraud-detection/
│
├── data/                     # Raw and processed datasets (NOT pushed to Git)
│   ├── train_transaction.csv
│   ├── train_identity.csv
│
├── notebooks/                # Phase 1 – Analysis & Modeling
│   ├── 01_data_overview.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling_xgboost.ipynb
│   ├── 05_shap_explainability.ipynb
│
├── src/                      # Reusable Python modules
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── explainability.py
│   ├── utils.py
│
├── api/                      # Phase 3 – FastAPI service
│   ├── main.py
│   ├── schemas.py
│   ├── inference.py
│
├── ui/                       # Streamlit application
│   ├── app.py
│
│
├── requirements.txt
├── .gitignore
├── README.md
└── .venv/                    # Virtual environment (not committed)
```



---

## 4. How to Run Locally

### Clone the Repository

```bash
git clone https://github.com/<your-username>/fraud-detection.git
cd fraud-detection
```

```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```
```bash
python -m uvicorn api.main:app --reload
```
```bash
streamlit run ui/app.py
```


## Live Link

```
https://shubzk17-fraud-detection-uiapp-9nvkgf.streamlit.app/
```


