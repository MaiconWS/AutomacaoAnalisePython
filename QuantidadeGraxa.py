import math

graxa =str
pergunta = input("Qual a medição graxa , hidraulico, aditivo ?  => ")

#Dimensões do tambor de graxa (Altura = 89cm, circunferencia = 58cm)
#Dimensões do reservatorio de aditivo (Altura = 49cm, Largura = 67cm, Comprimento = 104cm)

if pergunta == "graxa":
    MedicaoReguaTambor = float(input("Digite quantos cm deu na medição do tambor = "))
    #Volume do Graxa restante no tambor
    
    # 0.0841 = raio²
    VolumeGraxa = math.pi * 0.0841 * (MedicaoReguaTambor/100)
    # densidade da graxa 1.000 kg/m3, fonte = https://www.perma-tec.com/_Resources/Lubricants/Shell/Shell_Gadus_S3_V220C_2_MSDS_pt.pdf
    densidadeGraxa = 1000
    peso = densidadeGraxa * VolumeGraxa
    
    print(f"A quantidade KG restante de graxa no tambor é de => {peso:.2f}KG.")

elif pergunta == "hidraulico" :
    
    altura = float(input("Qual foi a altura medida ? "))
    comprimento = 0.58
    volume = 3.1416 * 0.0841 * (altura/100)
    litros = volume * 1000
    
    print(f"Ainda restam {litros:.2f}L de óleo hidraulico.")
    
elif pergunta == "aditivo" :
    
    comprimento = 1.04
    largura = 0.67
    altura = float(input("Digite a altura medida no reservatorio => "))
    volume = (comprimento * largura * (altura/100))*1000
    #conta para correção pois as bordas do tanque são arredondadas
    litros = (2.47 * volume) / 3.41
    
    print(f"Ainda restam {litros:.2f}L de aditivo.")