import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# -----------------------------
# Graph 1: Response Time
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Tasks"], df["ResponseTime"], marker="o")
plt.title("Response Time vs Number of Tasks")
plt.xlabel("Number of Tasks")
plt.ylabel("Response Time")
plt.grid(True)
plt.savefig("response_time.png")
plt.show()

# -----------------------------
# Graph 2: Queue Waiting Time
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Tasks"], df["QueueWait"], marker="o")
plt.title("Queue Waiting Time vs Number of Tasks")
plt.xlabel("Number of Tasks")
plt.ylabel("Queue Waiting Time")
plt.grid(True)
plt.savefig("queue_wait.png")
plt.show()

# -----------------------------
# Graph 3: Energy Per Task
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Tasks"], df["EnergyPerTask"], marker="o")
plt.title("Energy Per Task vs Number of Tasks")
plt.xlabel("Number of Tasks")
plt.ylabel("Energy Per Task")
plt.grid(True)
plt.savefig("energy.png")
plt.show()

# -----------------------------
# Graph 4: Offloading Percentage
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Tasks"], df["OffloadPercentage"], marker="o")
plt.title("Offloading Percentage vs Number of Tasks")
plt.xlabel("Number of Tasks")
plt.ylabel("Offloading Percentage")
plt.grid(True)
plt.savefig("offloading.png")
plt.show()

print("\nAll graphs generated successfully!")