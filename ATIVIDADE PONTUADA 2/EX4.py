soma_pares = 0
soma_impares = 0

num = 10
while num <= 99:
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num
    num += 1
print(f'Soma dos numeros PARES no intervalo [10, 99]: {soma_pares}')
print(f'Soma dos números IMPARES no intervalo [10,, 99]: {soma_impares}')