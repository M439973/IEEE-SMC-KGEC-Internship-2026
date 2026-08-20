import pandas as pd

# ---------------------------------
# Load WA-JOS State
# ---------------------------------

state = pd.read_csv("wajos_state.csv")

results = []

print("=" * 70)
print("WA-JOS Adaptive Offloading Selector")
print("=" * 70)

for _, row in state.iterrows():

    tasks = row["Tasks"]
    queue = row["QueueWait"]
    response = row["ResponseTime"]
    overload = row["Overload"]
    urgency = row["Urgency"]

    # ---------------------------------
    # WA-JOS Decision Rules
    # ---------------------------------

    if overload == 1:
        algorithm = "DE"

    elif tasks >= 85000:
        algorithm = "DE"

    elif urgency > 1.0:
        algorithm = "PSO"

    elif queue > response:
        algorithm = "DE"

    else:
        algorithm = "PSO"

    results.append({

        "Tasks": tasks,
        "QueueWait": queue,
        "ResponseTime": response,
        "Overload": overload,
        "Urgency": round(urgency, 3),
        "SelectedAlgorithm": algorithm

    })

selector_df = pd.DataFrame(results)

selector_df.to_csv("adaptive_selection.csv", index=False)

print("\nAdaptive Selection Completed Successfully\n")

print(selector_df)

print("\nFile Created:")
print("adaptive_selection.csv")