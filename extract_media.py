import os
import zipfile
import shutil
import glob
import sys

def convert_ppt_to_pptx(ppt_path):
    print(f"Convirtiendo a PPTX: {ppt_path}")
    try:
        import win32com.client
        powerpoint = win32com.client.Dispatch("Powerpoint.Application")
        powerpoint.Visible = True
        deck = powerpoint.Presentations.Open(os.path.abspath(ppt_path), WithWindow=False)
        
        pptx_path = os.path.abspath(ppt_path + "x")
        deck.SaveAs(pptx_path, 24) # 24 is pptx
        deck.Close()
        return pptx_path
    except Exception as e:
        print(f"Error convirtiendo {ppt_path}: {e}")
        return None

def extract_from_pptx(pptx_path, output_dir):
    print(f"Extrayendo imágenes de: {pptx_path}")
    base_name = os.path.basename(pptx_path).replace('.pptx', '')
    out_path = os.path.join(output_dir, base_name)
    os.makedirs(out_path, exist_ok=True)
    
    try:
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename.startswith('ppt/media/'):
                    filename = os.path.basename(file_info.filename)
                    if filename: # Not a directory
                        source = zip_ref.open(file_info.filename)
                        target = open(os.path.join(out_path, filename), "wb")
                        with source, target:
                            shutil.copyfileobj(source, target)
        print(f"Imágenes guardadas en: {out_path}")
    except Exception as e:
        print(f"Error extrayendo {pptx_path}: {e}")

def extract_from_pdf(pdf_path, output_dir):
    print(f"Extrayendo imágenes de PDF: {pdf_path}")
    base_name = os.path.basename(pdf_path).replace('.pdf', '')
    out_path = os.path.join(output_dir, base_name)
    os.makedirs(out_path, exist_ok=True)
    
    try:
        import fitz # PyMuPDF
        doc = fitz.open(pdf_path)
        img_count = 0
        for i in range(len(doc)):
            for img in doc.get_page_images(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha < 4:       # this is GRAY or RGB
                    pix.save(os.path.join(out_path, f"img_{i}_{xref}.png"))
                else:               # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.save(os.path.join(out_path, f"img_{i}_{xref}.png"))
                    pix1 = None
                pix = None
                img_count += 1
        print(f"Extraídas {img_count} imágenes en: {out_path}")
    except ImportError:
        print("PyMuPDF (fitz) no está instalado. Ejecuta: pip install PyMuPDF")
    except Exception as e:
        print(f"Error con PDF {pdf_path}: {e}")

if __name__ == "__main__":
    output_dir = "imagenes_extraidas"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. PPT files
    for ppt in glob.glob("*.ppt"):
        pptx_path = convert_ppt_to_pptx(ppt)
        if pptx_path:
            extract_from_pptx(pptx_path, output_dir)
            
    # 2. PPTX files
    for pptx in glob.glob("*.pptx"):
        # Ignore the ones we just created if they have .pptx.pptx? No, pattern is *.pptx
        # We also might have native pptx
        extract_from_pptx(pptx, output_dir)
        
    # 3. PDF files
    for pdf in glob.glob("papers/*.pdf"):
        extract_from_pdf(pdf, output_dir)
