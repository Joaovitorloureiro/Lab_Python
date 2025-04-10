realparalibra = 1.0 / 4.08
dolarparalibra = 1.0 / 1.12
libraparareal = 4.08
libraparadolar = 1.12

try:
    valor = float(input('Digite o valor:  '))

    moedaorigem = input('Digite a moeda de origem (Real/Dolar/Libra):  ').strip().capitalize()
    moedadestino = input('Digite a moeda de destino (Real/Dolar/libra):  ').strip().capitalize()

    if moedaorigem == 'Real':
        valoreemlibras = valor * realparalibra
    elif moedaorigem == 'Dolar':
        valoreemlibras = valor * dolarparalibra
    elif moedaorigem == 'Libra':
        valoreemlibras = valor
    else:
        print('Moeda de origem inválida! Use "Real", "Dolar" ou "Libra". ')

    if moedadestino == 'Real':
        valorcovertido = valoreemlibras * libraparareal
        simbolo = 'R$'
    elif moedadestino == 'Dolar':
        valorcovertido = valoreemlibras * libraparadolar
        simbolo = 'US$'
    elif moedadestino == 'Libra':
        valorcovertido = valoreemlibras
        simbolo = '£'
    else:
        print('Moeda de destino invalida! Use "Real", "Dolar" ou "Libra".')
    
    print(f'Valor convertido: {simbolo} {valorcovertido:.2f}')
except ValueError:
    print('ERRO: Digite um valor numérico válido!')