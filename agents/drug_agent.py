import pandas as pd

class DrugAgent:

    def __init__(self):
        # Load drug dataset
        self.drugs = pd.read_csv("data/drugs.csv")

    def get_drugs_for_disease(self, disease):
        # Filter drugs matching disease
        filtered = self.drugs[self.drugs["disease"] == disease]

        return filtered.to_dict(orient="records")