limite_inferior = -15
limite_superior = 5

print(f'Temperaturas no inverno devem estar no intervalo de {limite_inferior}°C a {limite_superior}°C.')
print('Digite uma temperatura fora desse intervalo para encerrar a leitura.\n')

soma_temperaturas = 0
quantidade_dias = 0

while True:
    temperatura_valida = False
    while not temperatura_valida:
        try:
            temperatura = float(input(f'Digite a temperatura do dia {quantidade_dias + 1} (em °C): '))
            temperatura_valida = True
        except ValueError:
            print('Erro: Por favor, digite um valor numérico válido.')
    
    if temperatura < limite_inferior or temperatura > limite_superior:
        print(f'Temperatura {temperatura} °C está fora do intevalo de inverno. Encerrando a leitura.')
        break

    soma_temperaturas += temperatura
    quantidade_dias += 1

if quantidade_dias > 0:
    media = soma_temperaturas / quantidade_dias
    print(f'\nA média das temperaturas no inverno é: {media:.2f}°C')
    print(f'Total de dias registrados: {quantidade_dias}')
else:
    print('\nNenhuma temperatura dentro do intevalo de invernp foi registrada.')