# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB02: CÁLCULO DO SALÁRIO DE UM FUNCIONÁRIO COM BASE NAS HORAS TRABALHADAS E HORAS EXTRAS.

nome = input('')
num_horas = int(input(''))
valor_hora = float(input(''))
salario = (8 * valor_hora) * 22 # SALÁRIO QUE OBRIGATORIAMENTE ELE DEVERÁ RECEBER (22 DIAS NO MÊS)

if num_horas >= 8 and num_horas <= 14: # MÍNIMO E MÁXIMO DA JORNADA DE TRABALHO
    if num_horas > 12:
        # PARA UMA JORANADA >12 HRS - PARA CADA HORA EXTRA O FUNCIONÁRIO RECEBE 1.5x O VALOR/HORA
        salario = (((num_horas - 8) * (valor_hora * 1.5)) * 22) + salario
    elif num_horas > 8 and num_horas <= 12:
        # PARA UMA JORNADA >8 E <12 HRS - PARA CADA HORA EXTRA O FUNCIONÁRIO RECEBE 1.25x O VALOR/HORA
        salario = (((num_horas - 8) * (valor_hora * 1.25)) * 22) + salario

    print('O salário do(a) funcionário(a) ' + nome + ' será de R$' + str(format(salario, '.2f')) + ' para esse mês')
else:
    print('Número de horas diárias não admitido')
