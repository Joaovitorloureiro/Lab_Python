oncaparakg = 0.0283495
toneladaparakg = 1000.0
kgparaonca = 35.27396
kgparatonelada = 1.0 / 1000.0

try:
    massa = float(input('Digite o valor da massa:  '))

    unidadeoriginal = input('Digite a moeda de origem (Onça/Tonelada/Kg):  ').strip().capitalize()
    unidadedestino = input('Digite a moeda de destino (Onça/Tonelada/Kg):  ').strip().capitalize()

    if unidadeoriginal == 'Onça':
        massaemkg = massa * oncaparakg
    elif unidadeoriginal == 'Tonelada':
        massaemkg = massa * toneladaparakg
    elif unidadeoriginal == 'Kg':
        massaemkg = massa
    else:
        print('Moeda de origem inválida! Use "Onça", "Toneladas" ou "Kg". ')

    if unidadedestino == 'Onça':
        massaconvertida = massaemkg * kgparaonca
        simbolo = 'Onça'
    elif unidadedestino == 'Tonelada':
        massaconvertida = massaemkg * kgparatonelada
        simbolo = 'Toneladas'
    elif unidadedestino == 'Kg':
        massaconvertida = massaemkg
        simbolo = 'Kg'
    else:
        print('Moeda de destino invalida! Use "Onça", "Tonelada" ou "Kg".')
    
    print(f'Valor convertido: {massaconvertida:.2f} {simbolo}')
except ValueError:
    print('ERRO: Digite um valor numérico válido!')