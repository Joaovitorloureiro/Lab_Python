try:
    valoringresso = int(input('Digite o valor inteiro do ingresso (em reais): '))
    totalpessoas = int(input('Digite o total de pessoas no jogo:  '))

    if valoringresso <= 0 or totalpessoas <= 0:
        print('ERRO: O valor do ingresso e o número de pessoas devem ser maiores que 0')

    else:
        publicototal = totalpessoas
        arrecadacao = 0

        for i in range(totalpessoas):
            idade = int(input(f'Digite a idade da {i+1} pessoa: '))

            if idade < 10:
                preco = 0.0            
            elif 11 <= idade <= 17:
                arrecadacao += valoringresso / 2
            else:
                doacao = input(f'A {i+1} pessoa doou 1kg de alimento? (S/N): ').strip().upper()
                if doacao == 'S':
                    arrecadacao += valoringresso / 2
                else:
                    arrecadacao += valoringresso
        print(f'\nPublico total: {publicototal} pessoas')
        print(f'Arrecadação total: R$ {arrecadacao:.2f}')
except ValueError:
    print('ERRO: Entrada invalida. Certifique-se de inserir numero inteiros corretamentes.')
            
