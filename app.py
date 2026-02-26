import streamlit as st
import os
import joblib

from agents.patient_agent import PatientAgent
from agents.drug_agent import DrugAgent
from agents.risk_agent import RiskAgent
from agents.decision_agent import DecisionAgent
from agents.severity_agent import SeverityAgent
from utils.pdf_generator import generate_pdf

# -----------------------------
# PAGE CONFIG MUST BE FIRST
# -----------------------------
st.set_page_config(page_title="AI Clinical Dashboard", layout="wide")

# -----------------------------
# CUSTOM CSS STYLING
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
h1 {
    color: #1f4e79;
    font-weight: bold;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stDownloadButton>button {
    background-color: #28a745;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# INITIALIZE AGENTS
# -----------------------------
patient_agent = PatientAgent()
drug_agent = DrugAgent()
risk_agent = RiskAgent()
decision_agent = DecisionAgent()
severity_agent = SeverityAgent()

# Load trained model (for confidence score)
model = joblib.load("models/disease_model.pkl")

# -----------------------------
# TITLE
# -----------------------------
st.title("🧠 AI Clinical Decision Support Dashboard")
st.markdown("### Intelligent Disease Prediction & Personalized Treatment Plan")
st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    allergies = st.text_input("Allergies")
    conditions = st.text_input("Existing Conditions")

with col2:
    symptoms = st.text_area("Describe Symptoms")

st.divider()

# -----------------------------
# MAIN LOGIC
# -----------------------------
if st.button("🔍 Generate Clinical Plan"):

    if not symptoms.strip():
        st.warning("Please enter symptoms.")
        st.stop()

    # Disease Prediction
    patient_profile = patient_agent.analyze_patient(
        age=age,
        gender=gender,
        symptoms=symptoms,
        allergies=allergies,
        conditions=conditions
    )

    predicted_disease = patient_profile["predicted_disease"]

    # Confidence Score
    if hasattr(model, "decision_function"):
        confidence = model.decision_function([symptoms]).max()
        confidence_score = round(abs(confidence), 2)
    else:
        confidence_score = "N/A"

    # Drug + Risk + Decision
    drug_options = drug_agent.get_drugs_for_disease(predicted_disease)
    ranked_drugs = risk_agent.calculate_risk(patient_profile, drug_options)
    final_decision = decision_agent.make_decision(patient_profile, ranked_drugs)

    severity = severity_agent.detect_severity(predicted_disease, symptoms)

    # -----------------------------
    # DASHBOARD DISPLAY
    # -----------------------------
    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Predicted Disease", predicted_disease)

    with colB:
        st.metric("Severity Level", severity)

    with colC:
        st.metric("Model Confidence", confidence_score)

    st.divider()

    # Severity Color Alert
    if severity == "High":
        st.error("🚨 High Severity Case – Immediate medical consultation advised.")
    else:
        st.success("⚠ Moderate Condition – Follow treatment guidance carefully.")

    st.divider()

    # -----------------------------
    # PATIENT SUMMARY CARD
    # -----------------------------
    st.markdown("### 🧾 Patient Summary")
    st.markdown(f"""
    **Age:** {age}  
    **Gender:** {gender}  
    **Disease Identified:** {predicted_disease}  
    **Recommended Medicine:** {final_decision['recommended_drug']}
    """)

    st.divider()

    # -----------------------------
    # MEDICATION PLAN
    # -----------------------------
    st.markdown("### 💊 Medication Plan")
    st.write("**Dosage:**", final_decision["dosage"])
    st.write("**Duration:**", final_decision["duration"])

    st.divider()

    # -----------------------------
    # EXPLANATION
    # -----------------------------
    st.markdown("### 📘 Why This Medicine?")
    st.write(final_decision["explanation"])

    st.divider()

    # -----------------------------
    # LIFESTYLE
    # -----------------------------
    st.markdown("### 🥗 Lifestyle & Recovery Steps")
    if final_decision.get("lifestyle"):
        for step in final_decision["lifestyle"]:
            st.write("•", step)
    else:
        st.write("No lifestyle plan available.")

    st.divider()

    # -----------------------------
    # WARNINGS
    # -----------------------------
    st.markdown("### ⚠ Warning Signs")
    for warn in final_decision["warnings"]:
        st.write("•", warn)

    st.divider()

    # -----------------------------
    # PDF REPORT
    # -----------------------------
    file_path = "clinical_report.pdf"

    generate_pdf(
    file_path,
    {"age": age, "gender": gender},
    final_decision,
    severity
)

    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Download Clinical Report (PDF)",
            data=f,
            file_name="AI_Clinical_Report.pdf",
            mime="application/pdf"
        )
        st.write("DEBUG Disease:", predicted_disease)
    st.caption("⚠ This AI system is for decision support only. Always consult a licensed medical professional.")