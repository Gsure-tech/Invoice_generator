import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=row["product_id"])
        pdf.cell(w=70, h=8, txt=row["product_name"])
        pdf.cell(w=30, h=8, txt=row["product_id"])
        pdf.cell(w=30, h=8, txt=row["product_id"])
        pdf.cell(w=30, h=8, txt=row["product_id"])


    pdf.output(f"PDFs/{filename}.pdf")
