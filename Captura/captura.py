import pyautogui
import time

time.sleep(2)  # espera a tela carregar

# Variáveis para controle da condição de parada
k = 0
n = 50

while True:
    try:
        # Procura a imagem com tolerância (requer Pillow)
        apontamento = pyautogui.locateCenterOnScreen('Captura\img\erro-02.png', confidence=0.7)
    except pyautogui.ImageNotFoundException:
        apontamento = None

    if apontamento is not None:
        pyautogui.moveTo(apontamento, duration=0.2)
        pyautogui.click()
        print(f"Imagem localizada na posição: {apontamento}")
        break

    if k >= n:
        print("Imagem não encontrada na tela após 50 tentativas.")
        break

    print(f"Tentativa {k + 1}...")
    k += 1
    time.sleep(0.5)  # dá mais tempo entre tentativas
