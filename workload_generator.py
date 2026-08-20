import pandas as pd
import random

# Number of workloads
workloads = []

# Generate workloads from 5000 to 100000
for tasks in range(5000, 100001, 5000):

    workload = {
        "Tasks": tasks,
        "TaskSize_MB": round(random.uniform(1, 10), 2),
        "CPU_Cycles": random.randint(500, 5000),
        "Memory_MB": random.randint(256, 4096),
        "Arrival_Time": random.randint(1, 100),
        "Deadline": random.randint(100, 500),
    }

    workloads.append(workload)

# Convert to DataFrame
df = pd.DataFrame(workloads)

# Save CSV
df.to_csv("workloads.csv", index=False)

print("=" * 50)
print("Workload Generation Completed Successfully")
print("=" * 50)

print("\nGenerated Workloads:")
print(df)

print("\nTotal Workloads:", len(df))

print("\nFile Saved As : workloads.csv")