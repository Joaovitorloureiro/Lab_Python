import math

n_valido = False
while not n_valido:
    try:
        n = int(input('Digite um valor inteiro positivo para n (n >= 1): '))
        if n < 1:
            print('Erro: O valor de n deve ser maior ou igual a 1.')
        else:
            n_valido = True
    except ValueError:
        print('Erro: Por favor, digite um valor numérico inteiro válido.')

pi = math.pi
soma = 0
multiplicacao = 1

for demoninador in range(1, n + 1):
    if demoninador % 2 == 0:
        soma += pi / demoninador
soma += pi


for numerador in range(1, n + 1, 1):
    multiplicacao *= numerador / pi

print(f'\nResultados para n = {n}:')
print(f'Soma (S) = {soma:.4f}')
print(f'Multipicação (M) = {multiplicacao:.4f}')    