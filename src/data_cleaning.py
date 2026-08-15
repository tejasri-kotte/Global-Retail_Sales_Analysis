import pandas as pd

# Load dataset
df = pd.read_csv("data/SuperStore_Orders.csv", encoding="latin1")

print("Dataset loaded successfully!")

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date columns
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

# Remove rows with missing important values
df = df.dropna(subset=["order_date", "sales", "profit"])

print("\nData cleaning completed!")

print("Rows and Columns after cleaning:")
print(df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
df.to_csv("data/cleaned_superstore_orders.csv", index=False)

print("Cleaned dataset saved successfully!")