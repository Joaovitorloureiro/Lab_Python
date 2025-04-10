numero = int(input('Digite um numero positivo: '))

if numero <= 0:
    print('O numero deve ser positivo!')
else:
    quadrado = numero ** 2

    impar = (quadrado % 2 != 0)
    multiplo_11 = (quadrado % 11 == 0)

    if impar and multiplo_11:
        print(f'O quadrado de {numero} é {quadrado}, que é impar e mutiplo de 11!')
    else:
        print(f'O quadrado de {numero} é {quadrado}, mas NÂO e impar e mutiplo de 11.')