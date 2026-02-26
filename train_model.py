import pandas as pd
import joblib
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# ---------------------------
# Load Deep Dataset
# ---------------------------
data = pd.read_csv("data/patient_training_deep.csv")

X = data["symptoms"]
y = data["disease"]

print("Total Samples:", len(data))
print("Unique Classes:", len(y.unique()))
print("Classes:", y.unique())

# ---------------------------
# Build Strong NLP Model
# ---------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        max_features=5000
    )),
    ("clf", LinearSVC())
])

# ---------------------------
# Stratified 5-Fold CV
# ---------------------------
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores = cross_val_score(model, X, y, cv=skf)

print("\nCross Validation Accuracy Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))

# ---------------------------
# Train-Test Split Evaluation
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nHoldout Test Accuracy:", np.mean(y_pred == y_test))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# ---------------------------
# Train on Full Dataset
# ---------------------------
model.fit(X, y)

joblib.dump(model, "models/disease_model.pkl")

print("\nModel trained on full dataset and saved successfully!")