import pandas as pd

# ------------------------------------
# Load Scheduler Output
# ------------------------------------

df = pd.read_csv("adaptive_scheduler.csv")

feedback = []

print("=" * 70)
print("WA-JOS Closed-Loop Feedback Controller")
print("=" * 70)

for _, row in df.iterrows():

    tasks = row["Tasks"]
    queue = row["QueueWait"]
    response = row["ResponseTime"]
    scheduler = row["SelectedScheduler"]

    # ------------------------------------
    # Feedback Rules
    # ------------------------------------

    if response > queue * 1.10:
        action = "Increase Edge Resources"

    elif scheduler == "RR":
        action = "Switch to GA Scheduling"

    elif scheduler == "GA":
        action = "Maintain Current Scheduling"

    else:
        action = "Re-evaluate"

    feedback.append({

        "Tasks": tasks,
        "QueueWait": queue,
        "ResponseTime": response,
        "Scheduler": scheduler,
        "FeedbackAction": action

    })

feedback_df = pd.DataFrame(feedback)

feedback_df.to_csv("feedback_results.csv", index=False)

print("\nFeedback Controller Completed Successfully!\n")

print(feedback_df)

print("\nFile Created:")
print("feedback_results.csv")