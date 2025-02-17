import PyPDF2
import tabula
import os

caminhoArquivo = r"C:\Users\cs319800\Desktop\AutomaçãoPython\PDF\1162.pdf"

with open(caminhoArquivo,"rb") as arquivo:
    leitor_pdf = PyPDF2.PdfReader(arquivo)
    texto = ""
    for pagina in leitor_pdf.pages:
        texto += pagina.extract_text()
        textoFormatado = ''.join(pagina.extract_text())

        
print(textoFormatado)
