from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import pagesizes
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime


def generate_pdf(file_path, patient_data, decision, severity):

    doc = SimpleDocTemplate(
        file_path,
        pagesize=pagesizes.A4
    )

    elements = []
    styles = getSampleStyleSheet()

    # Custom Title Style
    title_style = styles["Heading1"]
    title_style.textColor = colors.HexColor("#1f4e79")

    # ---------------------------
    # HEADER
    # ---------------------------
    elements.append(Paragraph("AI Clinical Decision Support Report", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 0.3 * inch))

    # ---------------------------
    # PATIENT INFO TABLE
    # ---------------------------
    patient_table_data = [
        ["Age", patient_data["age"]],
        ["Gender", patient_data["gender"]],
        ["Predicted Disease", decision["predicted_disease"]],
        ["Severity Level", severity]
    ]

    patient_table = Table(patient_table_data, colWidths=[2 * inch, 3 * inch])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#e6f2ff")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    elements.append(Paragraph("<b>Patient Summary</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(patient_table)
    elements.append(Spacer(1, 0.4 * inch))

    # ---------------------------
    # MEDICATION SECTION
    # ---------------------------
    elements.append(Paragraph("<b>Medication Plan</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    medication_table_data = [
        ["Medicine", decision["recommended_drug"]],
        ["Dosage", decision["dosage"]],
        ["Duration", decision["duration"]],
    ]

    medication_table = Table(medication_table_data, colWidths=[2 * inch, 3 * inch])
    medication_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#f2f2f2")),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))

    elements.append(medication_table)
    elements.append(Spacer(1, 0.4 * inch))

    # ---------------------------
    # EXPLANATION
    # ---------------------------
    elements.append(Paragraph("<b>Clinical Explanation</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(decision["explanation"], styles["Normal"]))
    elements.append(Spacer(1, 0.4 * inch))

    # ---------------------------
    # LIFESTYLE
    # ---------------------------
    elements.append(Paragraph("<b>Lifestyle & Recovery Advice</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    for item in decision.get("lifestyle", []):
        elements.append(Paragraph(f"• {item}", styles["Normal"]))

    elements.append(Spacer(1, 0.4 * inch))

    # ---------------------------
    # WARNINGS
    # ---------------------------
    elements.append(Paragraph("<b>Warning Signs</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    for warn in decision.get("warnings", []):
        elements.append(Paragraph(f"• {warn}", styles["Normal"]))

    elements.append(Spacer(1, 0.5 * inch))

    # ---------------------------
    # FOOTER DISCLAIMER
    # ---------------------------
    elements.append(Paragraph(
        "<i>This AI-generated report is for clinical decision support only. "
        "Please consult a licensed medical professional before taking medication.</i>",
        styles["Normal"]
    ))

    doc.build(elements)