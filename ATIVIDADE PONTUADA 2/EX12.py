soma = 0
cont = 0

print('Digite as temperaturas diária do verão capixaba (Digiite uma temperatura <= 28°C para sair): ')

while True:
    try:
        temperatura = float(input('Temperatura:  '))

        if temperatura <= 28:
            break
        
        soma += temperatura
        cont += 1
    
    except ValueError:
        print('ERRO: Digite um valor numérico válido!')
if cont > 0:
    media = soma / cont
    print(f'\nTemperatura média do verão capixaba: {media:.2f}°C')
else:
    print('\nNenhuma temperatura válida foi inserida.')