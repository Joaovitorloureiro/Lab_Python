try:
    preco = float(input('Digite o preço da mercadoria: '))

    opcao = input('Escolha a opção (Acrescimo/Desconto):  ').strip().capitalize()

    percentual = 0.03

    if opcao == 'Acrscimo':
        novopreco = preco * (1 + percentual)
        print(f'Preço ajustado com acrescimo de 3%: R$ {novopreco:.2f}')
    elif opcao == 'Desconto':
        novopreco = preco * (1 - percentual)
        print(f'Preço ajustado com desconto 3%> R$ {novopreco:.2f}')
    else:
     print('Opção invalida! Escolha "Acrescimo" ou "Desconto".')

except ValueError:
    print('ERRO: Digite um valor numérico válido para o preço!')