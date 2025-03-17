import pyautogui
import json
import time

coordenadas = []

print("Clique nos pontos que deseja salvar. Pressione 'q' para sair.")

while True:
    try:
        x, y = pyautogui.position()  # Pega posição atual do mouse
        print(f"Coordenada salva: ({x}, {y})")
        coordenadas.append((x, y))
        time.sleep(2)  # Pequeno delay para evitar capturas contínuas
    except KeyboardInterrupt:
        break  # Sai do loop ao pressionar Ctrl+C

# Salva as coordenadas em um arquivo JSON
with open("Captura/coordenadas.json", "w") as arquivo:
    json.dump(coordenadas, arquivo)

print("Coordenadas salvas com sucesso!")
