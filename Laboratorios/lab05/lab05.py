# GABRIEL DIAS DE OLIVEIRA, RA: 176495 - CIÊNCIA DA COMPUTAÇÃO 1º SEMESTRE
# LAB05: CRIAÇÃO DE UM PROGRAMA PARA CHEGACAGEM DE REDUNDÂNCIA EM UMA MENSAGEM, UTILIZANDO O CÓDIDO CRC E OPERAÇÕES XOR

# CRIAÇAO DAS VARIÁVEIS BASES DO CÓDIGO

mensagem = list(input('')) # GUARDA A MENSAGEM A SER ENVIADA PELO USUÁRIO - EM UMA LISTA
polinomio = list(input('')) # GUARDA O PÔLINOMIO BASE PARA AS OPERAÇÕES XOR E CRIAÇÃO DO CRC - EM UMA LISTA
crc = '' # CRC A SER PREENCHIDO COM O CÓDIGO GERADO

for cont in range(0, len(polinomio) - 1): # FOR QUE POPULA A MENSAGEM COM O QUE VIRÁ A SER O "CRC". TAMANHO CRC = nPOLINOMIO -1
    mensagem.append('0')

dif_tamanho = len(mensagem) - len(polinomio) + 1 # PEGA O TAMANHO SOMENTE DA MENSAGEM

for bit in range(0, dif_tamanho): # FOR PARA PERCORRER TODAS AS POSIÇÕES DA MENSAGEM
    if mensagem[bit] == '1': # SE O CARACTER DA MENSAGEM FOR '1', ENTÃO É REALIZADA OPERAÇÃO
        contador = 0

        for xor in range(bit, bit + len(polinomio)): # PARTINDO DA POSIÇÃO DA MENSAGEM ATUAL
            if mensagem[xor] == polinomio[contador]:
                mensagem[xor] = '0' # SE MENSAGEM = POLINOMIO, A POSIÇÃO RECEBE 0
            else:
                mensagem[xor] = '1'  # SE MENSAGEM != POLINOMIO, A POSIÇÃO RECEBE 1

            contador += 1 # COMO A POSIÇÃO INICIAL DA MENSAGEM SEMPRE VARIA NO FOR, MAS A DO POLINOMIO NÃO, A CHECAGEM DA POSIÇÃO DO POLINOMIO É FEITA PELO CONTADOR

for x in range(dif_tamanho, len(mensagem)): # FOR QUE PEGA O CONTEÚDO GERADO QUE DIZ RESPEITO AO FORMATO DO CRC
    crc += mensagem[x]

print(crc) # FINALIZA IMPIMINDO O CÓDIGO