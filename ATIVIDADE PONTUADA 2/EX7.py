contagem = 0
soma = 0

for num in range (9, 91):
    if num % 3 == 0 and num % 5 != 0 and num % 2 != 0:
        contagem += 1
        soma += num

print(f'Contagem de números: {contagem}')
print(f'Soma dos números: {soma}')
