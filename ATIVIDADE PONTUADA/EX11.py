from datetime import datetime

try:
    entrada = input('Digite a hora de entrada (HH:MM):  ')
    saida = input('Digite a hora de saída (HH:MM): ')
    valor30min = float(
        input('Digite o valor cobrado a cada 30 minutos (R$): '))

    formato = '%H:%M'
    horaentrada = datetime.strptime(entrada, formato)
    horasaida = datetime.strptime(saida, formato)

    diferenca = horasaida - horaentrada
    minutospermanecia = diferenca.total_seconds() // 60

    if minutospermanecia <= 0:
        print('ERRO: A hora de saida deve ser posterior a hora de entrada.')
    elif minutospermanecia > 1440:
        print('ERRO: O tempo máximo de permanência é de 24 horas.')
    else:
        if minutospermanecia <= 30:
            totalpagar = 0.0
        else:
            minutoscobrados = minutospermanecia - 30
            blocos30min = -(-minutoscobrados // 30)
            totalpagar = blocos30min * valor30min
        
        print(f'\nTempo total: {minutospermanecia} minutos')
        print(f'Total a pagar R$ {totalpagar:.2f}')
except ValueError:
    print('ERRO: Formato de hora inválido ou valor incorreto. Use o formato HH:MM e números válidos.')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')