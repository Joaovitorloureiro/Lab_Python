total_numeros = 300
menor_par = None
menor_impar = None
maior_par = None
maior_impar = None
numeros_lidos = 0

while numeros_lidos < total_numeros:
    print(f'\nNúmeros {numeros_lidos + 1}')

    numero_valido = False
    while not numero_valido:
        try:
            numero = float(input('Digite um número positivo: '))
            if numero <= 0:
                print('ERRO: O número deve ser positivo.')
            else:
                numero_valido = True
        except ValueError:
            print('ERRO: Por favor, digite um valor numérico válido.')

    if numero % 2 == 0:
        if menor_par is None or numero < menor_par:
            menor_par = numero
        if maior_par is None or numero > maior_par:
            maior_par = numero
    else:
        if menor_impar is None or numero < menor_impar:
            menor_impar = numero
        if maior_impar is None or numero > maior_impar:
            maior_impar = numero
    
    numeros_lidos += 1

print('\nResultados:')
print('Numero Pares:')
if menor_par is not None:
    print(f'Menor par {menor_par}')
    print(f'Maior par {maior_par}')
else:
    print('Nenhum número par foi digitado.')

print('\nNúmeros Ímpares:')
if menor_impar is not None:
    print(f'Menor ímpar: {menor_impar}')
    print(f'Maior ímpar {maior_impar}')
else:
    print('Nenhum número ímpar foi digitado.')