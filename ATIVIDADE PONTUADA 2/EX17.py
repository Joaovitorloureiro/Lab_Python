menor_numero = None

while True:
    numero_valido = False
    while not numero_valido:
        try:
            numero = float(input('Digite um número real positivo (0 para encerrar): '))
            if numero < 0:
                print('ERRO: O número deve ser positivo ou zero.')
            else:
                numero_valido = True
        except ValueError:
            print('ERRO: Por Favor, digite um valor numérico válido.')
    if numero == 0:
        break

    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

if menor_numero is not None:
    print(f'\nO menor número positivo digitado foi: {menor_numero}')
else:
    print('\nNenhum número positivo fo digitado.')