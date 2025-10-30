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
    except Exception:
        return None

def monitorar_erro():
    """Thread que monitora a tela constantemente"""
    print("👀 Monitoramento iniciado...")
    while True:
        erro = localizar_imagem(r'Captura\img\erro-02.png', confidence=0.7)
        
        if erro:
            ok = localizar_imagem(r'Captura\img\ok.png', confidence=0.7)
            if ok:
                gui.click(ok)
                time.sleep(0.5)

            cancelar = localizar_imagem(r'Captura\img\erro-03.png', confidence=0.7)
            if cancelar:
                gui.click(cancelar)
                time.sleep(0.5)

            gui.click(x=1348, y=165)
            time.sleep(0.5)

            print(f"⚠️ Erro detectado na posição: {erro}")
            erro_detectado.set()   # Apenas sinaliza o erro

        time.sleep(0.5)  # Ajuste da frequência

def apontamento(tentativas=6, delay=0.5, confidence=0.7, region=None):
    """
    Verifica se apareceu o erro erro04.png e, se sim,
    corrige o código no campo. 
    Retorna True se aplicou correção, False caso contrário.
    """
    for tentativa in range(1, tentativas + 1):
        erro = localizar_imagem(r'Captura\img\erro04.png', confidence=confidence)
        ok = localizar_imagem(r'Captura\img\ok.png', confidence=confidence)
        if erro:
            print(f"⚠️ [apontamento] erro detectado (tentativa {tentativa}) -> corrigindo...")

            # 1) Clica no campo onde está o erro (imagem encontrada)
            gui.click(ok)   # agora usa a posição detectada!
            time.sleep(0.5)

            # 2) Seleciona tudo e apaga
            gui.click(x=155, y=334)
            time.sleep(0.5)
            gui.doubleClick(x=155, y=334)
            time.sleep(0.2)
            gui.press('backspace')
            time.sleep(0.3)

            # 3) Digita o código correto
            gui.write('46999999')
            time.sleep(0.3)
            gui.press('enter')
            time.sleep(0.5)

            # 4) Continua preenchendo os outros campos

            gui.click(x=374, y=335)  # volta para o início
            time.sleep(0.5)
            gui.write('200')
            time.sleep(0.5)
            gui.click(x=1061, y=333)
            time.sleep(0.5)
            gui.write('1')
            time.sleep(0.5)
            gui.click(x=1172, y=335)
            time.sleep(0.5)
            gui.write('1')
            
            time.sleep(0.5)
            gui.click(x=155, y=249)
            
            gui.click(x=1318, y=244)  # volta para o início
            time.sleep(0.5)

            print("✅ Código corrigido para 46999999")
            return True

        # espera e tenta novamente
        time.sleep(delay)

    print("✅ [apontamento] nenhum erro detectado após tentativas")
    return False


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
    gui.write('46999998')
    time.sleep(1)
    
    gui.click(x=372, y=334)
    time.sleep(0.4)
    gui.write('200')
    time.sleep(1)
    if apontamento(tentativas=6, delay=0.4, confidence=0.7):
        time.sleep(0.4)
    gui.click(x=1062, y=329)
    time.sleep(1)
    
    gui.click(x=1075, y=338)
    time.sleep(1)
    gui.write(data_atual)
    time.sleep(1)
    gui.click(x=1118, y=331)
    time.sleep(1)
    gui.write('1')
    time.sleep(1)
    gui.click(x=1264, y=326)
    time.sleep(1)
    gui.write('2')
    time.sleep(1)
    gui.click(x=157, y=246)
    time.sleep(1)
    
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
