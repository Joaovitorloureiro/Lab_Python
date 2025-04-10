unidade  = input('Digite a unidade (C para Celsius, F para Fahrenheit:  ').strip().upper()

try:
    temperatura = float(input('Digite o valor da temperatura: '))

    if unidade == 'C':
        fahrenheit = (9/5) * temperatura + 32
        print(f'{temperatura}°C  é igual a {fahrenheit:.2f}°F')
    elif unidade == 'F':
        celsius = (5/9) * (temperatura - 32)
        print(f'{temperatura}°F é igual a {celsius:.2f}°C')
    else:
        print('Unidade inálida! Use "C" para Celsius ou "F" para Fahrenheit.')
except ValueError:
    print('ERRO: Digite um valor numérico válido para a temperatura!')
    