import pandas as pd

print("=" * 70)
print("WA-JOS FRAMEWORK")
print("=" * 70)

# ---------------------------------------
# Load all WA-JOS modules
# ---------------------------------------

state = pd.read_csv("wajos_state.csv")
selection = pd.read_csv("adaptive_selection.csv")
scheduler = pd.read_csv("adaptive_scheduler.csv")
feedback = pd.read_csv("feedback_results.csv")

# ---------------------------------------
# Merge all modules
# ---------------------------------------

framework = state.copy()

framework["SelectedAlgorithm"] = selection["SelectedAlgorithm"]

framework["SelectedScheduler"] = scheduler["SelectedScheduler"]

framework["FeedbackAction"] = feedback["FeedbackAction"]

# ------------------------------------
# Add Performance Metrics from DE
# ------------------------------------

de = pd.read_csv("de_results.csv")

framework["EnergyPerTask"] = de["EnergyPerTask"]
framework["OffloadPercentage"] = de["OffloadPercentage"]
framework["Overloads"] = de["Overloads"]

# ------------------------------------
# Save Final WA-JOS Output
# ------------------------------------

framework.to_csv("wajos_framework.csv", index=False)

print("\nWA-JOS Framework Completed Successfully!\n")

print(framework)

print("\nFile Created:")
print("wajos_framework.csv")