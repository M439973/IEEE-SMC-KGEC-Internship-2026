import pandas as pd

# ---------------------------------
# Load Result Files
# ---------------------------------

de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")
wajos = pd.read_csv("wajos_evaluation.csv")

# Optional LION
try:
    lion = pd.read_csv("lion_results.csv")
    lion_available = True
except:
    lion_available = False

results = []

for i in range(len(de)):

    row = {
        "Tasks": de.loc[i, "Tasks"],

        "DE_ResponseTime": de.loc[i, "ResponseTime"],
        "PSO_ResponseTime": pso.loc[i, "ResponseTime"],
        "WAJOS_ResponseTime": wajos.loc[i, "WAJOS_ResponseTime"],

        "DE_Energy": de.loc[i, "EnergyPerTask"],
        "PSO_Energy": pso.loc[i, "EnergyPerTask"],
        "WAJOS_Energy": wajos.loc[i, "WAJOS_Energy"],

        "DE_Offloading": de.loc[i, "OffloadPercentage"],
        "PSO_Offloading": pso.loc[i, "OffloadPercentage"],
        "WAJOS_Offloading": wajos.loc[i, "WAJOS_Offloading"],

        "DE_Overloads": de.loc[i, "Overloads"],
        "PSO_Overloads": pso.loc[i, "Overloads"],
        "WAJOS_Overloads": wajos.loc[i, "WAJOS_Overloads"]
    }

    if lion_available:
        row["LION_ResponseTime"] = lion.loc[i, "ResponseTime"]
        row["LION_Energy"] = lion.loc[i, "EnergyPerTask"]
        row["LION_Offloading"] = lion.loc[i, "OffloadPercentage"]
        row["LION_Overloads"] = lion.loc[i, "Overloads"]

    results.append(row)

final_df = pd.DataFrame(results)

final_df.to_csv("final_results.csv", index=False)

print("=" * 60)
print("FINAL RESULT TABLE CREATED")
print("=" * 60)
print(final_df)

print("\nSaved as final_results.csv")