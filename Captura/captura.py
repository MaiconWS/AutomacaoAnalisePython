import pyautogui
import time

time.sleep(2)  # espera a tela carregar

# Variáveis para controle da condição de parada
k = 0
n = 50

while True:
    try:
        # Procura a imagem com tolerância (requer Pillow)
        img = pyautogui.locateCenterOnScreen('ok.png', confidence=0.6)
    except pyautogui.ImageNotFoundException:
        img = None

    if img is not None:
        pyautogui.moveTo(img, duration=0.2)
        pyautogui.doubleClick()
        print(f"Imagem localizada na posição: {img}")
        break

    if k >= n:
        print("Imagem não encontrada na tela após 50 tentativas.")
        break

    print(f"Tentativa {k + 1}...")
    k += 1
    time.sleep(0.5)  # dá mais tempo entre tentativas
