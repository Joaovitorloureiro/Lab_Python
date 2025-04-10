soma_positivos = 0
soma_negativos = 0
cont_positivos = 0
cont_negativos = 0

while True:
    numero_valido = False
    while not numero_valido:
        try:
            numero = float(input('Digite um número real (0 para encerrar): '))
            numero_valido = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido.')

    if numero == 0:
        print('Leitura encerrada.')
        break

    if numero > 0:
        soma_positivos += numero
        cont_positivos += 1
    elif numero < 0:
        soma_negativos += numero
        cont_negativos += 1

print('\nResultados:')

if cont_positivos > 0:
    media_positivos = soma_positivos / cont_positivos
    print(f'Média dos números positivos: {media_positivos:.2f} ({cont_positivos} números lidos)')
else:
    print('Nenhum número negativo foi lido.')

