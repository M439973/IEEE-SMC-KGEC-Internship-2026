import pandas as pd
import matplotlib.pyplot as plt

# Load DE and PSO results
de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")
lion = pd.read_csv("lion_results.csv")

# -------------------------------
# 1. Response Time Comparison
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(de["Tasks"], de["ResponseTime"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["ResponseTime"], marker='s', label="PSO")
plt.plot(lion["Tasks"], lion["ResponseTime"], marker='^', label="LION")
plt.title("Response Time Comparison")
plt.xlabel("Number of Tasks")
plt.ylabel("Response Time")
plt.legend()
plt.grid(True)
plt.savefig("response_time_comparison.png")
plt.close()

# -------------------------------
# 2. Queue Waiting Time Comparison
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(de["Tasks"], de["QueueWait"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["QueueWait"], marker='s', label="PSO")
plt.plot(lion["Tasks"], lion["QueueWait"], marker='^', label="LION")
plt.title("Queue Waiting Time Comparison")
plt.xlabel("Number of Tasks")
plt.ylabel("Queue Waiting Time")
plt.legend()
plt.grid(True)
plt.savefig("queue_wait_comparison.png")
plt.close()

# -------------------------------
# 3. Energy Consumption Comparison
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(de["Tasks"], de["EnergyPerTask"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["EnergyPerTask"], marker='s', label="PSO")
plt.plot(lion["Tasks"], lion["EnergyPerTask"], marker='^', label="LION")
plt.title("Energy Consumption Comparison")
plt.xlabel("Number of Tasks")
plt.ylabel("Energy Per Task")
plt.legend()
plt.grid(True)
plt.savefig("energy_comparison.png")
plt.close()

# -------------------------------
# 4. Offloading Percentage Comparison
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(de["Tasks"], de["OffloadPercentage"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["OffloadPercentage"], marker='s', label="PSO")
plt.plot(lion["Tasks"], lion["OffloadPercentage"], marker='^', label="LION")
plt.title("Offloading Percentage Comparison")
plt.xlabel("Number of Tasks")
plt.ylabel("Offloading Percentage")
plt.legend()
plt.grid(True)
plt.savefig("offloading_comparison.png")
plt.close()

# -------------------------------
# 5. Overloaded Tasks Comparison
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(de["Tasks"], de["Overloads"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["Overloads"], marker='s', label="PSO")
plt.plot(lion["Tasks"], lion["Overloads"], marker='^', label="LION")
plt.title("Overloaded Tasks Comparison")
plt.xlabel("Number of Tasks")
plt.ylabel("Overloaded Tasks")
plt.legend()
plt.grid(True)
plt.savefig("overloads_comparison.png")
plt.close()

print("="*60)
print("Graphs Generated Successfully")
print("="*60)

print("Saved Files:")
print("1. response_time_comparison.png")
print("2. queue_wait_comparison.png")
print("3. energy_comparison.png")
print("4. offloading_comparison.png")
print("5. overloads_comparison.png")