import os
import glob
import fitz  # PyMuPDF
import re
import json

def extract_full_text_with_positions(doc):
    """Extrae el texto completo del documento manteniendo una estructura de párrafos."""
    full_text = []
    for page in doc:
        blocks = page.get_text("blocks")
        for b in blocks:
            if b[6] == 0: # Texto
                full_text.append(b[4].replace('\n', ' ').strip())
    return full_text

def find_figure_mentions(text_blocks, fig_num):
    """Busca menciones de una figura específica y devuelve el contexto."""
    # Patrones comunes: Figure 1, Fig. 1, Fig 1, etc.
    patterns = [
        rf"(?i)Figure\s+{fig_num}\b",
        rf"(?i)Fig\.\s+{fig_num}\b",
        rf"(?i)Fig\s+{fig_num}\b"
    ]
    
    contexts = []
    for i, block in enumerate(text_blocks):
        for pattern in patterns:
            if re.search(pattern, block):
                # Tomamos el bloque actual y quizás el anterior/siguiente para más contexto
                start = max(0, i - 1)
                end = min(len(text_blocks), i + 2)
                context = " ".join(text_blocks[start:end])
                contexts.append(context)
                break
    return list(set(contexts)) # Eliminar duplicados exactos

def process_papers(papers_dir, output_json):
    results = {}
    pdfs = glob.glob(os.path.join(papers_dir, "*.pdf"))
    
    for pdf_path in pdfs:
        base_name = os.path.basename(pdf_path)
        print(f"Analizando contexto en: {base_name}")
        try:
            doc = fitz.open(pdf_path)
            text_blocks = extract_full_text_with_positions(doc)
            
            paper_data = []
            
            # Buscaremos hasta 20 figuras por paper por si acaso
            for i in range(1, 21):
                mentions = find_figure_mentions(text_blocks, i)
                if mentions:
                    paper_data.append({
                        "figure_num": i,
                        "contexts": mentions
                    })
            
            results[base_name] = paper_data
            doc.close()
        except Exception as e:
            print(f"Error procesando {base_name}: {e}")
            
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"Análisis completado. Resultados en {output_json}")

if __name__ == "__main__":
    process_papers("papers", "figure_contexts.json")
