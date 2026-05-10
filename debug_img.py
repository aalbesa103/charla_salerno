import os
import glob
from PIL import Image

paper_dir = "imagenes_extraidas_metadatos/1-s2_0-S000926141630104X-main"
print(f"Checking images in {paper_dir}:")
for f in glob.glob(os.path.join(paper_dir, "*.png")):
    try:
        with Image.open(f) as img:
            desc = img.info.get("Description", "NO DESCRIPTION")
            print(f"- {os.path.basename(f)}: {desc[:150]}...")
    except Exception as e:
        print(f"- Error in {f}: {e}")
