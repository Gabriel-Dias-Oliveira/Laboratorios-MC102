# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB06: PROGRAMA PARA CONTROLE DA LINHA DE PRODUÇÃO DE CAJUÍNA, BASEADO EM UM NÚMERO 'X' DE REMESSAS, CADA UMA TENDO 'Y' CAJUS

def classificacao(qtd_caju):
    '''1º LINHA DE PRODUÇÃO ~ REDUZ A QUANTIDADE DE CAJUS DA REMESSA EM 1/3

    PARÂMETROS:
        qtd_caju -- NÚMERO DE CAJUS DA REMESSA

    RETORNA:
        A QUANTIDADE DE CAJUS 'BONS' (2/3 DO TOTAL)
    '''
    return int(qtd_caju * 2 / 3)

def prensagem(qtd_caju):
    '''2º LINHA DE PRODUÇÃO ~ CONVERTE O CAJU EM SUCO. O RETORNO VARIA DE ACORDO COM A QUANTIDADE DE CAJUS

    PARÂMETROS:
        qtd_caju -- NÚMERO DE CAJUS DA REMESSA

    RETORNA:
        A QUANTIDADE DE SUCO PRODUZIDA
    '''

    if qtd_caju >= 10: # SE A QUANTIDADE DE CAJU É >= 10. ENTÃO, RETORNA O DOBRO DA QUANTIDADE DE CAJUS EM SUCO
        return 2 * qtd_caju

    return 5 * qtd_caju # CASO A QUANTIDADE SEJA <10. ENTÃO O RETORNO DE SUCO É 5X QUANTIDADE DE CAJU

def filtragem(qtd_suco):
    '''3º LINHA DE PRODUÇÃO ~ DIMINUI A QUANTIDADE DE SUCO OBTIDO

    PARÂMETROS:
        qtd_scuo -- QUANTIDADE DE SUCO OBTIDA DA REMESSA

    RETORNA:
        A QUANTIDADE RESTANTE DE SUCO
    '''

    if qtd_suco > 45: # SE A QUANTIDADE DE SUCO FOR >45. ENTÃO, A QUANTIDADE DE SUCO QUE SEGUIRÁ NA PRODUÇÃO É 1/10 DO VALOR
        return int(qtd_suco * 1 / 10)

    return int(qtd_suco * 8 / 9) # CASO A QUANTIDADE SEJA <=45. ENTÃO, A QUANTIDADE QUE SEGUIRÁ SERÁ DE 8/9

def tratamento(qtd_cajuina):
    '''4º LINHA DE PRODUÇÃO ~ RETORNA A QUANTIDADE DE CAJUINA OBTIDA A PARTIR DA REMESSA

    PARÂMETROS:
        qtd_cajuina -- QUANTIDADE DE SUCO QUE SERÁ USADO PARA A EFETIVA PRODUÇÃO DE CAJUINA

    RETORNA:
        O VALOR DE CAJUINA OBTIDA NA REMESSA (2 VEZES QUANTIDADE DE SUCO RESTANTE)
    '''

    return 2 * qtd_cajuina #

def imprimeTela(tempo, remessa, producao, cajuina):
    '''FUNÇÃO PARA ACOMPANHAR O ESTADO ATUAL DA LINHA DE PRODUÇÃO

    PARÂMETROS:
        tempo -- TEMPO ATUAL DO PROCESSO
        remessa -- LISTA CONTENDO O ESTADO ATUAL DAS REMESSAS
        producao -- LISTA CONTENTO O ESTADO ATUAL DAS LINHAS DE PROCUÇÃO
        cajuina -- LISTA CONTENDO A QUANTIDADE DE CAJUINA PRODUZIDA POR CADA REMESSA (APÓS O FIM DO PROCESSAMENTO)
    '''
    print('T=' + str(tempo) + ' | ' + str(remessa) + ' -> ' + str(producao) + ' -> ' + str(cajuina)) # IMPRIME NA TELA O FORMATO BÁSICO DE SAÍDA

