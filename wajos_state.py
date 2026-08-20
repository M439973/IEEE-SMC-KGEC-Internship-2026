import pandas as pd

# Load DE results
df = pd.read_csv("de_results.csv")

state = []

for _, row in df.iterrows():

    tasks = row["Tasks"]

    queue = row["QueueWait"]

    response = row["ResponseTime"]

    overload = 1 if row["Overloads"] > 50000 else 0

    utilization = row["OffloadPercentage"] / 100

    battery = 1 - row["EnergyPerTask"]

    urgency = response / (queue + 0.0001)

    state.append({

        "Tasks": tasks,

        "QueueWait": queue,

        "ResponseTime": response,

        "Overload": overload,

        "Utilization": round(utilization,3),

        "Battery": round(battery,3),

        "Urgency": round(urgency,3)

    })

state_df = pd.DataFrame(state)

state_df.to_csv("wajos_state.csv", index=False)

print(state_df)
print("\nState Monitoring Completed Successfully")