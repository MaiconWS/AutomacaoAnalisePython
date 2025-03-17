import pyautogui as gui
from datetime import datetime
import time

tela = int(input('Digite (1) se sua tela for 1366x768 ou (2) se sua tela for 1920x1080 => '))
data = datetime.now().strftime('%d/%m/%Y')
qtd = int(input('Digite a quantidade de NF: '))
nome = 'Maicon Willian CS319800'

gui.hotkey('alt', 'tab')

#Deixar apenas a pasta com as Nfs abertas 

def resolucao_1(tela):
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
    
def resolucao_2(tela):
    for _ in range(qtd):
        
        gui.press('enter')
        time.sleep(1.5)
        gui.click(x=1034, y=92)
        time.sleep(1)
        gui.click(x=315, y=91)
        time.sleep(1)
        #local da data
        gui.click(x=592, y=191)
        time.sleep(1)
        #alterar a cor
        gui.click(x=609, y=232)
        time.sleep(1)
        #escolhendo a cor
        gui.click(x=604, y=399)
        time.sleep(1)
        #onde escrever a data
        gui.click(x=630, y=191)
        time.sleep(1)
        #escreve a data
        gui.write(data)
        time.sleep(1)
        #onde escrever o nome
        gui.click(x=838, y=191)
        time.sleep(0.5)
        #onde escrever o nome
        gui.click(x=838, y=191)
        time.sleep(1.5)
        #escreve o nome
        for letra in nome:
            gui.write(letra)
            #time.sleep(0.1)
        time.sleep(0.5)
        gui.click(x=1005, y=274)
        time.sleep(0.5)
        #salva
        gui.click(x=1759, y=91)
        time.sleep(1)
        gui.hotkey('alt', 'tab')
        time.sleep(1)
        gui.press('down')
        time.sleep(1)
        
if tela == 1:
    resolucao_1(qtd)
elif tela == 2:
    resolucao_2(qtd)
else:
    print("Opção inválida! Escolha 1 ou 2.")