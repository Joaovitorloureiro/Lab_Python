positivos = 0
negativos = 0
total_numeros = 0 

while True:
    numero_valido = False
    while not numero_valido:
        try:
            numero = float(input('Digitee um número real (0 para encerrar): '))
            numero_valido = True
        except ValueError:
            print('ERRO: Por favor, digite um valor númerico válido.')

    if numero == 0:
        break

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    total_numeros += 1

if total_numeros > 0:
    percentual_positivos = (positivos / total_numeros) * 100
    percentual_negativos = (negativos / total_numeros) * 100
    print('\nResultados:')
    print(f'Quantidade de números positivos: {positivos} ({percentual_positivos:.2f}%)')
    print(f'Quantidade de números negativos: {negativos} ({percentual_negativos:.2f}%)')
    print(f'Total de números lidos (excluindo o 0): {total_numeros}')
else:
    print('\nNenhum número foi lido (exceto o 0).')