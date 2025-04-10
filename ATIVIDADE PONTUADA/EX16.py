try:
    numeros = []
    for i in range(3):
        num = float(input(f'Digite o {i+1}° número real:  '))
        numeros.append(num)
    
    if len(numeros) != len(set(numeros)):
        print('AVISO: Os valores informados contêm duplicatas!')

    numerosordenados = sorted(numeros, reverse=True)
    mediadosmaires = (numeros[0] + numerosordenados[1] / 2)

    print(f'Média dos dois maiores números: {mediadosmaires:.2f}')

except ValueError:
    print('ERRO: Digite valores numéricos válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')