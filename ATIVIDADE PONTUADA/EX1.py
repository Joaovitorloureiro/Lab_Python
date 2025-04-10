import math

try:
    r = float(input("Digite o valor da raio da esfera:  "))
    area  = 4 * 3.14 * (r ** 2)
    volume = (4/3) * 3.14 * (r ** 3)
    print(f"O volume: {volume: .3f}")
    print(f"A area: {area: .2f}")
except ValueError:
    print("ERRO: Dados incorretos")
