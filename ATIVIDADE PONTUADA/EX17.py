try:
    a = float(input('Digite o valor de A:  '))
    b = float(input('Digite o valor de B:  '))
    c = float(input('Digite o valor de C:  '))

    if a <= 0 or b <= 0 or c <= 0:
        print('ERRO: Todos os valores devem ser positivos!')
    else:
        if (a < b + c) and (b < a + c) and (c < a + b):
            if a == b == c:
                tipo = 'Equilátero'
            elif a == b or b == c or a == c:
                tipo = 'Isósceles'
            else:
                tipo = 'Escaleno'
            print(f'Os valores {a}, {b} e {c} foram um triângulo {tipo}.')
        else:
            print(f'Os valores {a}, {b}, {c} NÂO formam um triângulo.')
except ValueError:
    print('ERRO: Digite valores numéricos válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')