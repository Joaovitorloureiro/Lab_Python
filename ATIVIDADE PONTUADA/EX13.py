try:
    num1 = float(input('Digite o primeiro número:  '))
    num2 = float(input('Digite o segundo número:  '))
    num3 = float(input('Digite o terceiro número:  '))

    media = (num1 + num2 + num3) / 3

    if media < 0 or media > 200:
        print(f'A média está fora do intervalo [o, 200]: {media:.5f}')
    else:
        cubo = media ** 3
        print(f'O cubo da média é: {cubo:.5f}')

    phi = 11.52743
    print(f'Valor de PHI: {phi:.5f}')

except ValueError:
    print('ERRO: Digite valores numéricos válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')