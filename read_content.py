import os
from PyPDF2 import PdfReader
import pandas as pd

# ---------- Custom Error ----------
class EmptyFileError(Exception):
    pass

def read_text(path):
    
               with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if not content.strip():
                         raise EmptyFileError
                    return content

def read_pdf(path):
    if os.path.getsize(path) == 0:
        raise EmptyFileError

    reader = PdfReader(path)
    content = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            content += text

    if not content.strip():
        raise EmptyFileError

    return content



def read_excel(path):
    df = pd.read_excel(path)

    if df.empty:
        raise EmptyFileError

    content = df.to_string(index=False)
    return content
def read_content(path):     
          
          if not os.path.exists(path):
                raise FileNotFoundError("file does not exit")
          
          if path.endswith(".txt"):
                 return read_text(path)
          
          
          elif path.endswith(".pdf"):
                  return read_pdf(path)
               
          elif path.endswith(".xlsx"):
                  return read_excel(path)   
          else:
                    raise ValueError("File not found") 