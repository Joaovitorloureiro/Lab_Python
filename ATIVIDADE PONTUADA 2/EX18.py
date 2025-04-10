total_numeros = 100
soma_numeros = 0
numeros_lidos = 0

while numeros_lidos < total_numeros:
    print(f'\nNúmeros {numeros_lidos + 1}:')

    numero_valido = False
    while not numero_valido:
        try:
            numero = int(input('Digite um número inteiro ímpar e múltiplo de 7 (0 para encerrar): '))
            if numero == 0:
                print('Leitura encerrada.')
                numero_valido = True
                break
            if numero % 2 == 0 or numero % 7 != 0:
                print('ERRO: O número deve ser ímpar e múltiplo de 7.')
            else:
                numero_valido = True
        except ValueError:
            print('ERRO: Por favor, digite um valor numérico inteiro válido.')

    if numero == 0:
        break

    soma_numeros += numero
    numeros_lidos += 1

if numeros_lidos > 0:
    media = soma_numeros / numeros_lidos
    print(f'\nA média dos {numeros_lidos} números ímpares e múltiplos de 7 é: {media:.2f}')
else:
    print('\nNenhum número ímpar e múltiplo de 7 foi lido.')    
        