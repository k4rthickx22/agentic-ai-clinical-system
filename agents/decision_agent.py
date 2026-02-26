from agents.clinical_protocol import clinical_protocols

class DecisionAgent:

    def make_decision(self, patient_profile, ranked_drugs):

        predicted_disease = patient_profile["predicted_disease"]

        # Get structured clinical protocol
        protocol = clinical_protocols.get(predicted_disease)

        # If protocol exists → use structured clinical recommendation
        if protocol:
            return {
    "predicted_disease": predicted_disease,
    "recommended_drug": protocol["first_line"],
    "dosage": protocol["dosage"],
    "duration": protocol["duration"],
    "explanation": protocol["explanation"],
    "lifestyle": protocol["lifestyle"],
    "warnings": protocol["warnings"],
    "risk_score": "Clinically Optimized"
}

        # Fallback if no protocol found
        if not ranked_drugs:
            return {
                "predicted_disease": predicted_disease,
                "recommended_drug": "No drug available",
                "risk_score": "N/A",
                "explanation": "No suitable drug found in database for this disease.",
                "dosage": "N/A",
                "duration": "N/A",
                "lifestyle": [],
                "warnings": []
            }

        best_drug = ranked_drugs[0]

        explanation = (
            f"The recommended drug is {best_drug['drug_name']} "
            f"because it has the lowest risk score ({best_drug['risk_score']}). "
            f"It is suitable for age {patient_profile['age']}."
        )

        return {
            "predicted_disease": predicted_disease,
            "recommended_drug": best_drug["drug_name"],
            "risk_score": best_drug["risk_score"],
            "explanation": explanation,
            "dosage": "Refer prescription",
            "duration": "As advised",
            "lifestyle": [],
            "warnings": []
        }