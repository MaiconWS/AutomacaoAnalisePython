import pyautogui as gui
from datetime import datetime
import threading
import time

# Configurações
repeticoes = int(input('Digite a quantidade de O.S: '))
data_atual = datetime.now().strftime('%d/%m/%Y')
erro_detectado = threading.Event()  # Evento para sinalizar erro

def localizar_imagem(caminho, confidence=0.7):
    """Tenta localizar uma imagem na tela e retorna sua posição ou None"""
    try:
        posicao = gui.locateCenterOnScreen(caminho, confidence=confidence)
        if posicao:
            print(f"📸 Imagem localizada: {caminho} na posição {posicao}")
        return posicao
    except gui.ImageNotFoundException as e:
        print(f"❌ Imagem não encontrada: {caminho} (highest confidence = {getattr(e, 'confidence', 'N/A')})")
        return None

def monitorar_erro():
    """Thread que monitora a tela constantemente"""
    print("👀 Monitoramento iniciado...")
    while not erro_detectado.is_set():
        erro = localizar_imagem('Captura\img\erro-02.png', confidence=0.7)
        
        if erro:
            ok = gui.locateCenterOnScreen('Captura\img\ok.png', confidence=0.7)
            gui.click(ok)
            time.sleep(0.5)
            cancelar = gui.locateCenterOnScreen('Captura\img\erro-03.png', confidence=0.7)
            gui.click(cancelar)
            time.sleep(0.5)
            gui.click(x=1348, y=165)
            time.sleep(0.5)
            print(f"⚠️ Erro detectado na posição: {erro}")
            erro_detectado.set()
        time.sleep(0.5)  # Ajuste a frequência de checagem se necessário

def bloco_nao_apontadas():
    """Executa o BLOCO PARA O.S NÃO APONTADAS"""
    print("🔄 Executando BLOCO PARA O.S NÃO APONTADAS")
    gui.click(x=1304, y=634)
    time.sleep(1)
    gui.click(x=158, y=244)
    gui.press('enter')

    gui.click(x=664, y=483)
    time.sleep(1)

    gui.press('tab')
    gui.click(x=196, y=250)
    time.sleep(1)

    gui.press('tab')
    gui.click(x=341, y=332)
    time.sleep(0.5)

    gui.press('1')
    gui.press('tab')
    gui.click(x=1107, y=335)
    time.sleep(0.5)
    gui.press('1')
    gui.press('tab')
    gui.click(x=1233, y=334)
    time.sleep(0.5)
    gui.press('1')

    gui.click(x=158, y=244)
    time.sleep(1.5)

    gui.click(x=1322, y=250)
    time.sleep(1)

    # Encerrar
    gui.click(x=609, y=159)
    time.sleep(1)
    gui.click(x=1032, y=278)
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
    gui.hotkey('alt', 'tab')
    time.sleep(0.5)

def bloco_ja_apontadas():
    """Executa o BLOCO PARA O.S JÁ APONTADAS com monitoramento"""
    print("✅ Executando BLOCO PARA O.S JÁ APONTADAS")
    gui.click(x=609, y=159)
    if erro_detectado.is_set(): return False
    time.sleep(1)

    gui.click(x=1032, y=278)
    if erro_detectado.is_set(): return False
    time.sleep(1)

    gui.write(data_atual)
    if erro_detectado.is_set(): return False
    time.sleep(0.5)

    gui.press('tab')
    if erro_detectado.is_set(): return False
    time.sleep(0.5)

    gui.press('0')
    if erro_detectado.is_set(): return False
    time.sleep(0.5)

    gui.press('space')
    if erro_detectado.is_set(): return False
    time.sleep(0.5)

    gui.click(x=120, y=164)
    if erro_detectado.is_set(): return False
    time.sleep(1.5)

    gui.hotkey('alt', 'tab')
    time.sleep(0.5)
    return True  # Tudo ok

# 🔥 Inicia thread de monitoramento
monitor_thread = threading.Thread(target=monitorar_erro, daemon=True)
monitor_thread.start()

# 🔁 Loop principal
gui.hotkey('alt', 'tab')
for _ in range(repeticoes):
    if erro_detectado.is_set():
        bloco_nao_apontadas()
        erro_detectado.clear()
        continue  # Pula para próxima repetição

    try:
        time.sleep(1)

        gui.press('down')
        time.sleep(1)

        gui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        gui.click(x=291, y=163)
        time.sleep(1.5)

        gui.click(x=731, y=248)
        time.sleep(0.5)

        gui.hotkey('ctrl', 'v')
        time.sleep(1)

        gui.click(x=636, y=564)
        time.sleep(0.5)
        gui.click(x=636, y=588)
        time.sleep(0.5)
        gui.click(x=679, y=683)
        time.sleep(1)

        # Tenta BLOCO JÁ APONTADAS e cai para NÃO se detectar erro
        if not bloco_ja_apontadas():
            raise Exception("Interrupção: erro detectado pelo monitoramento")

    except Exception as e:
        print(f"⚠️ Interrompido: {e}")
        bloco_nao_apontadas()
        erro_detectado.clear()  # Limpa o evento para próximos ciclos