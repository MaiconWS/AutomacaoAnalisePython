import pyautogui as gui
import time
from datetime import datetime

#repeticoes = int(input('Digite a quantidade de O.S: '))
data_atual = datetime.now().strftime('%d/%m/%Y')

for _ in range(20):           
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
    
    gui.click(x=615, y=165)
    time.sleep(3)
    
    gui.click(x=996, y=276)
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
    
    gui.click(x=205, y=165)
    time.sleep(1)
    
    gui.hotkey('alt', 'tab')    
