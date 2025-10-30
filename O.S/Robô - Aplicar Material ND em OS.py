# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:56:30 2025

@author: CS428185
"""

import pandas as pd
import pyautogui
import time
import keyboard
from datetime import datetime
 
data_atual = datetime.now().strftime('%d/%m/%Y')
 
# Caminho do arquivo Excel
excel_path = 'C:/Users/cs319800/Desktop/O.S/Excel/Materiais ND.xlsx'

# Leitura do arquivo Excel
base = pd.read_excel(excel_path)
 
# Mostra as colunas disponíveis para depuração
print("Colunas disponíveis no arquivo:", base.columns)
 
# Certifique-se de que as colunas necessárias estão corretas
colunas = ['OS', 'Codigo_Sap', 'Quantidade', 'Valor']  # Ajuste para 'OS' em vez de 'Ordem'
 
# Verifica se as colunas existem no DataFrame
for coluna in colunas:
    if coluna not in base.columns:
        raise KeyError(f"A coluna '{coluna}' não foi encontrada no arquivo Excel.")
 
# Seleciona as colunas necessárias
dados = base[colunas]
 
# Obtém as ordens de serviço únicas
ordens_servico = dados['OS'].unique()  # Substituído por 'OS'
 
# Alterna para o programa
pyautogui.hotkey('alt', 'tab')
 
for ordem in ordens_servico:
    # Filtra os materiais relacionados à ordem atual
    materiais_da_ordem = dados[dados['OS'] == ordem]  # Substituído por 'OS'
 
    # Obtém o total de materiais para controle da última iteração
    total_materiais = len(materiais_da_ordem)
    time.sleep(2)
    # Clicar em Procurar
    pyautogui.click(x=292, y=163)
    time.sleep(2)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    # Digitar O.S.
    pyautogui.write(str(ordem))  # Aqui usamos a variável 'ordem'
    # 13 Tabs até o campo de status
    for i in range(13):
        keyboard.press_and_release('tab')
    time.sleep(2)
    # Desmarca as opções de status
    keyboard.press_and_release('space')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('space')
    time.sleep(2)
    # Clicar em OK
    pyautogui.click(x=680, y=674)
    time.sleep(3)
    # Clicar em Pedido de Materiais
    pyautogui.click(x=557, y=544)
    time.sleep(5)
    # Clicar no Lápis
    pyautogui.click(x=1304, y=621)
    time.sleep(10)
    # Clicar em Incluir
    pyautogui.click(x=256, y=221)
    time.sleep(5)
 
    for idx, material in enumerate(materiais_da_ordem.iterrows(), start=1):
        _, material_dados = material
 
        # Preenche informações gerais
        pyautogui.write('15')  # Tipo de peça
        time.sleep(3)
        keyboard.press_and_release('tab')
        pyautogui.write('1700')  # Sistema
        time.sleep(2)
        keyboard.press_and_release('tab')
        pyautogui.write('1780')  # Subsistema
        time.sleep(2)
        keyboard.press_and_release('tab')
        pyautogui.write('1')  # Código Componente
        time.sleep(2)
        keyboard.press_and_release('tab')

        codigo_sap = material_dados['Codigo_Sap']
        quantidade = material_dados['Quantidade']
        valor = material_dados['Valor']
 
        # Insere as informações do material
        pyautogui.write(str(int(codigo_sap)))  # Evita .0
        time.sleep(2)
        keyboard.press_and_release('tab')
        time.sleep(3)
 
        pyautogui.write(str(int(quantidade)))  # Quantidade
        time.sleep(2)
        keyboard.press_and_release('tab')
        time.sleep(3)
 
        pyautogui.write('S11')  # GCM
        time.sleep(2)
        keyboard.press_and_release('tab')
        pyautogui.write('2')  # Prioridade de compra
        time.sleep(2)
        # Finaliza preenchimento do material
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        pyautogui.write('.')
        time.sleep(3)
 
        keyboard.press_and_release('tab')
        time.sleep(3)
        pyautogui.write(str(int(valor))) 
        time.sleep(2)
        keyboard.press_and_release('tab')
        pyautogui.write(data_atual) #DATA DA NECESSIDADE
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        pyautogui.write('MATERIAL ENTRESSAFRA 25-26')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('space')
        time.sleep(3)
        keyboard.press_and_release('tab')
        pyautogui.write('MATERIAL ENTRESSAFRA 25-26')
 
        # Verifica se é o último material da OS
        if idx == total_materiais:
            keyboard.press_and_release('f2')  # Pressiona F2 na última linha
            time.sleep(20)
            keyboard.press_and_release('f3')  # Pressiona F3 na última linha
            time.sleep(20)
        else:
            keyboard.press_and_release('f9')  # Pressiona Enter para confirmar
 
print("Processo finalizado.")