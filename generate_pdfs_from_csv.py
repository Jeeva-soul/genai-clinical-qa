import pandas as pd
from fpdf import FPDF
import os

# ✅ Absolute path to CSV
csv_path = r"E:\DATA SCIENTIST\Project\genai-clinical-qa\data\clinical_docs\brain_tumor_dataset.csv"

def csv_to_pdfs(csv_path, output_dir, row_limit=20):
    df = pd.read_csv(csv_path)
    os.makedirs(output_dir, exist_ok=True)

    for i, row in df.iterrows():
        if i >= row_limit:
            break  # only generate first N for testing

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Patient Case #{i+1}", ln=True)

        for col in df.columns:
            content = str(row[col])
            pdf.multi_cell(0, 10, f"{col}: {content}")  # ✅ Correct


        pdf.output(f"{output_dir}/case_{i+1}.pdf")

# ✅ Call the function using same correct csv_path
csv_to_pdfs(csv_path, "data/clinical_docs")
