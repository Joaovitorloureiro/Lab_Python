total_habitantes = 10000
empregados = 0
desempregados = 0

for i in range (total_habitantes):
    status = input(f'Pessoas {i+1}: Está empregado? (S/N): ').strip().upper()
    if status == 'S':
        empregados += 1
    elif status == 'N':
        desempregados += 1
    else:
        print('Entrada invalida. Digite "S" para SIM ou "N" para NÂO.')
        i -= 1

percent_empregados = (empregados / total_habitantes) * 100
percent_desempregados = (desempregados / total_habitantes) * 100

print(f'\nEmpregados: {percent_empregados:.2f}%')
print(f'Desempregados: {percent_desempregados:.2f}%')
