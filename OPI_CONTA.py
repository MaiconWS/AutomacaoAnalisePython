correto = int(input('Digite o correto número: '))
questionavel = int(input('Digite os itens questionaveis número: '))

valor = correto/(correto+questionavel)*100

print(f'A % segura é: {valor:.2f}%')
