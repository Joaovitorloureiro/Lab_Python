total_maratonistas = 2000

menor_tempo = None
inscricao_vencedor = None
maratonistas_lidos = 0

while maratonistas_lidos < total_maratonistas:
    print(f'\nMaratonistas {maratonistas_lidos + 1}:')

    inscricao_valida = False
    while not inscricao_valida:
        try:
            inscricao = int(input('Digite o número de inscricão:  '))
            if inscricao <= 0:
                print('Erro: Por favor, o número de inscrição deve ser positivo.')
            else:
                inscricao_valida = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico inteiro válido para a inscrição.')

tempo_valido = False
while not tempo_valido:
    try:
        tempo = float(input('Digite o tempo de prova (em minutos): '))
        if tempo <= 0:
            print('Erro: O tempo de prova deve ser positivo.')
        else:
            tempo_valido = True
    except ValueError:
        print('Erro: Por favor, digite um valor numérico válido para o tempo.')

if menor_tempo is None or tempo < menor_tempo:
    menor_tempo = tempo
    inscricao_vencedor = inscricao

maratonistas_lidos += 1

print('\nResultado:')
print(f'Maratonista vencedor - Inscrição: {inscricao_vencedor}')
print(f'Tempo de prova: {menor_tempo:.2f} minutos')