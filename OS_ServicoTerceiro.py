import pyautogui as gui
from datetime import datetime, timedelta
import time

data_atual = datetime.now()
nova_data = data_atual + timedelta(days=4)
nova_data_formatada = nova_data.strftime('%d/%m/%Y')

tela = int(input('Digite (1) se sua tela for 1366x768 ou (2) se sua tela for 1920x1080 => '))
Quantidade = int(input('Quantas O.S serão abertas ? '))

#para resolução 1366x768
def resolucao_1(tela):
    for _ in range(Quantidade):
        #incluir
        gui.click(x=437, y=161)
        time.sleep(3)
        #Classe manutenção
        gui.doubleClick(x=434, y=226)
        time.sleep(1)
        gui.press('delete')
        gui.press('backspace')
        time.sleep(1)
        gui.write('t')
        gui.click(x=819, y=225)
        time.sleep(0.5)
        gui.write('11')   
        time.sleep(0.5)
        #status
        gui.press('j')
        time.sleep(0.5)
        gui.press('enter')
        time.sleep(0.5)
        gui.click(x=665, y=251)
        time.sleep(0.5)
        gui.click(x=1490, y=443)
        time.sleep(1)
                
        #Copia frota na planilha
        gui.hotkey('ctrl','c')
        time.sleep(0.5)
        #frota manfro
        gui.click(x=722, y=250)

        time.sleep(0.5)
        gui.hotkey('ctrl','v')
        time.sleep(0.5)
        #data Entrada
        gui.click(x=408, y=273)
        time.sleep(1)
        gui.hotkey('ctrt','a')
        time.sleep(0.5)
        gui.press('0')
        time.sleep(0.5)
        #Data saída
        gui.click(x=681, y=275)
        time.sleep(0.5)
        gui.write(nova_data_formatada)
        time.sleep(0.5)
        gui.press('0')
        time.sleep(0.5)
        #Motivo de Entrada
        gui.click(x=292, y=298)
        time.sleep(0.5)
        gui.press('3')   
        time.sleep(0.5)
        #Ponto de manutenção
        gui.click(x=296, y=323)
        time.sleep(0.5)
        gui.write('11017')  
        time.sleep(0.5)
        #box
        gui.click(x=729, y=323)
        time.sleep(0.5)
        gui.write('525')
        time.sleep(0.5)
        
        gui.click(x=316, y=344)
        time.sleep(0.5)
        gui.write('6302') #COHYBRA
        time.sleep(0.5)
        
        #Descrição
        gui.click(x=424, y=446)
        #time.sleep(0.5)
        #gui.write('Eletrica - ')
        time.sleep(0.5)
        gui.hotkey('alt','tab')
        #copica descrição na planilha
        for _ in range (6) :
            gui.press('right')
            time.sleep(0.1)
        gui.hotkey('ctrl','c')
        for _ in range (6) :
            gui.press('left')
            time.sleep(0.1)
        time.sleep(0.5)
        #cola descrição no manfro
        gui.click(x=424, y=446)
        time.sleep(0.5)
        gui.hotkey('ctrl','v')
        time.sleep(0.5)
        
        gui.click(x=238, y=570)
        time.sleep(0.5)
        gui.write('21')
        time.sleep(0.5)
        gui.click(x=360, y=570)
        time.sleep(0.5)
        gui.write('1700')
        time.sleep(0.5)
        gui.click(x=491, y=570)
        time.sleep(0.5)
        gui.write('1780')
        gui.click(x=628, y=569)
        time.sleep(0.5)
        gui.write('1')
        gui.click(x=792, y=569)
        time.sleep(0.5)
        gui.write('1')
        gui.click(x=865, y=569)
        time.sleep(0.5)
        gui.write('1')
        gui.click(x=972, y=569)
        time.sleep(0.5)
        gui.write('Serviço em terceiro')
        
        gui.click(x=118, y=159)
        time.sleep(0.5)
                
        gui.hotkey('alt','tab')
        gui.press('down')
        time.sleep(3)
        

#para resolução 1920x1080            
def resolucao_2(tela):
    for _ in range(Quantidade):
        #incluir
        gui.click(x=673, y=254)
        time.sleep(3)
        #Classe manutenção
        gui.click(x=1054, y=315)
        time.sleep(0.5)
        gui.write('11')   
        time.sleep(0.5)
        #status
        gui.press('j')
        time.sleep(0.5)
        gui.press('enter')
        time.sleep(0.5)
        gui.click(x=2003, y=579)
        time.sleep(0.5)
                
        #Copia frota na planilha
        gui.hotkey('ctrl','c')
        time.sleep(0.5)
        #frota manfro
        gui.click(x=918, y=340)

        time.sleep(0.5)
        gui.hotkey('ctrl','v')
        time.sleep(0.5)
        #data Entrada
        gui.click(x=646, y=362)
        time.sleep(1)
        gui.hotkey('ctrt','a')
        time.sleep(0.5)
        gui.press('0')
        time.sleep(0.5)
        #Data saída
        gui.click(x=857, y=367)
        time.sleep(0.5)
        gui.write(nova_data_formatada)
        time.sleep(0.5)
        gui.press('0')
        time.sleep(0.5)
        #Motivo de Entrada
        gui.click(x=519, y=387)
        time.sleep(0.5)
        gui.press('3')   
        time.sleep(0.5)
        #Ponto de manutenção
        gui.click(x=522, y=409)
        time.sleep(0.5)
        gui.write('11001')
        time.sleep(0.5)
        #box
        gui.click(x=947, y=413)
        time.sleep(0.5)
        gui.write('104')
        time.sleep(0.5)
        #Descrição
        gui.click(x=412, y=533)
        time.sleep(0.5)
        gui.write('Eletrica - ')
        time.sleep(0.5)
        gui.hotkey('alt','tab')
        #copica descrição na planilha
        for _ in range (6) :
            gui.press('right')
            time.sleep(0.1)
        gui.hotkey('ctrl','c')
        for _ in range (6) :
            gui.press('left')
            time.sleep(0.1)
        time.sleep(0.5)
        #cola descrição no manfro
        gui.click(x=572, y=531)
        time.sleep(0.5)
        gui.hotkey('ctrl','v')
        gui.click(x=359, y=251)
        time.sleep(0.5)
                
        gui.hotkey('alt','tab')
        gui.press('down')
        time.sleep(3)
                
if tela == 1:
    resolucao_1(Quantidade)
elif tela == 2:
    resolucao_2(Quantidade)
else:
    print("Opção inválida! Escolha 1 ou 2.")