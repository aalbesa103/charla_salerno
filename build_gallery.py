import os
import glob

html = ["<html><head><style>body { font-family: sans-serif; background: #111; color: #fff; } img { max-width: 300px; max-height: 300px; margin: 10px; border: 1px solid #444; } .container { display: flex; flex-wrap: wrap; } .item { margin: 10px; text-align: center; width: 320px; word-wrap: break-word; font-size: 12px; }</style></head><body>"]

base_dir = "imagenes_extraidas"
folders = os.listdir(base_dir)

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        html.append(f"<h2>{folder}</h2><div class='container'>")
        images = []
        for ext in ["*.png", "*.jpeg", "*.jpg"]:
            images.extend(glob.glob(os.path.join(folder_path, ext)))
        
        for img in images:
            html.append(f"<div class='item'><img src='{img}' /><br>{img}</div>")
        html.append("</div><hr>")

html.append("</body></html>")

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("Gallery built at gallery.html")
