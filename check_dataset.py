import pandas as pd

# Read dataset
df = pd.read_csv("dataset.csv")

# Show first 5 rows
print(df.head())

# Show information
print("\nDataset Information:\n")
print(df.info())

# Show total rows and columns
print("\nShape:", df.shape)