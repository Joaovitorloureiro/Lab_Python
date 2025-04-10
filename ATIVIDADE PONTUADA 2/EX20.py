clientes_vip = 0
clientes_padrao = 0
total_clientes = 0

while True:
    print('\n=== Menu de Opções ===')
    print('1 - Cadastrar Cliente')
    print('0 - Sair do Program')

    opcao_valida = False
    while not opcao_valida:
        try:
            opcao = int(input('Escolha uma opção (1 ou 0): '))
            if opcao in [0, 1]:
                opcao_valida = True
            else:
                print('ERRo: Digite 1 ou 0.')
        except ValueError:
            print('ERRO: Por favor, digite um valor numérico (1 ou 0).')
    
    if opcao == 0:
        print('\nPrograma encerrado.')
        break
    
    if opcao == 1:

        salario_valido = False
        while not salario_valido:
            try:
                salario = float(input('Digite o salário do cliente (em R$): '))
                if salario < 0:
                    print('ERRO: O salario não pode ser negativo.')
                else:
                    salario_valido = True
            except ValueError:
                print('Erro: Por favor, digite um valor numérico válido para o salário.')

        if salario >= 5000:
            clientes_vip += 1
        else:
            clientes_padrao += 1

        total_clientes += 1
        print('Cliente cadastrado com sucesso!')
    
if total_clientes > 0:
    percentural_vip = (clientes_vip / total_clientes) * 100
    percentural_padrao = (clientes_padrao / total_clientes) * 100
    print('\nResultados:')
    print(f'Clientes com cartão VIP: {percentural_vip:.2f}% ({clientes_vip} clientes.)')
    print(f'Clientes com cartão PADRÃO: {percentural_padrao}% ({clientes_padrao} clientes.)')
    print(f'Total de cientes cadastrados: {total_clientes}')
else:
    print('\nNenhum  cliente foi cadastrado.')