import streamlit as st
import requests

API_URL = "https://fraud-detection-tixp.onrender.com"

st.set_page_config(
    page_title="Fraud Detection System",
    layout="centered"
)

st.title("💳 Fraud Detection Decision System")
st.write(
    "This system analyzes a transaction and returns a **risk level** "
    "along with **human-readable reasons**."
)

st.divider()

# -----------------------------
# Transaction Input Form
# -----------------------------

with st.form("transaction_form"):
    transaction_id = st.text_input("Transaction ID", "TXN_DEMO_001")
    amount = st.number_input("Transaction Amount", min_value=1.0, value=1200.0)
    time = st.number_input("Transaction Time (seconds)", min_value=0, value=900000)
    card1 = st.number_input("Card ID (card1)", min_value=0, value=12345)
    addr1 = st.number_input("Address ID (addr1)", min_value=0, value=210)
    device_type = st.selectbox("Device Type", ["desktop", "mobile", None])
    device_info = st.text_input("Device Info", "Windows_Chrome")

    submit = st.form_submit_button("Analyze Transaction")

# -----------------------------
# Call FastAPI
# -----------------------------

if submit:
    payload = {
        "TransactionID": transaction_id,
        "TransactionAmt": amount,
        "TransactionDT": int(time),
        "card1": int(card1),
        "addr1": int(addr1),
        "DeviceType": device_type,
        "DeviceInfo": device_info
    }

    with st.spinner("Analyzing transaction..."):
        response = requests.post(f"{API_URL}/predict", json=payload)

    if response.status_code == 200:
        result = response.json()

        st.subheader("🔍 Fraud Assessment Result")

        # Risk Level
        risk = result["risk_level"]
        if "High" in risk:
            st.error(f"🚨 Risk Level: {risk}")
        elif "Medium" in risk:
            st.warning(f"⚠️ Risk Level: {risk}")
        else:
            st.success(f"✅ Risk Level: {risk}")

        # Reasons
        st.markdown("### 📌 Why this transaction was flagged")
        if result["reasons"]:
            for r in result["reasons"]:
                st.write(f"- {r}")
        else:
            st.write("No suspicious patterns detected.")

        # Action
        st.markdown("### 🛠 Recommended Action")
        st.info(result["recommended_action"])

    else:
        st.error("Error calling fraud detection API")
        st.write("Status code:", response.status_code)
        st.write("Response text:", response.text)