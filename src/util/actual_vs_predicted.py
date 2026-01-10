import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load dataset
data = pd.read_csv("notebook/data/stud.csv")

X = data.drop("math_score", axis=1)
y = data["math_score"]

# Load trained model & preprocessor
preprocessor = joblib.load("artifacts/preprocessor.pkl")
model = joblib.load("artifacts/model.pkl")

# Transform input features
X_transformed = preprocessor.transform(X)

# Predict
y_pred = model.predict(X_transformed)

# Plot Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, alpha=0.6)
plt.plot([0, 100], [0, 100]) 
plt.xlabel("Actual Math Score")
plt.ylabel("Predicted Math Score")
plt.title("Actual vs Predicted Math Score")
plt.grid(True)


plt.savefig("static/images/actual_vs_predicted.png")
plt.close()

print("Actual vs Predicted chart generated successfully")
