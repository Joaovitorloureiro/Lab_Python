total_eleitores = 6
votos_candidato1 = 0
votos_candidato2 = 0
votos_nulos = 0
eleitores_votaram = 0

while eleitores_votaram < total_eleitores:
    print('\n=== Menu de Opçoes ===')
    print('1 - Votar')
    print('2 - Ver resultado parcial')
    print('3 - Encerrar votação')

    opcao = -1
    while opcao not in [1, 2, 3]:
        try:
            opcao = int(input('Escolha uma opção (1, 2 ou 3): '))
            if opcao not in [1, 2, 3]:
                print('ERRO: Digite 1, 2 ou 3.')
        except ValueError:
            print('ERRO: Por favor, digite um valor numérico (1, 2 ou 3).')
    
    if opcao == 1:
        if eleitores_votaram >= total_eleitores:
            print('Todos os eleitores já votaram!')
        else:
            print(f'\nEleitor {eleitores_votaram + 1}:')

            voto = -1
            while voto not in [0, 1, 2]:
                try:
                    voto = int(input('Digite seu voto (1 para Candidato 1, 2 para Candidato 2, 0 para Nulo/Inválido): '))
                    if voto not in [0, 1, 2]:
                        print('ERRO: Digite 1, 2 ou 0.')
                except ValueError:
                    print('ERRO: Por favor, digite um valor numérico (1, 2 ou 0).')
            
            if voto == 1:
                votos_candidato1 += 1
            elif voto == 2:
                votos_candidato2 += 1
            else:
                votos_nulos += 1
            
            eleitores_votaram += 1
            print('Voto registrado com sucesso!')
        
    elif opcao == 2:
        if eleitores_votaram == 0:
            print('Nenhum voto registrado ainda.')
        else:
            percentual_candidato1 = (votos_candidato1 / eleitores_votaram) * 100
            percentual_candidato2 = (votos_candidato2 / eleitores_votaram) * 100
            percentual_nulo = (votos_nulos / eleitores_votaram) * 100
            print('\nResultado Parcial:')
            print(f'Candidato 1: {percentual_candidato1:.2f}% ({votos_candidato1} votos)')
            print(f'Candidato 2: {percentual_candidato2:.2f}% ({votos_candidato2} votos)')
            print(f'Nulos/Inválidos: {percentual_nulo:.2f}% ({votos_nulos} votos)')
            print(f'Eleitores que votaram: {eleitores_votaram} de {total_eleitores}')


    elif opcao == 3:
        print('\nVotação encerrada.')
        break

if eleitores_votaram > 0:
    percentual_candidato1 = (votos_candidato1 / eleitores_votaram) * 100
    percentual_candidato2 = (votos_candidato2 / eleitores_votaram) * 100
    percentual_nulo = (votos_nulos / eleitores_votaram) * 100
    print('\nResultado Final da Eleição:')
    print(f'Candidato 1: {percentual_candidato1:.2f}% ({votos_candidato1} votos)')
    print(f'Candidato 2: {percentual_candidato2:.2f}% ({votos_candidato2} votos)')
    print(f'Nulos/Inválidos: {percentual_nulo:.2f}% ({votos_nulos} votos)')
    print(f'Total de eleitores que votaram: {eleitores_votaram} de {total_eleitores}')
else:
    print('\nNenhum voto foi registrado.')