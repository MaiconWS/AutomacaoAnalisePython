# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import pandas as pd
import pyautogui
import time
import keyboard
 
# Caminho do arquivo Excel
excel_path = "C:/Users/cs319800/Desktop/O.S/Excel/Materiais VB.xlsx"

 
# Leitura do arquivo Excel
base = pd.read_excel(excel_path)
 
# Mostra as colunas disponíveis para depuração
print("Colunas disponíveis no arquivo:", base.columns)
# Certifique-se de que as colunas necessárias estão corretas
colunas = ['OS', 'Codigo_Sap', 'Quantidade']  # Ajuste para 'OS' em vez de 'Ordem'
 
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
    time.sleep(10)
    # Clicar em Procurar
    pyautogui.click(x=292, y=163)
    time.sleep(10)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    # Digitar O.S.
    pyautogui.write(str(ordem))  # Aqui usamos a variável 'ordem'
    # 13 Tabs até o campo de status
    for i in range(13):
        keyboard.press_and_release('tab')
    time.sleep(20)
    # Desmarca as opções de status
    keyboard.press_and_release('space')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('space')
    time.sleep(10)
    # Clicar em OK
    pyautogui.click(x=680, y=674)
    time.sleep(20)
    # Clicar em Pedido de Materiais
    pyautogui.click(x=557, y=544)
    time.sleep(20)
    # Clicar no Lápis
    pyautogui.click(x=1304, y=621)
    time.sleep(30)
    # Clicar em Incluir
    pyautogui.click(x=256, y=221)
    time.sleep(10)
 
    for idx, material in enumerate(materiais_da_ordem.iterrows(), start=1):
        _, material_dados = material
 
        # Preenche informações gerais
        pyautogui.write('10')  # Tipo de peça #10 = reserva
        time.sleep(1)
        keyboard.press_and_release('tab')
        pyautogui.write('1700')  # Sistema
        keyboard.press_and_release('tab')
        pyautogui.write('1780')  # Subsistema
        keyboard.press_and_release('tab')
        pyautogui.write('1')  # Código Componente
        keyboard.press_and_release('tab')
        codigo_sap = material_dados['Codigo_Sap']
        quantidade = material_dados['Quantidade']
        # Insere as informações do material
        pyautogui.write(str(codigo_sap))  # Código SAP
        keyboard.press_and_release('tab')
        time.sleep(1)
        pyautogui.write(str(quantidade))  # Quantidade
        keyboard.press_and_release('tab')
        time.sleep(1)
    
 
        # Verifica se é o último material da OS
        if idx == total_materiais:
            keyboard.press_and_release('f2')  # Pressiona F2 na última linha
            time.sleep(30)
            keyboard.press_and_release('f3')  # Pressiona F3 na última linha
            time.sleep(30)
        else:
            keyboard.press_and_release('f9')  # Pressiona Enter para confirmar
 
print("Processo finalizado.")
