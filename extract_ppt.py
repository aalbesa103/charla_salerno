import sys
import os

try:
    import win32com.client
    def extract_text(filepath):
        print(f"Extracting: {filepath}")
        Application = win32com.client.Dispatch("PowerPoint.Application")
        Application.Visible = True
        Presentation = Application.Presentations.Open(os.path.abspath(filepath), WithWindow=False)
        text = []
        for slide in Presentation.Slides:
            for shape in slide.Shapes:
                if shape.HasTextFrame:
                    if shape.TextFrame.HasText:
                        text.append(shape.TextFrame.TextRange.Text)
        Presentation.Close()
        # Application.Quit() # Don't quit to avoid closing user's PPT if open
        with open(filepath + ".txt", "w", encoding="utf-8") as f:
            f.write("\n\n".join(text))
        print("Done.")

    extract_text("Charla_Tesinistas.ppt")
    extract_text("Simulaciones Monte Carlo aplicadas al estudio de fenómenos (6).ppt")
    extract_text("simulaciones Monte Carlo.pptx")

except Exception as e:
    print(f"Error using win32com: {e}")
