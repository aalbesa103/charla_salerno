import os
import glob
import json
import re
from PIL import Image

def get_image_caption(img_path):
    try:
        with Image.open(img_path) as img:
            caption = img.info.get("Description", "Caption no encontrado.")
            # Limpiar espacios múltiples y caracteres raros
            caption = re.sub(r'\s+', ' ', caption).strip()
            return caption
    except:
        return "Error leyendo metadatos."

def build_encyclopedia(context_json, img_dir, output_md):
    with open(context_json, 'r', encoding='utf-8') as f:
        contexts = json.load(f)
    
    md_content = "# ENCICLOPEDIA EXHAUSTIVA DE GRÁFICOS CIENTÍFICOS (CORREGIDA)\n\n"
    md_content += "Este documento es el catálogo definitivo de todos los resultados visuales de tus papers.\n\n"
    
    # Ordenar papers alfabéticamente para consistencia
    sorted_papers = sorted(contexts.keys())
    
    for paper_name in sorted_papers:
        figures = contexts[paper_name]
        paper_base = paper_name.replace('.pdf', '')
        md_content += f"## Paper: {paper_name}\n\n"
        
        paper_img_dir = os.path.join(img_dir, paper_base)
        img_files = glob.glob(os.path.join(paper_img_dir, "*.png")) if os.path.exists(paper_img_dir) else []
        
        for fig_data in figures:
            fig_num = str(fig_data["figure_num"])
            md_content += f"### FIGURA {fig_num}\n\n"
            
            associated_img = None
            # Búsqueda robusta con regex: "Fig(ure)? [spaces] num"
            # Buscamos que el número esté rodeado de límites de palabra o puntuación
            pattern = re.compile(rf"(fig|figure)\.?\s*{fig_num}(\s|[.:,;]|$)", re.IGNORECASE)
            
            for img_path in img_files:
                caption = get_image_caption(img_path)
                if pattern.search(caption):
                    associated_img = img_path
                    break
            
            if associated_img:
                # Usar ruta relativa para el markdown
                rel_path = os.path.relpath(associated_img, start=os.path.dirname(output_md)).replace('\\', '/')
                md_content += f"![Fig {fig_num}]({rel_path})\n\n"
                md_content += f"**Caption Original:**\n> {get_image_caption(associated_img)}\n\n"
            else:
                md_content += f"*Imagen no vinculada automáticamente.* (Revisar en carpeta `{paper_base}/`)\n\n"
            
            md_content += "**Contexto y Discusión en el Texto:**\n"
            for ctx in fig_data["contexts"]:
                clean_ctx = re.sub(r'\s+', ' ', ctx).strip()
                # Escapar markdown básico para evitar que rompa el formato
                clean_ctx = clean_ctx.replace('*', '\\*').replace('_', '\\_')
                md_content += f"- {clean_ctx}\n\n"
            
            md_content += "---\n\n"
            
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Enciclopedia corregida generada en: {output_md}")

if __name__ == "__main__":
    build_encyclopedia("figure_contexts.json", "imagenes_extraidas_metadatos", "ENCICLOPEDIA_GRAFICOS.md")
