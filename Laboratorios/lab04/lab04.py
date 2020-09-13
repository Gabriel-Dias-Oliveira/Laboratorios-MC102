# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB04: CRIAÇÃO DE UM PROGRAMA QUE CALCULA O QUANTO UMA "APLICAÇÃO" RENDE A UMA TAXA DE JUROS MENSAL.

from decimal import Decimal

# CRIAÇÃO DAS VARIAVEIS BASES DO PROGRAMA, APLICAÇÃO INICIAL (CAPITAL),
# JUROS MENSAIS E
# QUANTOS MESES ESSA APLICAÇÃO RENDERÁ

capital = Decimal(input(''))
juros = Decimal(input(''))
meses = int(input(''))

for x in range(0, meses): # LAÇO DE REPETIÇÃO QUE SERVE PARA CALCULAR O RENDIMENTO MENSAL
    capital = capital * (1 + juros)

    while True: # WHILE TRUE IMPLICA NA ENTRADA OBRIGATÓRIA DESSE LAÇO E SUA REPETIÇÃO ATÉ QUE SEJA DADO UM VALOR VÁLIDO
        operacao = Decimal(input(''))

        if capital + operacao >= 0:
            capital += operacao
            break # SE O VALOR DA APLICAÇÃO + OPERAÇÃO DO MÊS EM QUESTÃO FOR VÁLIDA (> 0) PARA O LAÇO
        else:
             print('Valor inválido no mês', str(x) + '. Tente novamente.')

print('O total após', meses, 'meses é de R$', str(format(capital, '.2f')) + '.') # FIM COM A IMPRESÃO DO VALOR GERADO AO FINAL DA APLICAÇÃO