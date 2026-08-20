import pandas as pd

print("=" * 70)
print("GENERATING PERFORMANCE SUMMARY")
print("=" * 70)

# ----------------------------------------------------
# Load Results
# ----------------------------------------------------

de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")
wajos = pd.read_csv("wajos_framework.csv")

# ----------------------------------------------------
# Calculate Statistics
# ----------------------------------------------------

summary = []

metrics = [
    ("ResponseTime", "Response Time"),
    ("EnergyPerTask", "Energy Per Task"),
    ("OffloadPercentage", "Offloading Percentage"),
    ("Overloads", "Overloaded Tasks")
]

for column, metric_name in metrics:

    de_mean = de[column].mean()
    pso_mean = pso[column].mean()
    wajos_mean = wajos[column].mean()

    de_std = de[column].std()
    pso_std = pso[column].std()
    wajos_std = wajos[column].std()

    de_best = de[column].min()
    pso_best = pso[column].min()
    wajos_best = wajos[column].min()

    de_worst = de[column].max()
    pso_worst = pso[column].max()
    wajos_worst = wajos[column].max()

    # Improvement (%) compared to DE
    if de_mean != 0:
        improvement = ((de_mean - wajos_mean) / de_mean) * 100
    else:
        improvement = 0

    summary.append({
        "Metric": metric_name,

        "DE_Mean": round(de_mean, 4),
        "PSO_Mean": round(pso_mean, 4),
        "WAJOS_Mean": round(wajos_mean, 4),

        "DE_STD": round(de_std, 4),
        "PSO_STD": round(pso_std, 4),
        "WAJOS_STD": round(wajos_std, 4),

        "DE_Best": round(de_best, 4),
        "PSO_Best": round(pso_best, 4),
        "WAJOS_Best": round(wajos_best, 4),

        "DE_Worst": round(de_worst, 4),
        "PSO_Worst": round(pso_worst, 4),
        "WAJOS_Worst": round(wajos_worst, 4),

        "Improvement(%)": round(improvement, 2)
    })

# ----------------------------------------------------
# Save Results
# ----------------------------------------------------

summary_df = pd.DataFrame(summary)

summary_df.to_csv("performance_summary.csv", index=False)

print("\nPerformance Summary Generated Successfully!\n")
print(summary_df)

print("\nFile Created:")
print("performance_summary.csv")