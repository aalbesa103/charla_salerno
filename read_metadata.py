import os
import glob
from PIL import Image

def verify_metadata(directory):
    png_files = glob.glob(os.path.join(directory, "**", "*.png"), recursive=True)
    if not png_files:
        print(f"No se encontraron imágenes en {directory}")
        return

    print(f"Verificando {len(png_files)} imágenes generadas...\n")
    
    # We will pick up to 5 images that HAVE a valid caption to show
    valid_captions = []
    
    for img_path in png_files:
        try:
            with Image.open(img_path) as img:
                info = img.info
                desc = info.get("Description", "SIN METADATA")
                source = info.get("Source_Paper", "DESCONOCIDO")
                
                if "Caption not found" not in desc and desc != "SIN METADATA":
                    valid_captions.append((img_path, source, desc))
        except Exception as e:
            pass

    print(f"Imágenes con Captions Válidos encontrados: {len(valid_captions)} de {len(png_files)}\n")
    
    for i, (path, source, desc) in enumerate(valid_captions[:10]):
        print(f"--- Imagen {i+1} ---")
        print(f"Archivo: {os.path.basename(path)}")
        print(f"Paper Origen: {source}")
        print(f"Caption incrustado: {desc[:200]}...")
        print("")

if __name__ == "__main__":
    verify_metadata("imagenes_extraidas_metadatos")
