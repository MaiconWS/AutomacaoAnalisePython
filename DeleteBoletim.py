import pyautogui as gui
import time


gui.hotkey('alt', 'tab')
for _ in range(20):
    gui.click(x=884, y=289)
    time.sleep(0.5)
    gui.click(x=921, y=556)
    time.sleep(0.5)