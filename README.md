# Fraud Detection System – End‑to‑End ML Project

## 1. Project Overview

This project builds a **production‑oriented fraud detection system** for the banking/payments domain. The goal is not only to train a high‑performing ML model, but to **translate model outputs into human‑understandable decisions** that can be consumed by non‑technical users.

The system is designed in **three clear phases**:

1. **Modeling & Explainability** – Data analysis, feature engineering, XGBoost modeling, SHAP‑based explainability
2. **Business Communication** – Insight‑focused dashboards (Power BI) for stakeholders
3. **Production Deployment** – Real‑time inference with FastAPI + Streamlit, returning risk levels and human‑readable reasons

This mirrors how fraud systems are built in real banks and fintech companies.

---

## 2. Dataset

**IEEE‑CIS Fraud Detection Dataset**

* Transaction‑level banking data (`train_transaction.csv`)
* Device and identity enrichment (`train_identity.csv`)
* Severe class imbalance (~3–4% fraud), realistic noise, high dimensionality

The dataset is intentionally split to simulate real banking systems where transaction data and identity data come from different sources.

---

## 3. Project Objectives

* Build a robust fraud detection model using tree‑based ML (XGBoost)
* Handle class imbalance and time‑based validation correctly
* Use SHAP internally for explainability
* Convert ML explanations into **plain‑language reason codes**
* Present insights through dashboards understandable by non‑technical users
* Deploy an end‑to‑end inference pipeline

---

## 4. High‑Level Architecture

**Phase 1 – Modeling (Notebook‑Driven)**

* Data pre-processing , EDA
* Feature engineering (transaction‑level + behavioral)
* Baseline models → advanced XGBoost model
* SHAP analysis (global & local)

**Phase 2 – Communication (Power BI)**

* Risk distribution trends
* Top fraud drivers (human‑readable)
* High‑risk transaction summaries

**Phase 3 – Production (API + UI)**

* FastAPI inference service
* SHAP‑derived reason code generation
* Streamlit UI for user input & results

---

## 5. Repository Structure

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
├── dashboards/               # Power BI files / exports
│   ├── fraud_dashboard.pbix
│
├── requirements.txt
├── .gitignore
├── README.md
└── .venv/                    # Virtual environment (not committed)
```

---

## 6. Explainability Strategy (Key Design Decision)

* SHAP is used **internally** to understand model behavior
* End users never see SHAP values or plots
* SHAP outputs are mapped to **reason codes**, e.g.:

  * "Unusually high transaction amount"
  * "New or unknown device detected"
  * "High transaction velocity"

This ensures trust, consistency, and regulatory alignment.

---

## 7. Model Output Design (User‑Facing)

Instead of probabilities, the system returns:

* **Risk Level**: Low / Medium / High / Very High
* **Reasons**: Top 2–3 human‑readable explanations
* **Recommended Action**: Allow / Verify / Hold / Block

This design prioritizes decision clarity over raw metrics.

---

## 8. Tech Stack

* **Python** – Core language
* **Pandas / NumPy** – Data processing
* **XGBoost** – Fraud classification model (Best performing model in Kaggle IEE- CIS Fraude detection challange in 2019)
* **SHAP** – Model explainability (internal)
* **FastAPI** – Inference service
* **Streamlit** – Interactive UI
* **Power BI** – Business dashboards

---

## 9. Development Phases & Milestones

**Phase 1 – Modeling (Current Focus)**

* Complete EDA and feature engineering
* Train and validate XGBoost model
* Perform SHAP analysis

**Phase 2 – Communication**

* Create Power BI dashboard from aggregated outputs

**Phase 3 – Deployment**

* Build FastAPI inference API
* Build Streamlit UI
* End‑to‑end demo

---

## 10. Notes

* Raw data files are excluded from Git
* The project emphasizes **decision intelligence**, not just ML accuracy
* Structure is designed to scale to production‑grade systems
