total_pacientes = 500
soma_taxa = 0
pacientes_lidos = 0

while pacientes_lidos < total_pacientes:
    print(f'\nPaciente {pacientes_lidos + 1}:')

    idade_valida = False
    while not idade_valida:
        try:
            idade = float(input('Digite a idade do paciente (em anos): '))
            if idade <= 0:
                print('Erro: A idae deve ser positiva.')
            else:
                idade_valida = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido para a idade.')

    massa_valida = False
    while not massa_valida:
        try:
            massa = float(input('Digite a massa do paciente (em Kg): '))
            if massa <= 0:
                print('Erro: A massa deve ser positiva.')
            else:
                massa_valida = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido para a massa.')

    diabetes_valido = False
    while not diabetes_valido:
        try:
            diabetes = int(input('O paciente é diabético? (1 para Sim, 0 para Não): '))
            if diabetes not in [0, 1]:
                print('Erro: Digite 1 para Sim ou 0 para Não.')
            else:
                diabetes_valido = True
        except ValueError:
            print('Erro: Por favor, digite um valor numerico (1 ou 0).')
    
    if diabetes == 0:
        taxa = (0.08 * massa) ** 0.5 / (1.08 * idade)
    else:
        taxa = (massa ** (1/3) / (0.93 * idade))

    soma_taxa += taxa
    pacientes_lidos += 1

media_taxas = soma_taxa / total_pacientes
print(f'\nA taxa média de glicose dos {total_pacientes} pacientes é: {media_taxas:.4f}')