try:
    soma = 0

    while True:
        n = int(input('Diite um número N (0 para parar):  '))

        if n == 0:
            break

        if n < 10 or n > 90:
            print('ERRO: O número deve estar no intervalo [10, 90]!')
            continue

        if n % 5 == 2:
            soma += n
    print(f'Soma dos números lidos: {soma}')

except ValueError:
    print('ERRO: Digite um valor inteiro válido!')
