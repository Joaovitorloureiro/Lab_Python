try:
    numeros = []
    for i in range(5):
        num = int(input(f'Digite o {i+1}° número inteiro positivo:  '))
        if num <= 0:
            print('ERRO: Todos os números devem ser positivos!')
            exit()
        numeros.append(num)

    if len(numeros) != len(set(numeros)):
        print('AVISO: Os valores informados contêm duplicatas!')
    
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    mediapares = sum(pares) / len(pares) if pares else 0
    mediaimpares = sum(impares) / len(impares) if impares else 0

    print(f'Média dos números PARES: {mediapares:.2f}')
    print(f'Média dos números IMPARES: {mediaimpares:.2f}')

except ValueError:
    print('ERRO: Digite valores inteiros válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')