# CRIAÇAO DAS VARIÁVEIS BASES DO CÓDIGO

valor_valido = True # INFORMA SE TODOS OS VALORES DIGITADOS DE CAJUS SÃO VÁLIDOS >2 (TRUE = O PROGRAMA SEGUE | FALSE = ALERTA É IMPRESSO)
linha_producao = [0, 0, 0, 0] # LISTA DAS REPRESENTANDO AS 4 LINHAS DE PRODUÇÃO
cajuina = [] # LISTA PARA A QUANTIDADE DE CAJUINA
remessa = [] # LISTA PARA A QUANTIDADE DE CAJUS NAS REMESSAS
num_remessa = int(input('')) # QUANTIDADE DE REMESSAS

for x in range(0, num_remessa): # FOR QUE RODA 'NUM_REMESSA' VEZES, PARA SOLICITAR A QUANTIDADE DE CAJU DE CADA REMESSA
    qtd_caju = int(input(''))

    if qtd_caju < 2: # SE A QUANTIDADE DE CAJU FOR <2, UM ERRO DEVE SER IMPRESSO ASSIM COMO A PARADA DO PROGRANA
        valor_valido = False # VALOR_VALIDO = FALSE NÃO PERMITE QUE O PROGRAMA DÊ INICIO A PRODUÇÃO DE CAJUINA
        print('É necessário pelo menos dois cajus para produção de cajuína!')
        break # PARA O LAÇO

    remessa.append(qtd_caju) # CASO O VALOR SEJA VÁLIDO O VALOR É GUARDADO NAS REMESSAS

if valor_valido: # SE O VALOR_VALIDO = TRUE OS PROCESSOS IRÃO OCORRER
    for tempo in range(0, (num_remessa + 4)): # PARA QUE TODAS AS REMESSAS SEJAM PROCESSAS, O FOR DEVE RODAR 'NUM_REMESSA' VEZES + 4 VEZES (4 LINHAS PRODUÇÃO)
        imprimeTela(tempo, remessa, linha_producao, cajuina) # IMPRIME SEMPRE O ESTADO ATUAL DO PROCESSO

        if tempo > 3 and linha_producao[3] != 0: # SE O TEMPO = 4. ENTÃO, AS REMESSAS JÁ PODEM COMEÇAR A SER CONVERTIDAS EM CAJUINA
            cajuina.append(linha_producao[3]) 

        # O BLOCO DE CÓDIGO A SEGUIR BÁSICAMENTE FAZ A TROCA DAS QUANTIDADES ENTRE AS RESPECTIVAS LINHAS DE PRODUÇÕES
        linha_producao[3] = tratamento(linha_producao[2]) # 3º LINHA DE PRODUÇÃO -> 4º LINHA DE PRODUÇÃO
        linha_producao[2] = filtragem(linha_producao[1]) # 2º LINHA DE PRODUÇÃO -> 3º LINHA DE PRODUÇÃO
        linha_producao[1] = prensagem(linha_producao[0]) # 1º LINHA DE PRODUÇÃO -> 2º LINHA DE PRODUÇÃO

        if tempo < num_remessa: # VERIFICA SE AINDA EXISTEM REMESSAS PARA SEREM CHECADAS
            linha_producao[0] = classificacao(remessa[tempo]) # CASO EXISTA, A 1º LINHA DE PRODUÇÃO VAI RECEBER UMA NOVA REMESSA
            remessa[tempo] = 0
        else:
            linha_producao[0] = 0 # CASO CONTRÁRIO, NÃO EXISTEM MAIS REMESSAS, ENTÃO A 1º LINHA DE PRODUÇÃO RECEBE 0

    imprimeTela(tempo + 1, remessa, linha_producao, cajuina) # IMPRIME O RESULTADO OBTIDO DEPOIS DO FIM DO PROCESSO