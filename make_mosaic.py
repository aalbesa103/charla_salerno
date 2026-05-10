import os
import glob
from PIL import Image, ImageDraw, ImageFont

def create_mosaic(input_dir, output_file, max_images=100, cols=8):
    # Recursively find all images in this directory and subdirectories
    files = []
    for root, dirs, filenames in os.walk(input_dir):
        # skip presentation folders
        if "Charla_" in root or "Simulaciones" in root or "simulaciones" in root:
            continue
        for f in filenames:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                files.append(os.path.join(root, f))
                
    images = files[:max_images]
    
    if not images:
        print("No images found.")
        return

    thumb_w, thumb_h = 300, 300
    rows = (len(images) + cols - 1) // cols
    
    mosaic_w = cols * thumb_w
    mosaic_h = rows * thumb_h
    
    mosaic = Image.new('RGB', (mosaic_w, mosaic_h), (255, 255, 255))
    
    for i, img_path in enumerate(images):
        try:
            with Image.open(img_path) as img:
                img.thumbnail((thumb_w, thumb_h))
                thumb_bg = Image.new('RGB', (thumb_w, thumb_h), (240, 240, 240))
                
                paste_x = (thumb_w - img.width) // 2
                paste_y = (thumb_h - img.height) // 2
                thumb_bg.paste(img, (paste_x, paste_y))
                
                draw = ImageDraw.Draw(thumb_bg)
                # Show parent folder + filename
                parent = os.path.basename(os.path.dirname(img_path))
                filename = os.path.basename(img_path)
                label = f"{parent[:15]}/{filename}"
                
                draw.rectangle([0, 0, thumb_w, 20], fill=(0,0,0))
                draw.text((5, 2), label, fill=(255,255,255))
                
                row = i // cols
                col = i % cols
                mosaic.paste(thumb_bg, (col * thumb_w, row * thumb_h))
        except Exception as e:
            print(f"Failed {img_path}: {e}")
            
    mosaic.save(output_file)
    print(f"Mosaic saved to {output_file}")

create_mosaic("imagenes_extraidas", r"C:\Users\Usuario\.gemini\antigravity\brain\47f530a3-b5e5-491e-afc3-3cc1e8dc7f3f\browser\mosaic_papers.png", max_images=200, cols=10)
