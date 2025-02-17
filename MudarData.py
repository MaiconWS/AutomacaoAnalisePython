import pyautogui as gui
import time
from datetime import datetime

#dataOS = str(input('Digite a data da O.S: '))
repeticoesAprovisionamento = int(input('Digite a quantidade de O.S em aprovisionamento: '))
repeticoesLiberado = int(input('Digite a quantidade de O.S em Liberada para a programação: '))

gui.hotkey('alt', 'tab')


for _ in range(repeticoesAprovisionamento):  
              
    time.sleep(2)
    
    gui.press('down')
    time.sleep(1)
    
    
    gui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    gui.click(x=291, y=163)
    time.sleep(2)
    
    gui.click(x=731, y=248)
    time.sleep(1)
    
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    gui.click(x=860, y=589)
    time.sleep(0.03)
    
    gui.click(x=837, y=610)
    time.sleep(0.03)
    
    gui.click(x=841, y=636)
    time.sleep(0.03)
    
    gui.click(x=688, y=673)
    time.sleep(0.03)
    
    gui.click(x=615, y=165)
    time.sleep(3)
    
    gui.click(x=1131, y=224)
    time.sleep(2)
    
    gui.press('backspace')
    gui.press('a')
    
    gui.click(x=118, y=163)
    time.sleep(1)
    gui.click(x=613, y=166)
    time.sleep(1)
    gui.click(x=682, y=275)
    time.sleep(1)
    gui.click(x=614, y=168)
    time.sleep(2)
    
    i = 0
    while i < 9:
        gui.press('backspace')
        i+= 1
        time.sleep(0.2)
        
    time.sleep(2)
    #gui.write(dataOS)
    gui.hotkey('alt', 'tab')
    time.sleep(1)
    for _ in range(4):
        gui.press('right')
        time.sleep(0.2)
    
    gui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    for _ in range(4):
        gui.press('left')
        time.sleep(0.2)
        
    time.sleep(1)    
    gui.hotkey('alt', 'tab')
    time.sleep(1)
    gui.hotkey('ctrl', 'v')
    
    time.sleep(1)
    gui.click(x=115, y=167)
    time.sleep(1)
    
    gui.click(x=615, y=169)
    time.sleep(2)
    
    gui.click(x=1131, y=224)
    time.sleep(2)
    gui.press('backspace')
    gui.press('v')
    time.sleep(1)
    
    gui.click(x=114, y=166)
    time.sleep(1)
    
    gui.hotkey('alt', 'tab')
    
    
for _ in range(repeticoesLiberado):  
              
    time.sleep(2)
    
    gui.press('down')
    time.sleep(1)
    
    
    gui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    gui.click(x=291, y=163)
    time.sleep(2)
    
    gui.click(x=731, y=248)
    time.sleep(1)
    
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    gui.click(x=860, y=589)
    time.sleep(0.03)
    
    gui.click(x=837, y=610)
    time.sleep(0.03)
    
    gui.click(x=841, y=636)
    time.sleep(0.03)
    
    gui.click(x=688, y=673)
    time.sleep(0.03)
    
    gui.click(x=615, y=165)
    time.sleep(3)
    
    gui.click(x=1131, y=224)
    time.sleep(2)
    
    gui.press('backspace')
    gui.press('a')
    
    gui.click(x=118, y=163)
    time.sleep(1)
    gui.click(x=613, y=166)
    time.sleep(1)
    gui.click(x=682, y=275)
    time.sleep(1)
    gui.click(x=614, y=168)
    time.sleep(2)
    
    i = 0
    while i < 9:
        gui.press('backspace')
        i+= 1
        time.sleep(0.2)
        
    time.sleep(2)
    #gui.write(dataOS)
    gui.hotkey('alt', 'tab')
    time.sleep(1)
    for _ in range(4):
        gui.press('right')
        time.sleep(0.2)
    
    gui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    for _ in range(4):
        gui.press('left')
        time.sleep(0.2)
        
    time.sleep(1)    
    gui.hotkey('alt', 'tab')
    time.sleep(1)
    gui.hotkey('ctrl', 'v')
    
    time.sleep(1)
    gui.click(x=115, y=167)
    time.sleep(1)
    
    gui.click(x=615, y=169)
    time.sleep(2)
    
    gui.click(x=1131, y=224)
    time.sleep(2)
    gui.press('backspace')
    gui.press('l')
    time.sleep(1)
    
    gui.click(x=114, y=166)
    time.sleep(1)
    
    gui.hotkey('alt', 'tab')