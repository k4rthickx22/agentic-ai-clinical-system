class RiskAgent:

    def calculate_risk(self, patient_profile, drug_options):

        evaluated_drugs = []

        for drug in drug_options:

            risk_score = 0

            # Age Check
            if not (drug["min_age"] <= patient_profile["age"] <= drug["max_age"]):
                risk_score += 10

            # Allergy Check
            patient_allergy = str(patient_profile["allergies"]).lower()
            drug_allergy = str(drug["allergy"]).lower()

            if drug_allergy != "nan" and drug_allergy != "none":
                if drug_allergy in patient_allergy:
                    risk_score += 20

            # Side effect severity
            risk_score += drug["side_effect_severity"]

            drug["risk_score"] = risk_score
            evaluated_drugs.append(drug)

        # Sort by lowest risk
        evaluated_drugs = sorted(evaluated_drugs, key=lambda x: x["risk_score"])

        return evaluated_drugs