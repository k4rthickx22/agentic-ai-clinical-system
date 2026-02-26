class SeverityAgent:

    def detect_severity(self, predicted_disease, symptoms):

        symptoms = symptoms.lower()

        severe_keywords = {
            "Pneumonia": ["breathing distress", "severe chest pain"],
            "Dengue Fever": ["bleeding", "severe abdominal pain"],
            "Asthma": ["severe breathlessness", "unable to speak"],
            "Hypertension": ["chest pain", "vision loss"],
            "Diabetes": ["confusion", "unconscious"],
            "Anemia": ["fainting", "extreme weakness"],
            "Viral Fever": ["persistent high fever"]
        }

        if predicted_disease in severe_keywords:
            for word in severe_keywords[predicted_disease]:
                if word in symptoms:
                    return "High"

        return "Moderate"