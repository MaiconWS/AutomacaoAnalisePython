import pyautogui as gui
import time

img = "Erro.png"

try:
    localiza = gui.locateCenterOnScreen(img, confidence=0.5)
    print(localiza)
    
except Exception as erro:
    for _ in range(3):
        gui.click(x=488, y=281)
        time.sleep(0.5)
        gui.click(x=560, y=553)
        time.sleep(0.5)


    