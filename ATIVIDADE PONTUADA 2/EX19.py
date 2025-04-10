inicio = 1000
fim = 1500
multiplos_7 = []
multiplos_13 = []
multiplos_7_e_13 = []

for numero in range(inicio, fim + 1):
    eh_multiplo_7 = (numero % 7 == 0)
    eh_multiplo_13 = (numero % 13 == 0)

    if eh_multiplo_7 and multiplos_13:
        multiplos_7_e_13.append(numero)
    elif eh_multiplo_7:
        multiplos_7.append(numero)
    elif eh_multiplo_13:
        multiplos_13.append(numero)

print('Múltiplos de 7 ou 13 no intervalo de 1000 a 1500:\n')

print('Múltiplos apenas de 7:')
print(multiplos_7)

print('\nMúltiplos apenas de 13:')
print((multiplos_13))

print('\nMúltiplos de 7 e 13 (ao mesmo tempo):')
print(multiplos_7_e_13)

todos_multiplos = multiplos_7 + multiplos_13 + multiplos_7_e_13
print('\nTodos os números que são múltiplos de 7 ou 13 (em ordem):')
print(sorted(todos_multiplos))