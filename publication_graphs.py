import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# Load Results
# ---------------------------------------

de = pd.read_csv("de_results.csv")
pso = pd.read_csv("pso_results.csv")
wajos = pd.read_csv("wajos_framework.csv")

# Optional LION
try:
    lion = pd.read_csv("lion_results.csv")
    lion_available = True
except:
    lion_available = False

# ---------------------------------------
# Response Time
# ---------------------------------------

plt.figure(figsize=(8,5))

plt.plot(de["Tasks"], de["ResponseTime"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["ResponseTime"], marker='s', label="PSO")
plt.plot(wajos["Tasks"], wajos["ResponseTime"], marker='D', label="WA-JOS")

if lion_available:
    plt.plot(lion["Tasks"], lion["ResponseTime"], marker='^', label="LION")

plt.title("Response Time Comparison")
plt.xlabel("Tasks")
plt.ylabel("Response Time")
plt.grid(True)
plt.legend()
plt.savefig("Paper_ResponseTime.png")
plt.close()

# ---------------------------------------
# Energy Comparison
# ---------------------------------------

plt.figure(figsize=(8,5))

plt.plot(de["Tasks"], de["EnergyPerTask"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["EnergyPerTask"], marker='s', label="PSO")
plt.plot(wajos["Tasks"], wajos["EnergyPerTask"], marker='D', label="WA-JOS")

if lion_available:
    plt.plot(lion["Tasks"], lion["EnergyPerTask"], marker='^', label="LION")

plt.title("Energy Comparison")
plt.xlabel("Tasks")
plt.ylabel("Energy Per Task")
plt.grid(True)
plt.legend()
plt.savefig("Paper_Energy.png")
plt.close()

# ---------------------------------------
# Offloading Comparison
# ---------------------------------------

plt.figure(figsize=(8,5))

plt.plot(de["Tasks"], de["OffloadPercentage"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["OffloadPercentage"], marker='s', label="PSO")
plt.plot(wajos["Tasks"], wajos["OffloadPercentage"], marker='D', label="WA-JOS")

if lion_available:
    plt.plot(lion["Tasks"], lion["OffloadPercentage"], marker='^', label="LION")

plt.title("Offloading Percentage Comparison")
plt.xlabel("Tasks")
plt.ylabel("Offloading Percentage")
plt.grid(True)
plt.legend()
plt.savefig("Paper_Offloading.png")
plt.close()

# ---------------------------------------
# Overloads Comparison
# ---------------------------------------

plt.figure(figsize=(8,5))

plt.plot(de["Tasks"], de["Overloads"], marker='o', label="DE")
plt.plot(pso["Tasks"], pso["Overloads"], marker='s', label="PSO")
plt.plot(wajos["Tasks"], wajos["Overloads"], marker='D', label="WA-JOS")

if lion_available:
    plt.plot(lion["Tasks"], lion["Overloads"], marker='^', label="LION")

plt.title("Overloaded Tasks Comparison")
plt.xlabel("Tasks")
plt.ylabel("Overloaded Tasks")
plt.grid(True)
plt.legend()
plt.savefig("Paper_Overloads.png")
plt.close()

print("=" * 60)
print("Publication Graphs Generated Successfully")
print("=" * 60)

print("Generated Files:")
print("1. Paper_ResponseTime.png")
print("2. Paper_Energy.png")
print("3. Paper_Offloading.png")
print("4. Paper_Overloads.png")