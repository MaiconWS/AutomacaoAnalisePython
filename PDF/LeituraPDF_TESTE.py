import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    return text

def find_information(text):
    # Expressão regular para NF e FT (números de 6 a 7 dígitos)
    nf_pattern = r'NF\s*(\d{6})'  # Captura números após "NF"
    ft_pattern = r'FT[:\s]*(\d{5})'  # Captura números após "FT"
    pattern = r'\b\d{7}\b'

    nf_number = re.search(nf_pattern, text)
    ft_number = re.search(ft_pattern, text)
    pattern = re.findall(pattern, text)

    return {
        "NF": nf_number.group(1) if nf_number else None,
        "FT": ft_number.group(1) if ft_number else None,
        "Cod.": pattern
    }

# Caminho do PDF
pdf_path = r"C:\Users\cs319800\Desktop\AutomaçãoPython\PDF\1162.pdf"

# Extração de texto e busca de informações
pdf_text = extract_text_from_pdf(pdf_path)
info = find_information(pdf_text)

# Exibir resultados
print(f"NF Encontrada: {info['NF']}")
print(f"FT Encontrada: {info['FT']}")
print(f"Codigos Encontrados: {info['Cod.']}")
