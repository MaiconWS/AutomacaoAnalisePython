import pyautogui as gui
import time
from datetime import datetime

repeticoes = int(input('Digite a quantidade de O.S: '))
data_atual = datetime.now().strftime('%d/%m/%Y')
apontada = input("As O.S estão apontadas ? Responda com (Sim) ou (Não) => ")


gui.hotkey('alt', 'tab')
for _ in range(repeticoes):

    time.sleep(1)
    
    gui.press('down')
    time.sleep(1)
    
    gui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    gui.click(x=291, y=163)
    time.sleep(1.5)
    
    gui.click(x=731, y=248)
    time.sleep(0.5) 

    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    gui.click(x=636, y=564)
    time.sleep(0.5)
    gui.click(x=636, y=588)
    time.sleep(0.5)
    gui.click(x=679, y=683)


    time.sleep(1)

    
    if apontada == "Não":
        #APONTAR
        gui.click(x=1304, y=634)
        time.sleep(1)
         #gui.press('f9')
        gui.click(x=158, y=244)
        gui.press('enter')

        gui.click(x=664, y=483)
        time.sleep(1)

        gui.press('tab')
        gui.click(x=196, y=250)
        time.sleep(1)

        gui.press('tab')
        gui.click(x=341, y=332)
        time.sleep(0.5)

        gui.press('1')
        #time.sleep(0.5)
    
    
        gui.press('tab')
        gui.click(x=1107, y=335)
        time.sleep(0.5)

        gui.press('1')
        # time.sleep(0.5)
    
    
        gui.press('tab')
        gui.click(x=1233, y=334)
        time.sleep(0.5)

        gui.press('1')
        #time.sleep(0.5)

        #gui.press('f2')
        gui.click(x=158, y=244)
        time.sleep(1.5)

        gui.click(x=1322, y=250)
        time.sleep(1)

        #encerrar
    
        gui.click(x=609, y=159)
        time.sleep(1)
    
        gui.click(x=1032, y=278)
        time.sleep(1)
    
        gui.write(data_atual)
        time.sleep(0.5)
    
        gui.press('tab')
        time.sleep(0.5)
    
        gui.press('0')
        time.sleep(0.5)
    
        gui.press('space')
        time.sleep(0.5)
    
        gui.click(x=120, y=164)
        time.sleep(1.5)
        gui.hotkey('alt', 'tab')
        time.sleep(0.5)
        
    else:
        gui.click(x=609, y=159)
        time.sleep(1)
    
        gui.click(x=1032, y=278)
        time.sleep(1)
    
        gui.write(data_atual)
        time.sleep(0.5)
    
        gui.press('tab')
        time.sleep(0.5)
    
        gui.press('0')
        time.sleep(0.5)
    
        gui.press('space')
        time.sleep(0.5)
    
        gui.click(x=120, y=164)
        time.sleep(1.5)
        gui.hotkey('alt', 'tab')
        time.sleep(0.5)