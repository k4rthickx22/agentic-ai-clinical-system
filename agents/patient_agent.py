import joblib

class PatientAgent:

    def __init__(self):
        # Load trained disease model
        self.model = joblib.load("models/disease_model.pkl")

    def analyze_patient(self, age, gender, symptoms, allergies, conditions):
        # Predict disease
        predicted_disease = self.model.predict([symptoms])[0]

        # Create structured profile
        patient_profile = {
            "age": age,
            "gender": gender,
            "symptoms": symptoms,
            "allergies": allergies,
            "conditions": conditions,
            "predicted_disease": predicted_disease
        }

        return patient_profile