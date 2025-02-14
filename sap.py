import pandas as pd
import re

# Carregar o arquivo CSV
arquivo_csv = "Gestao2.csv"  # Substitua pelo nome do seu arquivo
df = pd.read_csv(arquivo_csv)
descricoes = []
codigos = []
quantidades = []

# Expressão regular para encontrar os códigos de produto
regex = r"\b\d{7}_\d+\b"

def inserir_colunas(descricao):
    # Extrair os valores numéricos (removendo colchetes e aspas)
    codigos_encontrados = re.findall(regex, descricao)
    
    for codigo in codigos_encontrados:
        descricoes.append(descricao)
        codigos.append(codigo[:7])
        quantidades.append(codigo[8:])

for row in df.iterrows():
    inserir_colunas(str(row[1].iloc[0]))

new_df = pd.DataFrame(data={'Descricao Da Ordem': descricoes,'Codigo Produto': codigos, "Quantidade de Produto": quantidades})

new_df.to_csv("codigos_2.csv",sep=';' , index=False)