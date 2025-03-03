import pyautogui as gui
from datetime import datetime
import time


data = datetime.now().strftime('%d/%m/%Y')
qtd = int(input('Digite a quantidade de NF: '))
nome = 'Maicon Willian CS319800'

gui.hotkey('alt', 'tab')

#Deixar apenas a pasta com as Nfs abertas 

for _ in range(qtd):
    
    gui.press('enter')
    time.sleep(1.5)
    gui.click(x=866, y=87)
    time.sleep(1)
    gui.click(x=314, y=89)
    time.sleep(1)
    gui.click(x=405, y=190)
    time.sleep(1)
    gui.click(x=428, y=242)
    time.sleep(1)
    gui.click(x=404, y=392)
    time.sleep(1)
    gui.click(x=419, y=188)
    time.sleep(1)
    gui.write(data)
    time.sleep(1)
    gui.click(x=647, y=192)
    time.sleep(0.5)
    gui.click(x=647, y=192)
    time.sleep(1.5)
    for letra in nome:
        gui.write(letra)
        #time.sleep(0.1)
    time.sleep(0.5)
    gui.click(x=1005, y=274)
    time.sleep(0.5)
    gui.click(x=1272, y=92)
    time.sleep(1)
    gui.hotkey('alt', 'tab')
    time.sleep(1)
    gui.press('down')
    time.sleep(1)