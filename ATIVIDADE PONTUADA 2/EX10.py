try:
    x = int(input('Digite o valor de x (x >= 1):  '))

    if x < 1:
        print('ERRO: O valor de x deve ser maior ou igual a 1!')
    else:
        limite_superior = 6 * x

        multiplos = []
        for num in range(6, limite_superior + 1):
            if num % 6 == 0:
                multiplos.append(num)

        if multiplos:
            media = sum(multiplos) / len(multiplos)
            print(f'A média dos multiplos de 6 no intervalo [6, {limite_superior}] é: {media:.2f}')
        else:
            print('Nenhum mútiplo de 6 encontrado (não deveria acontecer).')
        
except ValueError:
    print('ERRO: Digite um valor intero válido!')