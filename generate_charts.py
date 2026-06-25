import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/creditcard.csv")
IMAGE_DIR = Path("images")
IMAGE_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
fraud = df[df["Class"] == 1]["Amount"]
normal = df[df["Class"] == 0]["Amount"]

plt.figure(figsize=(7,5))
counts = df["Class"].value_counts().sort_index()
plt.bar(["Normal (0)", "Fraud (1)"], [counts.get(0,0), counts.get(1,0)])
plt.title("Fraud vs Normal Transactions")
plt.xlabel("Transaction Class")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "fraud_vs_normal.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.hist(df["Amount"], bins=60)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "amount_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.hist(df["Time"], bins=60)
plt.title("Transaction Time Distribution")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "time_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(7,5))
plt.boxplot([normal, fraud], tick_labels=["Normal", "Fraud"], showfliers=False)
plt.title("Normal vs Fraud Transaction Amounts")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "amount_boxplot.png", dpi=150)
plt.close()

corr = df.corr(numeric_only=True)["Class"].drop("Class").sort_values(key=lambda s: s.abs(), ascending=False).head(10)
plt.figure(figsize=(8,5))
plt.bar(corr.index, corr.values)
plt.title("Top 10 Features Correlated With Fraud Class")
plt.xlabel("Feature")
plt.ylabel("Correlation with Class")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "top_correlations.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.hist(fraud, bins=40)
plt.title("Fraud Transaction Amount Distribution")
plt.xlabel("Fraud Transaction Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "fraud_amount_distribution.png", dpi=150)
plt.close()

print("Charts saved inside images/ folder.")
