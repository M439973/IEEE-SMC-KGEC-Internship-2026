import subprocess
import pandas as pd
from random_forest import model

print("=" * 70)
print("INTELLIGENT TASK OFFLOADING SYSTEM")
print("=" * 70)

print("\nStep 1 : Generating Workloads...")
subprocess.run(["python", "workload_generator.py"])

print("\nStep 2 : Running Differential Evolution...")
subprocess.run(["python", "de.py"])

print("\nStep 3 : Running Particle Swarm Optimization...")
subprocess.run(["python", "pso.py"])

print("\nStep 4 : Comparing Algorithms...")
subprocess.run(["python", "compare_algorithms.py"])

print("\nStep 5 : Predicting Best Algorithm")

tasks = int(input("\nEnter Number of Tasks: "))

queue_wait = tasks * 0.98
response_time = tasks * 1.03
energy = 0.188
offload = 13.0
overloads = int(tasks * 0.94)

sample = pd.DataFrame({
    "Tasks": [tasks],
    "QueueWait": [queue_wait],
    "ResponseTime": [response_time],
    "EnergyPerTask": [energy],
    "OffloadPercentage": [offload],
    "Overloads": [overloads]
})

prediction = model.predict(sample)

print("\n" + "=" * 50)
print("FINAL RESULT")
print("=" * 50)

print("Tasks :", tasks)
print("Selected Algorithm :", prediction[0])

print("\nSystem Execution Completed Successfully")