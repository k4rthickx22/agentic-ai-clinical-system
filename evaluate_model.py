import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# Load dataset
data = pd.read_csv("data/patient_training.csv")

X = data["symptoms"]
y_true = data["disease"]

# Load trained model
model = joblib.load("models/disease_model.pkl")

# Predict
y_pred = model.predict(X)

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_true, y_pred))