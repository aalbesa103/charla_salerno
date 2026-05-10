import os
import glob
import fitz  # PyMuPDF
from PIL import Image, PngImagePlugin
import io

def reconstruct_text(text_block):
    text = ""
    for line in text_block.get("lines", []):
        for span in line.get("spans", []):
            text += span.get("text", "") + " "
    return text.strip()

def is_caption(text):
    text_lower = text.lower()
    return text_lower.startswith("fig") or text_lower.startswith("scheme") or text_lower.startswith("chart")

def calculate_distance(bbox1, bbox2):
    # bbox is (x0, y0, x1, y1)
    # Simple vertical distance if bbox2 is below bbox1
    if bbox2[1] >= bbox1[3]: # bbox2 is below bbox1
        return bbox2[1] - bbox1[3]
    elif bbox1[1] >= bbox2[3]: # bbox1 is below bbox2
        return bbox1[1] - bbox2[3]
    return 0 # overlapping vertically

def extract_from_pdf(pdf_path, output_dir):
    print(f"Procesando: {pdf_path}")
    base_name = os.path.basename(pdf_path).replace('.pdf', '')
    out_path = os.path.join(output_dir, base_name)
    os.makedirs(out_path, exist_ok=True)
    
    try:
        doc = fitz.open(pdf_path)
        img_count = 0
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]
            
            image_blocks = []
            caption_blocks = []
            
            for b in blocks:
                if b["type"] == 1: # Image
                    image_blocks.append(b)
                elif b["type"] == 0: # Text
                    text = reconstruct_text(b)
                    if text and is_caption(text):
                        caption_blocks.append((b["bbox"], text))
            
            for img_b in image_blocks:
                img_bbox = img_b["bbox"]
                best_caption = "Caption not found or not standard format."
                min_dist = float('inf')
                
                # Find the closest caption
                for cap_bbox, cap_text in caption_blocks:
                    dist = calculate_distance(img_bbox, cap_bbox)
                    # Also check horizontal overlap roughly to ensure it's related
                    h_overlap = not (cap_bbox[2] < img_bbox[0] or cap_bbox[0] > img_bbox[2])
                    if h_overlap and dist < min_dist and dist < 300: # Max 300px away
                        min_dist = dist
                        best_caption = cap_text
                
                # Some images are just background or tiny logos
                if img_b.get("width", 0) < 50 or img_b.get("height", 0) < 50:
                    continue
                
                try:
                    # Save image with metadata
                    image_bytes = img_b.get("image")
                    if not image_bytes:
                        continue
                        
                    img = Image.open(io.BytesIO(image_bytes))
                    if img.mode != 'RGB' and img.mode != 'RGBA':
                        img = img.convert('RGB')
                        
                    info = PngImagePlugin.PngInfo()
                    info.add_text("Description", best_caption)
                    info.add_text("Source_Paper", base_name)
                    
                    safe_name = f"img_p{page_num}_{img_count}.png"
                    save_path = os.path.join(out_path, safe_name)
                    
                    img.save(save_path, "PNG", pnginfo=info)
                    img_count += 1
                except Exception as e:
                    print(f"Error guardando imagen en pag {page_num}: {e}")
                    
        print(f"Extraídas {img_count} imágenes con metadatos en: {out_path}")
    except Exception as e:
        print(f"Error procesando PDF {pdf_path}: {e}")

if __name__ == "__main__":
    output_dir = "imagenes_extraidas_metadatos"
    os.makedirs(output_dir, exist_ok=True)
    
    pdfs = glob.glob("papers/*.pdf")
    for pdf in pdfs:
        extract_from_pdf(pdf, output_dir)
