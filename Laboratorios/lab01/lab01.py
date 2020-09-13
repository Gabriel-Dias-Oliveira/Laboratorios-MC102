# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB01: CÓDIGO PARA INVERTER UM NÚMERO DECIMAL - "MUNDO INVERTIDO".

from decimal import Decimal

numero = Decimal(input("")) # NÚMERO NO FORMATO AB.CD ~ ZEROS NO COMÇO E FIM PODEM SER IGNORADOS

# DIVIDE-SE O NÚMERO E TODAS AS SUAS RESPECTIVAS UNIDADES:

parte_inteira = int(numero)

dezena = str(int(parte_inteira // 10))
unidade = str(int(parte_inteira % 10))

parte_decimal = (numero - parte_inteira) * 100 # SABENDO QUAL É A PARTE INTEIRA PODEMOS PEGAR A PARTE DECIMAL

decimo = str(int(parte_decimal // 10))
centesimo = str(int(parte_decimal % 10))

# POSTERIORMENTE BASTA REMODELAR O NÚMERO PARA QUE ELE ESTEJA INVERTIDO

novo_numero = str("R$ " + centesimo + decimo + "." + unidade + dezena)

print(novo_numero)