import pandas as pd

print("=" * 70)
print("EXPORTING FINAL PROJECT REPORT")
print("=" * 70)

# ----------------------------------------------------
# Load All Files
# ----------------------------------------------------

comparison = pd.read_csv("comparison.csv")
performance = pd.read_csv("performance_summary.csv")
evaluation = pd.read_csv("wajos_evaluation.csv")
final_results = pd.read_csv("final_results.csv")
dataset = pd.read_csv("dataset.csv")

# ----------------------------------------------------
# Create Excel Report
# ----------------------------------------------------

with pd.ExcelWriter("Final_Project_Report.xlsx", engine="openpyxl") as writer:

    comparison.to_excel(
        writer,
        sheet_name="Comparison",
        index=False
    )

    performance.to_excel(
        writer,
        sheet_name="Performance Summary",
        index=False
    )

    evaluation.to_excel(
        writer,
        sheet_name="WAJOS Evaluation",
        index=False
    )

    final_results.to_excel(
        writer,
        sheet_name="Final Results",
        index=False
    )

    dataset.to_excel(
        writer,
        sheet_name="Training Dataset",
        index=False
    )

print("\nExcel Report Created Successfully!")

print("\nGenerated File:")
print("Final_Project_Report.xlsx")

print("\nProject Report Export Completed Successfully!")