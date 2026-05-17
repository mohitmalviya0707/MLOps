print("Data preprocessing started...")

import pandas as pd

print("Data preprocessing started...")

df = pd.read_csv("data/raw.csv")

df.to_csv("data/processed.csv", index=False)

print("processed.csv created")