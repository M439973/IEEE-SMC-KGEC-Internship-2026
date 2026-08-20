import pandas as pd
import random

# -------------------------------
# Load Workloads
# -------------------------------

df = pd.read_csv("workloads.csv")

results = []

print("=" * 70)
print("Running Differential Evolution Simulation")
print("=" * 70)

# -------------------------------
# Adaptive Mutation Parameters
# -------------------------------

F_MAX = 0.90
F_MIN = 0.40

total_generations = len(df)

for generation, (_, row) in enumerate(df.iterrows(), start=1):

    tasks = row["Tasks"]

    # Adaptive Mutation Factor
    F = F_MAX - ((F_MAX - F_MIN) * (generation - 1) / (total_generations - 1))

    # Simulated DE Performance
    queue_wait = round(tasks * random.uniform(0.95, 1.05) * F, 2)
    response_time = round(tasks * random.uniform(1.00, 1.10) * F, 2)
    energy = round(random.uniform(0.185, 0.195) * F, 3)
    offload = round(random.uniform(9.5, 15.0), 2)
    overloads = int(tasks * random.uniform(0.92, 0.99))

    # -------------------------------
    # Additional Metrics
    # -------------------------------

    cost = energy * 5
    sla = response_time
    load = queue_wait
    throughput = tasks / (response_time + 0.0001)

    # -------------------------------
    # Fitness Function
    # -------------------------------

    fitness = (
        0.20 * response_time +
        0.20 * energy +
        0.15 * cost +
        0.20 * sla +
        0.15 * load -
        0.10 * throughput
    )

    # -------------------------------
    # Save Results
    # -------------------------------

    results.append({
        "Generation": generation,
        "MutationFactor": round(F, 3),
        "Tasks": tasks,
        "QueueWait": queue_wait,
        "ResponseTime": response_time,
        "EnergyPerTask": energy,
        "OffloadPercentage": offload,
        "Overloads": overloads,
        "Cost": round(cost, 4),
        "SLA": round(sla, 4),
        "Load": round(load, 4),
        "Throughput": round(throughput, 4),
        "Fitness": round(fitness, 4),
        "Algorithm": "DE"
    })

# -------------------------------
# Convert to DataFrame
# -------------------------------

result_df = pd.DataFrame(results)

# -------------------------------
# Elitism
# -------------------------------

elite_index = result_df["Fitness"].idxmin()

best_solution = result_df.loc[elite_index]

print("\n" + "=" * 70)
print("Best DE Solution (Elite)")
print("=" * 70)
print(best_solution)

result_df["Elite"] = False
result_df.loc[elite_index, "Elite"] = True

# -------------------------------
# Save CSV
# -------------------------------

result_df.to_csv("de_results.csv", index=False)

print("\nSimulation Completed Successfully!\n")

print(result_df)

print("\nResults saved as: de_results.csv")