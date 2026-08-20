import pandas as pd

# ------------------------------------
# Load Adaptive Offloading Results
# ------------------------------------

df = pd.read_csv("adaptive_selection.csv")

results = []

print("=" * 70)
print("WA-JOS Adaptive Scheduling Selector")
print("=" * 70)

for _, row in df.iterrows():

    tasks = row["Tasks"]
    queue = row["QueueWait"]
    response = row["ResponseTime"]
    overload = row["Overload"]
    urgency = row["Urgency"]

    # ------------------------------------
    # Scheduling Decision Rules
    # ------------------------------------

    if urgency >= 1.0:
        scheduler = "GA"

    elif overload == 1:
        scheduler = "RR"

    elif queue > response:
        scheduler = "RR"

    elif tasks >= 85000:
        scheduler = "RR"

    else:
        scheduler = "GA"

    results.append({

        "Tasks": tasks,
        "QueueWait": queue,
        "ResponseTime": response,
        "Overload": overload,
        "Urgency": round(urgency, 3),
        "SelectedScheduler": scheduler

    })

scheduler_df = pd.DataFrame(results)

scheduler_df.to_csv("adaptive_scheduler.csv", index=False)

print("\nAdaptive Scheduling Completed Successfully!\n")

print(scheduler_df)

print("\nFile Created:")
print("adaptive_scheduler.csv")