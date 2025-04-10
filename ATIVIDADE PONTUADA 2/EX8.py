try:
    num_clientes = int(input('Digite o número de clientes que partiparão:  '))

    if num_clientes <= 0:
        print('ERRO: O número de clientes deve ser positivo!')
    else:
        votos_sabor1 = 0
        votos_sabor2 = 0
        votos_sabor3 = 0

        for i in range(num_clientes):
            while True:
                voto = int(input(f'Digite o voto do cliente {i+1} (1, 2 ou 3):  '))
                if voto in [1, 2, 3]:
                    break
                print('ERRO: Voto inválido! Digite 1, 2 ou 3.')
            
            if voto == 1:
                votos_sabor1 += 1
            elif voto == 2:
                votos_sabor2 += 1
            elif voto == 3:
                votos_sabor3 += 1
        
        print('\nResultado da votação:')
        print(f'Votos para Sabor 1: {votos_sabor1}')
        print(f'Votos para Sabor 2: {votos_sabor2}')
        print(f'Votos para sabor 3: {votos_sabor3}')

        if votos_sabor1 > votos_sabor2 and votos_sabor1 > votos_sabor3:
            print('Sabor mais popular: Sabor 1')
        elif votos_sabor2 > votos_sabor1 and votos_sabor2 > votos_sabor3:
            print('Sabor mais popular: Sabor 2')
        elif votos_sabor3 > votos_sabor1 and votos_sabor3 > votos_sabor2:
            print('Sabor mais popular: Sabor 3')
        else:
            print('Empate entre os sabores ou votação equilibrada!')
except ValueError:
    print('ERRO: Digite valores inteiros válidos!')
