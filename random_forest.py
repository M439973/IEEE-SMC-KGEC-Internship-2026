import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully\n")

# Features
X = df[[
    "Tasks",
    "QueueWait",
    "ResponseTime",
    "EnergyPerTask",
    "OffloadPercentage",
    "Overloads"
]]

# Target
y = df["BestAlgorithm"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%\n")

print("Classification Report\n")
print(classification_report(y_test, y_pred))

# Example Prediction
new_task = [[25000,25856,25969,0.193,9.77,24678]]

prediction = model.predict(new_task)

print("Prediction for New Task")
print("Selected Algorithm :", prediction[0])