from random_forest import model
from de import DifferentialEvolution
from pso import ParticleSwarmOptimization
import pandas as pd

print("========== TASK OFFLOADING SIMULATION ==========\n")

# Get task size from user
tasks = int(input("Enter Number of Tasks: "))

# Example values (replace later with real simulation values)
queue_wait = tasks + 100
response_time = tasks + 200
energy = 0.193
offload = 10.5
overloads = int(tasks * 0.95)

# Create DataFrame (avoids the warning)
new_data = pd.DataFrame({
    "Tasks": [tasks],
    "QueueWait": [queue_wait],
    "ResponseTime": [response_time],
    "EnergyPerTask": [energy],
    "OffloadPercentage": [offload],
    "Overloads": [overloads]
})

# Predict algorithm
algorithm = model.predict(new_data)[0]

print("\nRandom Forest Selected:", algorithm)

# Run selected optimizer
if algorithm == "DE":
    print("\nRunning Differential Evolution...\n")
    de = DifferentialEvolution()
    solution, fitness = de.optimize()

else:
    print("\nRunning Particle Swarm Optimization...\n")
    pso = ParticleSwarmOptimization()
    solution, fitness = pso.optimize()

print("Best Solution:")
print(solution)

print("\nBest Fitness:")
print(fitness)