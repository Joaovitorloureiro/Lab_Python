try:
    massa = float(input('Digite a massa (em quilogramas):  '))
    altura = float(input('Digite a altura (em metros):  '))

    if massa <= 0 or altura <= 0:
        print('ERRO: Massa e altura devem ser valores possitivos!')
    else:
        imc = massa / (altura ** 2)
        if imc < 18.5:
            classificacao = 'Magreza'
        elif 18.5 <= imc < 25:
            classificacao = 'Saudavel'
        elif 25 <= imc < 30:
            classificacao = 'Sobrepeso'
        elif 30 <= imc < 35:
            classificacao = 'Obesidade Grau I'
        elif 35<= imc < 40:
            classificacao = 'Obesidade Grau II (Severa)'
        else:
            classificacao = 'Obesidade Gray III (Mórbida)'
        
        print(f'IMC: {imc:.2f}')
        print(f'Classificacao: {classificacao}')
except ValueError:
    print('ERRO: Digite valores numéricos válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')