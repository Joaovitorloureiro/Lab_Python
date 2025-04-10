try:
    altura_cm =float(input('Digite a altura (em centimetros): '))
    sexo = input('Digite o sexo (M para masculino, F para feminino): ').strip().upper()

    if altura_cm <= 0:
        print('ERRO: A altura deve ser maior que 0')
    else:
        h = altura_cm / 100

        if sexo == 'M':
            quilo_ideal = 72.7 * h - 58
            print(f'O peso ideal para um homem com {altura_cm} cm é: {quilo_ideal:.2f} kg')
        elif sexo == 'F':
            quilo_ideal = 62.1 * h - 44.7
            print(f'O quilo ideal para uma mulher com {altura_cm} cm é: {quilo_ideal:.2f} kg')
        else:
            print('ERRO: Sexo invalido. Digite "M" para masculino ou "f" para feminino')
except ValueError:
    print('ERRO: Dados incorretos')