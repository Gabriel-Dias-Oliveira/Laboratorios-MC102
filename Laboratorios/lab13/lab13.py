# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB13: ADAPTAÇÃO DO JOGO 'ONDE ESTÁ CARMEN SANDIEGO?'.

def filtra_lista(pista, dicionario, dica_formada, conta_letra, k):
    '''FILTRA A LISTA DE POSSÍVEIS PAÍSES BASEADO NAS DICAS FORNECIDAS

    PARÂMETRO:
        pista -- PARTE DA DICA TOTAL (CONJUNTO DE LETRAS)
        dicionario -- CONTÉM OS PAÍSES NO QUAL A CARMEN PODE ESTAR
        dica_formada -- CONTÉM A STRING COMPLETA DA DICA
        conta_letra -- CONTA AS LETRAS DAS DICAS ~ USADO COMO FILTRO PARA OS PAÍSES
        k -- POSIÇÃO [0, 1 OU 2] DA DICA ATUAL
    RETURN:
        RETORNA O DICIONÁRIO FILTRADO
    '''

    # PARA CADA LETRA DA PISTA VAMOS FILTRAR OS POSSÍVEIS PAÍSES
    for letra in pista:
        possiveis_paises = []

        # POPULA E ADMINISTRA O DICIONÁRIO DE LETRAS
        if letra not in list(conta_letra.keys()):
            conta_letra[letra] = 1
        else:
            conta_letra[letra] += 1

        for chave in dicionario.keys():
            # SE O PAÍS NÃO CONTER A LETRA
            # SE O PAÍS CONTER A LETRA, MAS EM UMA QUANTIDADE MENOR QUE A DICA
            # ENTÃO ELE NÃO É UM POSSÍVEL PAÍS
            if letra in chave and chave.count(letra) >= conta_letra[letra]:
                 possiveis_paises.append(chave)

        dicionario = {chave: valor for chave, valor in dicionario.items() if chave in possiveis_paises}

    # FILTRA OS ÚLTIMOS POSSÍVEIS PAÍSES
    if k == 2 and len(possiveis_paises) > 1:
        dicionario = {chave: valor for chave, valor in dicionario.items() if len(chave) == len(dica_formada)}

    return dicionario

def busca_carmen(dicionario, pais, k, dica, conta_letra):
    '''FUNÇÃO RECURSIVA RESPONSÁVEL POR FAZER A BUSCA DA CARMEN ENTRE OS PAÍSES

    PARÂMETRO:
        dicionario -- CONTÉM OS PAÍSES NO QUAL A CARMEN PODE ESTAR
        pais -- PAÍS ATUAL ONDE O JOGADOR ESTÁ
        k -- POSIÇÃO [0, 1 OU 2] DA DICA ATUAL
        dica -- CONTÉM A STRING COMPLETA DA DICA
        conta_letra -- CONTA AS LETRAS DAS DICAS ~ USADO COMO FILTRO PARA OS PAÍSES
    RETURN:
        O RETORNO RECURSIVO NOS FORNECE:
            FALSE ~ CARMEN FOI ACHADA E O PROGRMA PARA
            pais_novo ~ NOVO PAÍS PARA O QUAL O JOGADO DEVE IR
    '''

    # SE O DICIONÁRIO SÓ TIVER UMA POSIÇÃO ENTÃO ACHAMOS O PRÓXIMO PAÍS OU A CARMEN
    if len(dicionario) == 1:
        pais_novo = ''.join(list(dicionario.keys()))
        if pais_novo == 'carmen':
            print(f'Descobri com {k} pistas que Carmen Sandiego está no país')
            return False
        else:
            print(f'Descobri com {k} pistas que devo viajar para {pais_novo}')
            conta_letra.clear()
            return pais_novo
    else:
        dicionario = filtra_lista(dica[k], dicionario, ''.join(dica), conta_letra, k)
        # CHAMA A PRÓPRIA FUNÇÃO PARA QUE O DICIONÁRIO POSSA SER FILTRADO COM UMA NOVA DICA
        return busca_carmen(dicionario, pais, k+1, dica, conta_letra)

pais_inicial = input().strip()
paises_dicas = {}
conta_letra = {}
pais_dica = ''

# POPULA O DICIONÁRIO COM OS PAÍSES E AS RESPECTIVAS DICAS
while pais_dica != 'X':
    pais_dica = input().strip()

    if pais_dica.upper() != 'X':
        pais_dica = pais_dica.split(':')
        chave = pais_dica[0]
        pais_dica = (''.join(pais_dica[1:])).split(',')

        paises_dicas[chave] = pais_dica

# CARMEN SERÁ TRATADA COMO UM PAÍS PARA PODER SER FILTRADA AO LONGO DA BUSCA
paises_dicas['carmen'] = []

print('Iniciando as buscas em', pais_inicial)

# ENQUANTO A FUNÇÃO NÃO ACHAR A CARMEN
while pais_inicial != False:
    pais_novo = busca_carmen(paises_dicas.copy(), pais_inicial, 0, paises_dicas[pais_inicial], conta_letra)
    pais_inicial = pais_novo