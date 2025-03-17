import csv
import re
import os
from PyPDF2 import PdfReader

# Diretório contendo os PDFs
pdf_directory = "ORC_FJ"

# Lista de arquivos PDF no diretório
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]

# Nome do arquivo CSV (salvo no mesmo local do código)
csv_file = os.path.join(os.getcwd(), "ORC_FJ/dados_extraidos.csv")

# Expressões regulares para capturar os valores
patterns = {
    "OS": r"OS\s*(\d+)",
    "FT": r"FT:\s*(\d+)",
    "NF": r"NF\s*(\d+)|NF(\d+)",
    "DATA": r"DATA[: ](\d{2}/\d{2}/\d{4})",
    "ORCAMENTO": r"ORCAM\s*ENTO\s*(\d+)",
    "TOTAL": r"Total[: ]+([\d.,]+)"  # Captura todas as ocorrências de "Total"
}

# Criar e escrever no CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Arquivo", "OS", "FT", "NF", "DATA", "ORCAMENTO", "TOTAL"])  # Cabeçalho

    for pdf_name in pdf_files:
        pdf_path = os.path.join(pdf_directory, pdf_name)
        
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
        
        # Extraindo os valores ou definindo "N/A" caso não encontrados
        dados = [pdf_name]  # Adiciona o nome do arquivo
        for key, pattern in patterns.items():
            if key == "TOTAL":
                matches = re.findall(pattern, text)  # Captura todas as ocorrências de "Total"
                value = matches[-1] if matches else "N/A"  # Pega a última ocorrência
            else:
                match = re.search(pattern, text)
                value = match.group(1) if match else "N/A"
            dados.append(value)
        
        writer.writerow(dados)  # Escrevendo os dados no CSV

print(f"Arquivo {csv_file} gerado com sucesso!")