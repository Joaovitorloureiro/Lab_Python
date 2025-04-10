multiplos = []
soma = 0
cont = 0

for num in range(198, 99, -11):
    print(num)
    multiplos.append(num)
    soma += num
    cont += 1

media = soma / cont  if cont > 0 else 0

print(f'\nSoma dos multiplos de 11: {soma}')
print(f'Média dos múltiplos de 11: {media:.2f}')