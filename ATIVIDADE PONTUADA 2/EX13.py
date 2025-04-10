total_pessoas = 50
maior_altura_homem = 0
maior_altura_mulher = 0
soma_altura_homens = 0
soma_altura_mulheres = 0
contagem_homens = 0
contagem_mulheres = 0
homens_acima_182 = 0
mulheres_acima_182 = 0

for pessoa in range(1, total_pessoas + 1):
    print(f'\nDados da pessoa {pessoa}:')

    while True:
        try:
            altura = float(input('Digite a altura(em metros, exemplo: 1.75):  '))
            if altura <= 0:
                raise ValueError
            break
        except ValueError:
            print('ERRO: Por favor, digite um valor numérico válido para altura (exemplo: 1.75).')

    while True:
        try:
            sexo = int(input('Digite o sexo (1 para Masculino, 2 para Feminino):  '))
            if sexo not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print('ERRO: DIgite 1 para Masculino ou 2 para Feminino.')

    if sexo == 1:
        contagem_homens += 1
        soma_altura_homens += 1
        soma_altura_homens += altura
        if altura > maior_altura_homem:
            maior_altura_homem = altura
        if altura > 1.82:
            homens_acima_182 += 1
    else:
        contagem_mulheres += 1
        soma_altura_mulheres += altura
        if altura > maior_altura_mulher:
            maior_altura_mulher = altura
        if altura > 1.82:
            mulheres_acima_182 += 1

print('\n====Resultado====')
print(f'a) Maior altura entre homens: {maior_altura_homem:.2f} metros')
print(f'b) Maior altura entre mulheres: {maior_altura_mulher:.2f} metros')
print(f'Média da altura dos homens: {maior_altura_homem:.2f} metros')
print(f'Média da altura das mulheres: {maior_altura_mulher:.2f} metros')
percentual_homens_acima_182 = (homens_acima_182 / contagem_homens * 100) if contagem_homens > 0 else 0
percentual_mulheres_acima_182 = (mulheres_acima_182 / contagem_mulheres * 100) if contagem_mulheres > 0 else 0
print(f'Porcentagem de homens com mais de 1.82 m: {percentual_homens_acima_182:.2f}%')
print(f'Porcentagem de mulheres com mais de 1.82 m: {percentual_mulheres_acima_182:.2f}%')


