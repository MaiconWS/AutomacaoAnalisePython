import pandas as pd
import re

nomePlanilha = input("Digite o nome da planilha: ")
# Carregar o arquivo CSV
arquivo_csv = (f"{nomePlanilha}.csv")  # Substitua pelo nome do seu arquivo
df = pd.read_csv(arquivo_csv, delimiter=";", encoding="utf-8")

# Listas para armazenar os dados extraídos
os = []
descricoes = []
codigos = []
quantidades = []

# Expressão regular para encontrar os códigos de produto
regex = r"\b\d{7}_\d+\b"

def inserir_colunas(descricao, os_value):
    # Extrair os códigos de produto usando a expressão regular
    codigos_encontrados = re.findall(regex, descricao)
    
    for codigo in codigos_encontrados:
        os.append(os_value)  # Adiciona o valor da coluna O.S
        descricoes.append(descricao)
        codigos.append(codigo[:7])  # Extrai os primeiros 7 dígitos do código
        quantidades.append(codigo[8:])  # Extrai a quantidade após o underscore

# Nomes das colunas no CSV
coluna_descricao = "Descrição da ordem"  # Substitua pelo nome correto da coluna de descrição
coluna_os = "O.S"  # Substitua pelo nome correto da coluna O.S

# Iterar sobre as linhas do DataFrame e extrair os dados
for index, row in df.iterrows():
    descricao = str(row[coluna_descricao])  # Converte a descrição para string
    os_value = row[coluna_os]  # Obtém o valor da coluna O.S
    inserir_colunas(descricao, os_value)  # Passa o valor de O.S para a função

# Criar um novo DataFrame com os dados extraídos
new_df = pd.DataFrame(data={
    'O.S': os,
    'Descricao Da Ordem': descricoes,
    'Codigo Produto': codigos,
    'Quantidade de Produto': quantidades
})

# Salvar os dados em um novo arquivo CSV
new_df.to_csv("codigos_2.csv", sep=';', index=False)