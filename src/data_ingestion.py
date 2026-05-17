print("Data ingestion started...")
import pandas as pd
import os

print("Data ingestion started...")

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({
    "name": ["mohit", "rahul", "aman"],
    "age": [21, 22, 23]
})

df.to_csv("data/raw.csv", index=False)

print("raw.csv created")