import math
try:
    h = float(input('Digite o valor da Altura(cm): '))
    b = float(input('Digite o valor da base(cm):  '))

    if b <= 0 or b <= 0:
        print('ERRO: Base e Altura devem ser maior que 0')
    else:
        perimetro = 2 * b + 2 * h
        polegadas = perimetro / 2.54
        jarbas = polegadas * 0.03

    print("/nResultados do perimetro")
    print(f'O perimetro em centimetros: {perimetro: .2f} cm')
    print(f'O perimetro em polegadas: {polegadas: .2f} polegadas')
    print(f'O perimetro em jarbas {jarbas: .2f} jarbas')
except ValueError:
    print('ERRO: Dados incorretos')
