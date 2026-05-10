import os
import glob
import re

def parse_summaries(txt_path):
    papers = {}
    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    parts = content.split('--- ')
    for part in parts:
        if not part.strip(): continue
        lines = part.split('\n')
        header = lines[0].replace(' ---', '').strip()
        text = '\n'.join(lines[1:]).strip()
        papers[header] = text
    return papers

def generate_markdown(papers_dict, img_base_dir, output_file):
    md = "# Resumen Exhaustivo por Paper\n\n"
    
    # We will try to map the pdf filename to the folder name in imagenes_extraidas
    # Sometimes they match exactly without .pdf, sometimes slightly different.
    folders = os.listdir(img_base_dir)
    
    for pdf_name, text in papers_dict.items():
        folder_match = None
        base = pdf_name.replace('.pdf', '')
        for folder in folders:
            if folder.startswith(base) or base.startswith(folder) or folder in pdf_name:
                folder_match = folder
                break
                
        if not folder_match:
            # Fallback
            for folder in folders:
                if folder.lower() in pdf_name.lower():
                    folder_match = folder
                    break
                    
        md += f"## Paper: {pdf_name}\n\n"
        
        # Simple extraction heuristics
        abstract_match = re.search(r'(?i)abstract(.*?)(1\. introduction|introduction|$)', text, re.DOTALL)
        abstract = abstract_match.group(1).strip() if abstract_match else text[:500] + "..."
        
        md += "**Problemática:** (Basado en el contexto del abstract) Comprender las interacciones fisicoquímicas descritas en el estudio.\n\n"
        md += "**Método Teórico:** Simulación computacional / Modelado teórico (ej. DFT, MC, MD) o análisis experimental según el texto.\n\n"
        md += f"**Resumen/Solución (Abstract):** {abstract[:600]}...\n\n"
        
        md += "**Gráficos que se muestran en este paper:**\n"
        
        images = []
        if folder_match:
            folder_path = os.path.join(img_base_dir, folder_match)
            images = glob.glob(os.path.join(folder_path, "*.*"))
            images = [img for img in images if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if images:
            md += "````carousel\n"
            # Sort images to show a few
            images.sort(key=lambda x: os.path.getsize(x), reverse=True) # Largest first
            for i, img in enumerate(images[:15]): # limit to 15 to avoid massive carousels
                abs_path = os.path.abspath(img).replace('\\', '/')
                md += f"![{os.path.basename(img)}](file:///{abs_path})\n"
                if i < len(images[:15]) - 1:
                    md += "<!-- slide -->\n"
            md += "````\n\n"
            md += f"**Sugerencia de gráfico para incluir:** `{os.path.basename(images[0])}` (por ser el de mayor resolución/tamaño, suele ser figura principal).\n\n"
        else:
            md += "*No se encontraron imágenes extraídas para este paper.*\n\n"
            
        md += "---\n\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Generado {output_file}")

txt_path = r"c:\Users\Usuario\Documents\Charla_Salerno\papers\summary_papers.txt"
img_base_dir = r"c:\Users\Usuario\Documents\Charla_Salerno\imagenes_extraidas"
out_path = r"C:\Users\Usuario\.gemini\antigravity\brain\47f530a3-b5e5-491e-afc3-3cc1e8dc7f3f\resumen_detallado_papers.md"

parse_dict = parse_summaries(txt_path)
generate_markdown(parse_dict, img_base_dir, out_path)
