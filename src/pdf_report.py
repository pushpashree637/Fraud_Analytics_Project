from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

metrics = pd.read_csv(BASE_DIR / "reports" / "model_metrics.csv")
comparison = pd.read_csv(BASE_DIR / "reports" / "model_comparison.csv")

pdf = SimpleDocTemplate(
    str(BASE_DIR / "reports" / "Fraud_Analytics_Report.pdf")
)

styles = getSampleStyleSheet()

elements = []

elements.append(
    Paragraph(
        "<b>AI Financial Transaction Fraud Analytics Report</b>",
        styles["Title"]
    )
)

elements.append(
    Paragraph("<br/><b>Model Evaluation Metrics</b>", styles["Heading2"])
)

metric_data = [["Metric", "Value"]]

for _, row in metrics.iterrows():
    metric_data.append([row["Metric"], str(round(row["Value"],4))])

table = Table(metric_data)

table.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige)
]))

elements.append(table)

elements.append(
    Paragraph("<br/><b>Model Comparison</b>", styles["Heading2"])
)

comparison_data=[comparison.columns.tolist()]

comparison_data += comparison.values.tolist()

table2=Table(comparison_data)

table2.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.darkblue),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('BACKGROUND',(0,1),(-1,-1),colors.lightgrey)
]))

elements.append(table2)

pdf.build(elements)

print("PDF Report Generated Successfully!")