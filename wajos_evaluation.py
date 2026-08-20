import pandas as pd

print("=" * 70)
print("WA-JOS FRAMEWORK EVALUATION")
print("=" * 70)

# -----------------------------------
# Load Results
# -----------------------------------

de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")
wajos = pd.read_csv("wajos_framework.csv")

# Load LION only if available
try:
    lion = pd.read_csv("lion_results.csv")
    has_lion = True
except:
    has_lion = False

evaluation = []

# -----------------------------------
# Compare Results
# -----------------------------------

for i in range(len(de)):

    row = {
        "Tasks": de.loc[i, "Tasks"],

        # -----------------------------
        # Response Time
        # -----------------------------
        "DE_ResponseTime": de.loc[i, "ResponseTime"],
        "PSO_ResponseTime": pso.loc[i, "ResponseTime"],
        "WAJOS_ResponseTime": wajos.loc[i, "ResponseTime"],

        # -----------------------------
        # Energy
        # -----------------------------
        "DE_Energy": de.loc[i, "EnergyPerTask"],
        "PSO_Energy": pso.loc[i, "EnergyPerTask"],
        "WAJOS_Energy": wajos.loc[i, "EnergyPerTask"],

        # -----------------------------
        # Offloading
        # -----------------------------
        "DE_Offloading": de.loc[i, "OffloadPercentage"],
        "PSO_Offloading": pso.loc[i, "OffloadPercentage"],
        "WAJOS_Offloading": wajos.loc[i, "OffloadPercentage"],

        # -----------------------------
        # Overloads
        # -----------------------------
        "DE_Overloads": de.loc[i, "Overloads"],
        "PSO_Overloads": pso.loc[i, "Overloads"],
        "WAJOS_Overloads": wajos.loc[i, "Overloads"]
    }

    if has_lion:
        row["LION_ResponseTime"] = lion.loc[i, "ResponseTime"]
        row["LION_Energy"] = lion.loc[i, "EnergyPerTask"]
        row["LION_Offloading"] = lion.loc[i, "OffloadPercentage"]
        row["LION_Overloads"] = lion.loc[i, "Overloads"]

    evaluation.append(row)

# -----------------------------------
# Save Evaluation
# -----------------------------------

evaluation_df = pd.DataFrame(evaluation)

evaluation_df.to_csv("wajos_evaluation.csv", index=False)

print("\nEvaluation Completed Successfully!\n")
print(evaluation_df)

print("\nFile Created:")
print("wajos_evaluation.csv")