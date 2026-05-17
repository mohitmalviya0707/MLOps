print("Feature engineering started...")

import pandas as pd

print("Feature engineering started...")

df = pd.read_csv("data/processed.csv")

df["age_plus_5"] = df["age"] + 5

df.to_csv("data/features.csv", index=False)

print("features.csv created")