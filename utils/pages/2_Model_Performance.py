import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

# Page Config
st.set_page_config(page_title="Model Performance", layout="wide")

st.title("📊 Model Performance Dashboard")
st.markdown("### Disease Classification Model Evaluation")

# Load dataset
data = pd.read_csv("data/patient_training_deep.csv")

X = data["symptoms"]
y = data["disease"]

# Load trained model
model = joblib.load("models/disease_model.pkl")

# Train-test split (for visualization)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

y_pred = model.predict(X_test)

# Accuracy
accuracy = (y_pred == y_test).mean()

st.metric("Model Accuracy", f"{accuracy*100:.2f}%")

# Classification Report
st.subheader("📄 Classification Report")
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.dataframe(report_df)

# Confusion Matrix
st.subheader("📊 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=model.classes_,
            yticklabels=model.classes_)
plt.ylabel("Actual")
plt.xlabel("Predicted")

st.pyplot(fig)