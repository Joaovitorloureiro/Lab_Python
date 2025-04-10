total_mercadorias = 50
taxa_reajuste = 5
limite_preco = 25.50
taxa_desconto = 2

for mercadoria in range(1, total_mercadorias + 1):
    print(f'\nMercadoria {mercadoria}:')

    preco_valido = False
    while not preco_valido:
        try:
            preco = float(input('Digite o preço da mercadoria (em R$): '))
            if preco <= 0:
                print('Erro: O preço deve ser positivo.')
            else:
                preco_valido = True
        except ValueError:
            print('Erro: Por favor, digite um valor numéric válido para o preço.')

preco_reajustado = preco * (1 + taxa_reajuste / 100)

if preco_reajustado > limite_preco:
    preco_final = preco_reajustado * (1 - taxa_reajuste / 100)
    print(f'Preço original: R$ {preco:.2f}')
    print(f'Preço com reajuste de {taxa_reajuste}%: R$ {preco_reajustado:.2f}')
    print(f'Preço excedeu R$ {limite_preco:.2f}, aplicando desconto de {taxa_desconto}%')
    print(f'Preço final: R$ {preco_final:.2f}')
else:
    preco_final = preco_reajustado
    print(f'Preço original: R$ {preco:.2f}')
    print(f'Preço com reajust de {taxa_reajuste}%: R$ {preco_final:.2f}')