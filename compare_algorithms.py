import pandas as pd

# ----------------------------------------------------
# Load DE and PSO Results
# ----------------------------------------------------

de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")

# ----------------------------------------------------
# Min-Max Normalization
# ----------------------------------------------------

def normalize(column):
    if column.max() == column.min():
        return pd.Series([0] * len(column), index=column.index)
    return (column - column.min()) / (column.max() - column.min())

# ----------------------------------------------------
# Weights
# ----------------------------------------------------

LATENCY_WEIGHT = 0.20
ENERGY_WEIGHT = 0.20
COST_WEIGHT = 0.15
SLA_WEIGHT = 0.20
LOAD_WEIGHT = 0.15
THROUGHPUT_WEIGHT = 0.10

# ----------------------------------------------------
# SLA Parameters
# ----------------------------------------------------

BETA = 0.20
SLA_LIMIT = 0.70

# ----------------------------------------------------
# Normalize Original Metrics
# ----------------------------------------------------

for df in [de, pso]:

    df["QueueWait"] = normalize(df["QueueWait"])
    df["ResponseTime"] = normalize(df["ResponseTime"])
    df["EnergyPerTask"] = normalize(df["EnergyPerTask"])
    df["OffloadPercentage"] = normalize(df["OffloadPercentage"])
    df["Overloads"] = normalize(df["Overloads"])

# ----------------------------------------------------
# Create Derived Metrics
# ----------------------------------------------------

for df in [de, pso]:

    df["Cost"] = df["EnergyPerTask"] * 5
    df["SLA"] = df["ResponseTime"]
    df["Load"] = df["QueueWait"]
    df["Throughput"] = df["Tasks"] / (df["ResponseTime"] + 0.0001)
    df["SLA_Violation"] = (df["SLA"] > SLA_LIMIT).astype(int)

# ----------------------------------------------------
# Normalize Derived Metrics
# ----------------------------------------------------

for df in [de, pso]:

    df["Cost"] = normalize(df["Cost"])
    df["SLA"] = normalize(df["SLA"])
    df["Load"] = normalize(df["Load"])
    df["Throughput"] = normalize(df["Throughput"])

# ----------------------------------------------------
# Compare Algorithms
# ----------------------------------------------------

comparison = []

print("=" * 70)
print("Comparing Differential Evolution (DE) and PSO")
print("=" * 70)

for i in range(len(de)):

    # Calculate DE score
    de_score = (
        LATENCY_WEIGHT * de.loc[i, "ResponseTime"]
        + ENERGY_WEIGHT * de.loc[i, "EnergyPerTask"]
        + COST_WEIGHT * de.loc[i, "Cost"]
        + SLA_WEIGHT * de.loc[i, "SLA"]
        + LOAD_WEIGHT * de.loc[i, "Load"]
        - THROUGHPUT_WEIGHT * de.loc[i, "Throughput"]
    )

    de_score = de_score + (BETA * de.loc[i, "SLA_Violation"])

    # Calculate PSO score
    pso_score = (
        LATENCY_WEIGHT * pso.loc[i, "ResponseTime"]
        + ENERGY_WEIGHT * pso.loc[i, "EnergyPerTask"]
        + COST_WEIGHT * pso.loc[i, "Cost"]
        + SLA_WEIGHT * pso.loc[i, "SLA"]
        + LOAD_WEIGHT * pso.loc[i, "Load"]
        - THROUGHPUT_WEIGHT * pso.loc[i, "Throughput"]
    )

    pso_score = pso_score + (BETA * pso.loc[i, "SLA_Violation"])

    # Choose winner
    if de_score <= pso_score:
        winner = "DE"
    else:
        winner = "PSO"

    # Save one row
    comparison.append({
        "Tasks": de.loc[i, "Tasks"],
        "DE_Fitness": round(de_score, 4),
        "PSO_Fitness": round(pso_score, 4),
        "QueueWait": min(de.loc[i, "QueueWait"], pso.loc[i, "QueueWait"]),
        "ResponseTime": min(de.loc[i, "ResponseTime"], pso.loc[i, "ResponseTime"]),
        "EnergyPerTask": min(de.loc[i, "EnergyPerTask"], pso.loc[i, "EnergyPerTask"]),
        "OffloadPercentage": max(de.loc[i, "OffloadPercentage"], pso.loc[i, "OffloadPercentage"]),
        "Overloads": min(de.loc[i, "Overloads"], pso.loc[i, "Overloads"]),
        "BestAlgorithm": winner
    })

# ----------------------------------------------------
# Save Results
# ----------------------------------------------------

comparison_df = pd.DataFrame(comparison)

comparison_df.to_csv("comparison.csv", index=False)
comparison_df.to_csv("dataset.csv", index=False)

print("\nComparison Completed Successfully!\n")
print(comparison_df)

print("\nFiles Created:")
print("comparison.csv")
print("dataset.csv")

print("\nTotal Records Generated:", len(comparison_df))