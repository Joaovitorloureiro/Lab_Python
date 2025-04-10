salario_minimo = 998.05
total_clientes = 1000

categoria_A = 0
categoria_B = 0
categoria_C = 0

for i in range(total_clientes):
    salario = float(input(f'Digite o salári do cliente {i+1}: R$'))

    if salario >= 15 * salario_minimo:
        categoria_A += 1
    elif salario >= 5 * salario_minimo:
        categoria_B += 1
    else:
        categoria_C += 1

percent_A = (categoria_A / total_clientes) * 100
percent_B = (categoria_B / total_clientes) * 100
percent_C = (categoria_C / total_clientes) * 100

print(f'\nClientes categoria A (>= 15 SM): {percent_A:.2f}%')
print(f'Clientes categoria B (5 >= SM < 15 SM): {percent_B:.2f}%')
print(f'Clientes categoria C (< 5 SM): {percent_C:.2f}%')