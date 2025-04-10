import math

pi = math.pi
limite_inferior = 10 * (pi ** 3)
limite_superior = 100 * pi

print(f'Intervalo fechado: [{limite_inferior:.2f}, {limite_superior:.2f}]')
print('Digite número dentro desse intervalo. A leitura será encerrada se você digitar um número fora dele.\n')

soma_numeros = 0
quantidade_numeros = 0

while True:
    numero_valido = False
    while not numero_valido:
        try:
            numero = float(input('Digite um número: '))
            numero_valido = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido.')

    if numero < limite_inferior or numero > limite_superior:
        print(f'Número {numero} está fora de intervalo. Encerrado a leitura.')
        break

    soma_numeros += numero
    quantidade_numeros += 1

if quantidade_numeros > 0:
    media = soma_numeros / quantidade_numeros
    print(f'\nA média dos {quantidade_numeros} números lidos dentro do intervalo é: {media:.2f}')
else:
    print('\nNenhum número dentro do intervalo foi lido.')