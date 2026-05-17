print("Model building started...")

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

print("Model building started...")

df = pd.read_csv("data/features.csv")

X = df[["age", "age_plus_5"]]
y = [0, 1, 0]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("model.pkl created")