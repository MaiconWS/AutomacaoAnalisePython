import pyautogui as gui
import time
from datetime import datetime

# Entrada do usuário
repeticoes = int(input('Digite a quantidade de O.S: '))

# Data atual formatada
data_atual = datetime.now().strftime('%d/%m/%Y')

# Loop principal
for _ in range(repeticoes):
    # Seleciona a O.S
    gui.press('down')
    time.sleep(1)

    # Copia O.S
    gui.hotkey('ctrl','c')
    time.sleep(0.5)

    # Abre tela de busca
    gui.click(x=291, y=163)
    time.sleep(1.5)

    # Cola O.S
    gui.click(x=731, y=248)
    time.sleep(0.5)
    gui.hotkey('ctrl','v')
    time.sleep(1)

    # Confirma busca
    gui.click(x=636, y=564)
    time.sleep(0.5)
    gui.click(x=636, y=588)
    time.sleep(0.5)
    gui.click(x=679, y=683)
    time.sleep(1)

    # Abre campo de edição
    gui.click(x=609, y=159)
    time.sleep(1)

    # Insere data
    gui.click(x=1032, y=278)
    time.sleep(1)
    gui.write(data_atual)
    time.sleep(0.5)

    # Insere valor "0"
    gui.press('tab')
    time.sleep(0.5)
    gui.press('0')
    time.sleep(0.5)

    # Marca checkbox
    gui.click(x=666, y=464)
    gui.press('space')
    time.sleep(0.5)

    # Retorna à tela inicial
    gui.click(x=120, y=164)
    time.sleep(1.5)

    # Alterna para outra janela
    gui.hotkey('alt', 'tab')
    time.sleep(0.5)
