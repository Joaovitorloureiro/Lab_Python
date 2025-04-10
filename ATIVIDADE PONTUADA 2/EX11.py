try:
    n = int(input('Digite um número inteiro n:  '))
    
    print(f'Os 50 números subsequentes a {n} são:  ')
    for i in range(n + 1, n + 51):
        print(i, end=' ')

except ValueError:
    print('ERRO: Digite um valor inteiro válido!')