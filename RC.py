import pyautogui as gui
import time


time.sleep(2)
gui.doubleClick(x=1673, y=233)
time.sleep(1)
    
gui.hotkey('ctrl', 'c')
time.sleep(1)

gui.hotkey('alt', 'tab')
time.sleep(1)

gui.click(x=256, y=226)

gui.write('15')
gui.hotkey('tab', 'tab')