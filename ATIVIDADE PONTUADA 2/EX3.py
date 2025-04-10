limite_inferior = int(input('Digite o limite inferior:  '))
limite_superior = int(input('Digite o limite superior:  '))
n = (int(input('Digite o número n (n >= 2):  ')))

if n < 2 or limite_inferior < 0 or limite_superior < limite_inferior:
    print('Entrada invalida. Certifique-se de que n >= 2 e os limites são naturais com superior >= inferior.')
else:
    print(f'Multiplos de {n} no intervalo [{limite_inferior}, {limite_superior}]:')

    primeiro_multiplo = limite_inferior if limite_inferior % n == 0 else limite_inferior + (n - limite_inferior % n)

    for num in range(primeiro_multiplo, limite_superior + 1, n):
        print(num)