try:
    av1 = float(input('Digite a nota da AV1 (0 a 10):  '))
    av2 = float(input('Digite a nota da AV2 (0 a 10):  '))
    pf = float(input('Digite a nota da Prova Final (0 a 10, ou -1 se não fez):  '))
    tf = int(input('Digite o total de faltas (TF):  '))

    if not (0 <= av1 <= 10 and 0 <= av2 <= 10 and 0 <= pf <= 10 or pf == -1) or tf < 0:
        print('ERRO: Notas devem estar entre 0 e 10, e faltas não podem ser negativas!')
    else:
        mp = (av1 + av2) / 2

        if mp >= 6:
            final = mp
        elif 3 <= mp < 6 and pf != -1:
            final = (mp + pf) / 2
        else:
            final = mp
        
        maxfaltas = 20
        if tf > maxfaltas:
            resultado = 'Reprovado por Falta'
        elif final >= 6:
            resultado = 'Aprovado'
        elif 3 <= mp < 6:
            resultado = 'Prova Final'
        else:
            resultado = 'Reprovado'
        
        print(f'\nResultados Parciais e Finais:')
        print(f'MP (Média Parcial): {mp:.2f}')
        print(f'Final (Nota Final): {final:.2f}')
        print(f'STATUS: {resultado}')

except ValueError:
    print('ERRO: Digite valores numéricos válidos!')
except Exception as e:
    print(f'ERRO: Ocorreu um problema - {e}')