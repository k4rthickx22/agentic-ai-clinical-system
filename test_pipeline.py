from agents.patient_agent import PatientAgent
from agents.drug_agent import DrugAgent
from agents.risk_agent import RiskAgent
from agents.decision_agent import DecisionAgent

# Initialize agents
patient_agent = PatientAgent()
drug_agent = DrugAgent()
risk_agent = RiskAgent()
decision_agent = DecisionAgent()

# Step 1: Analyze patient
patient_profile = patient_agent.analyze_patient(
    age=50,
    gender="Male",
    symptoms="high sugar frequent urination",
    allergies="Sulfa",
    conditions="Hypertension"
)

# Step 2: Get drugs
drug_options = drug_agent.get_drugs_for_disease(
    patient_profile["predicted_disease"]
)

# Step 3: Risk evaluation
ranked_drugs = risk_agent.calculate_risk(
    patient_profile,
    drug_options
)

# Step 4: Final decision
final_decision = decision_agent.make_decision(
    patient_profile,
    ranked_drugs
)

print("\nFINAL DECISION\n")
print("Predicted Disease:", final_decision["predicted_disease"])
print("Recommended Drug:", final_decision["recommended_drug"])
print("Risk Score:", final_decision["risk_score"])
print("Explanation:", final_decision["explanation"])