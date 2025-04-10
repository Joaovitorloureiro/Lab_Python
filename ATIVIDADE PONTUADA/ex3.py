try:
    tempo_segundos = int(input('Digite o tempo de permanencia (em segundos):  '))
    
    if tempo_segundos < 0:
        print('ERRO: O tempo deve ser maior ou igual a 0')
    else:
        horas = tempo_segundos // 3600
        resto_segundos = tempo_segundos % 3600
        minutos = resto_segundos // 60
        segundos = resto_segundos % 60

        print(f'{horas} Hora(s) + {minutos} Minuto(s) + {segundos} Segundo(s)')

except ValueError:
    print('ERRO: Dados incorretos')