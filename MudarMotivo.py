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
    
    gui.click(x=637, y=563)
    time.sleep(0.3)
    
    gui.click(x=639, y=589)
    time.sleep(0.3)

    gui.click(x=688, y=673)
    time.sleep(0.3)
    
    gui.click(x=611, y=158)
    time.sleep(1.5)

    gui.click(x=299, y=300)
    time.sleep(1)
    
    gui.press('backspace')
    time.sleep(0.5)  
    
    gui.write('4')
    time.sleep(0.5)
    
    gui.click(x=117, y=162)
    time.sleep(1)
    
    gui.hotkey('alt', 'tab')
