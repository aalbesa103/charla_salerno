import fitz  # PyMuPDF
import os

pdf_dir = "papers"
output_file = "ground_truth_papers.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_dir, filename)
            try:
                doc = fitz.open(path)
                out.write(f"--- START PAPER: {filename} ---\n")
                # Extraer las primeras 2 páginas para Abstract y Metodología
                for page_num in range(min(2, len(doc))):
                    out.write(doc[page_num].get_text())
                out.write(f"\n--- END PAPER: {filename} ---\n\n")
                doc.close()
            except Exception as e:
                out.write(f"Error reading {filename}: {e}\n")

print(f"Extracción completada en {output_file}")
