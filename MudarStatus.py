import pyautogui as gui
import time

repeticoes = int(input('Digite a quantidade de O.S: '))

gui.hotkey('alt', 'tab')

for _ in range(repeticoes):  

    time.sleep(1)
    
    gui.press('down')
    time.sleep(1)
    
    
    gui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    gui.click(x=291, y=163)
    time.sleep(1)
    
    gui.click(x=731, y=248)
    time.sleep(1)
    
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    gui.click(x=860, y=589)
    time.sleep(0.3)
    
    gui.click(x=837, y=610)
    time.sleep(0.3)
    
    gui.click(x=841, y=636)
    time.sleep(0.3)
    
    gui.click(x=688, y=673)
    time.sleep(0.3)
    
    gui.click(x=611, y=158)
    time.sleep(1.5)

    gui.click(x=1133, y=223)
    time.sleep(1)
    
    gui.press('backspace')
    time.sleep(1)
    
    gui.press('a')
    time.sleep(1.5)
    
    gui.click(x=117, y=162)
    time.sleep(1)
    
    gui.click(x=651, y=460)
    time.sleep(1)
    
    gui.hotkey('alt', 'tab')
