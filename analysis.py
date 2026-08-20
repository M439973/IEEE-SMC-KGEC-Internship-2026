import pandas as pd

# Load comparison results
df = pd.read_csv("comparison.csv")

print("=" * 60)
print("PROJECT PERFORMANCE ANALYSIS")
print("=" * 60)

print("\nTotal Workloads:", len(df))

print("\nBest Algorithm Counts:")
print(df["BestAlgorithm"].value_counts())

print("\nAverage Queue Wait:")
print(df["QueueWait"].mean())

print("\nAverage Response Time:")
print(df["ResponseTime"].mean())

print("\nAverage Energy Per Task:")
print(df["EnergyPerTask"].mean())

print("\nAverage Offload Percentage:")
print(df["OffloadPercentage"].mean())

print("\nAverage Overloads:")
print(df["Overloads"].mean())

summary = pd.DataFrame({
    "Metric": [
        "Average QueueWait",
        "Average ResponseTime",
        "Average Energy",
        "Average Offload",
        "Average Overloads"
    ],
    "Value": [
        df["QueueWait"].mean(),
        df["ResponseTime"].mean(),
        df["EnergyPerTask"].mean(),
        df["OffloadPercentage"].mean(),
        df["Overloads"].mean()
    ]
})

summary.to_csv("performance_summary.csv", index=False)

print("\nperformance_summary.csv created successfully.")