total_entrevistados = 10000
soma_fundamental = 0
soma_medio = 0
soma_superior = 0 
cont_fundamental = 0
cont_medio = 0
cont_superior = 0
entrevistados_lidos = 0

while entrevistados_lidos < total_entrevistados:
    print(f'\nEntrevistado {entrevistados_lidos + 1}:')

    salario_valido = False
    while not salario_valido:
        try:
            salario = float(input('Digite o salário bruto (em R$): '))
            if salario < 0:
                print('Erro: O salário não pode ser negativo.')
            else:
                salario_valido = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido para o salário.')

escolaridade_valida = False
while not escolaridade_valida:
    try:
        print('Nivel de escolaridade:')
        print('1 - Fundamental')
        print('2 - Médio')
        print('3 - Superior')
        escolaridade = int(input('Escolha uma opção (1, 3 ou 3): '))
        if escolaridade not in [1, 2, 3]:
            print('Erro: Digite 1, 2 ou 3.')
        else:
            escolaridade_valida = True
    except ValueError:
        print('Erro: Por favor, digite um valor numérico (1, 2 ou 3).')

    if escolaridade == 1:
        soma_fundamental += salario
        cont_fundamental += 1
    elif escolaridade == 2:
        soma_medio += salario
        cont_medio += 1
    else:
        soma_superior += salario
        cont_superior += 1

    entrevistados_lidos += 1

print('\nResultados - Média Salarial por Nivel de Escolaridade:')

if cont_fundamental > 0:
    media_fundamental = soma_medio / cont_medio
    print(f'Superior: R$ {media_fundamental:.2f} ({cont_fundamental} entrevistados)')
else:
    print('Médio: Nenhum entrevistado com esse nível de escolaridade.')

if cont_superior > 0:
    media_superior = soma_superior / cont_superior
    print(f'Superior: R$ {media_superior:.2f} ({cont_superior} entrevistados)')
else:
    print('Superior: Nenhum entrevistado com esse nível de escolaridade')