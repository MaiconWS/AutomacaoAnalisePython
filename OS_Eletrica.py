import pyautogui as gui
from datetime import datetime, timedelta
import time

data_atual = datetime.now()
nova_data = data_atual + timedelta(days=4)
nova_data_formatada = nova_data.strftime('%d/%m/%Y')

Quantidade = int(input('Quantas O.S serão abertas ? '))

for _ in range(Quantidade):
    
    gui.click(x=437, y=161)
    time.sleep(3)
    gui.click(x=819, y=225)
    time.sleep(0.5)
    gui.write('11')   
    time.sleep(0.5)
    gui.press('j')
    time.sleep(0.5)
    gui.press('enter')
    time.sleep(0.5)
    gui.click(x=665, y=251)
    time.sleep(0.5)
    gui.click(x=1490, y=443)
    time.sleep(1)
    gui.hotkey('ctrl','c')
    time.sleep(0.5)
    gui.click(x=722, y=250)
    time.sleep(0.5)
    gui.hotkey('ctrl','v')
    time.sleep(0.5)
    gui.click(x=408, y=273)
    time.sleep(1)
    gui.hotkey('alt','a')
    time.sleep(0.5)
    gui.press('0')
    time.sleep(0.5)
    gui.click(x=681, y=275)
    time.sleep(0.5)
    gui.write(nova_data_formatada)
    time.sleep(0.5)
    gui.press('0')
    time.sleep(0.5)
    gui.click(x=292, y=298)
    time.sleep(0.5)
    gui.press('3')   
    time.sleep(0.5)
    gui.click(x=296, y=323)
    time.sleep(0.5)
    gui.write('11001')
    time.sleep(0.5)
    gui.click(x=729, y=323)
    time.sleep(0.5)
    gui.write('104')
    time.sleep(0.5)
    gui.click(x=424, y=446)
    time.sleep(0.5)
    gui.write('Elétrica - ')
    time.sleep(0.5)
    gui.hotkey('alt','tab')
    
    for _ in range (6) :
        gui.press('right')
        time.sleep(0.1)
    gui.hotkey('ctrl','c')
    for _ in range (6) :
        gui.press('left')
        time.sleep(0.1)
    time.sleep(0.5)
    gui.click(x=424, y=446)
    time.sleep(0.5)
    gui.hotkey('ctrl','v')
    gui.click(x=118, y=159)
    time.sleep(0.5)
    
    gui.hotkey('alt','tab')
    gui.press('down')
    time.sleep(3)