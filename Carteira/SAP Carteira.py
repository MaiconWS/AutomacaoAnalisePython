import pandas as pd
import re

# Solicita o nome da planilha
nomePlanilha = input("Digite o nome da planilha (sem '.csv'): ").strip()

# Monta o nome do arquivo com extensão
arquivo_csv = f"Carteira/{nomePlanilha}.csv"

try:
    # Tenta carregar o arquivo CSV
    df = pd.read_csv(arquivo_csv, delimiter=";", encoding="utf-8", low_memory=False)
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    exit()

# Listas para armazenar os dados extraídos
os = []
descricoes = []
codigos = []
quantidades = []

# Expressões regulares para encontrar os códigos de produto (ex: 1234567_10 ou 10_1234567)
regex = r"\b\d{7}_\d+\b"
regex1 = r"\b\d+_\d{7}\b"

def inserir_colunas(descricao, os_value):
    codigos_encontrados = re.findall(regex, descricao)
#    codigos_encontrados += re.findall(regex1, descricao)
    for codigo in codigos_encontrados:
        os.append(os_value)
        descricoes.append(descricao)
        codigos.append(codigo.split('_')[0])  # Código antes do "_"
        quantidades.append(codigo.split('_')[1])  # Quantidade depois do "_"

# Nomes das colunas no CSV
coluna_descricao = "Descrição da O.S"
coluna_os = "O.S"


# Verifica se as colunas existem
if coluna_descricao not in df.columns or coluna_os not in df.columns:
    print(f"Erro: As colunas '{coluna_descricao}' ou '{coluna_os}' não foram encontradas no arquivo.")
    print(f"Colunas disponíveis: {list(df.columns)}")
    exit()

# Itera sobre as linhas do DataFrame e extrai os dados
for _, row in df.iterrows():
    descricao = str(row[coluna_descricao])
    os_value = row[coluna_os]
    inserir_colunas(descricao, os_value)

# Cria um novo DataFrame com os dados extraídos
new_df = pd.DataFrame({
    'O.S': os,
    'Descricao Da Ordem': descricoes,
    'Codigo Produto': codigos,
    'Quantidade de Produto': quantidades
})

# Salva os dados em um novo CSV
output_filename = "codigos_2.csv"
new_df.to_csv(output_filename, sep=';', index=False, encoding="utf-8")
print(f"Arquivo '{output_filename}' salvo com sucesso!")
