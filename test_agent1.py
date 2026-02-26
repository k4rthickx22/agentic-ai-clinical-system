from agents.patient_agent import PatientAgent

agent = PatientAgent()

result = agent.analyze_patient(
    age=50,
    gender="Male",
    symptoms="high sugar frequent urination",
    allergies="None",
    conditions="Hypertension"
)

print(result)