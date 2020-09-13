# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB09: CONSTRUÇÃO DE UM JOGO DA VIDA ~ 'SIMULAÇÃO DO COMPORTAMENTO DE CÉLULAS'.

def imprime_tabuleiro(matriz):
    '''IMPRIME O TABULEIRO COM A FOMATAÇÃO E AS CÉLULAS CORREPONDENTES

    PARÂMETROS:
        matriz -- REPRESENTAÇÃO DO TABULEIRO
    '''

    # LAÇOS PARA PERCORRER A MATRIZ E IMPRIMIR SEU CONTEÚDO
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='')
        print('')

    print('-')

def celula_vida(i, j, matriz):
    '''ATRIBUI UMA CÉLULA VIVA A UMA LINHA-COLUNA

    PARÂMETROS:
        i -- LINHA
        j -- COLUNA
        matriz -- REPRESENTAÇÃO DO TABULEIRO
    '''
    matriz[i][j] = '+'

def cria_tabuleiro(linha, coluna, matriz):
    '''CRIA O TABULEIRO COM O TAMANHO LINHA-COLUNA DEFINIDOS PELO USUÁRIO

    PARÂMETROS:
        linha -- LINHAS DO TABULEIRO
        coluna -- COLUNAS DO TABULEIRO
        matriz -- REPRESENTAÇÃO DO TABULEIRO
    '''

    # INICIA O TABULEIRO COM CÉLULAS MORTAS '.'
    for i in range(linha):
        linha_nova = []
        for j in range(coluna):
            linha_nova.append('.')

        matriz.append(linha_nova)

def atualiza_tabuleiro(matriz, nov_gera):
    '''ATUALIZA O TABULEIRO DE ACORDO COM AS MUDANÇAS OCORRIDAS ~ NOVA GERAÇÃO

    PARÂMETROS:
        matriz -- REPRESENTAÇÃO DO TABULEIRO
        nov_gera -- NOVA GERAÇÃO A SER COLOCADA NO TABULEIRO
    '''

    for i in range(len(nov_gera)):
        for j in range(len(nov_gera[i])): #
            matriz[nov_gera[i][0]][nov_gera[i][1]] = nov_gera[i][2]

def nova_celula(matriz):
    '''RESPONSÁVEL POR FAZER AS ANÁLISES DO JOGO, DEFININDO ASSIM COMO DEVE SER A PRÓXIMA GERAÇÃO

    PARÂMETROS:
        matriz -- REPRESENTAÇÃO DO TABULEIRO
    '''
    nova_geracao = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            linha = coluna = -1 # PARÂMETROS PARA DESLOCAR AS POSIÇÕES
            cont_vizinho = 0

            for cont in range(6): # PARA CADA POSIÇÃO PODE EXISTIR 6 VIZINHOS
                # SE O DESLOVAMENTO DA LINHA E DA COLUNA, NÃO GERAREM UM POSIÇÃO INVÁLIDA:
                if (i + linha != len(matriz) and i + linha != -1) and (j + coluna != len(matriz[i]) and j + coluna != -1):
                    if matriz[i + linha][j + coluna] == '+':
                        # VERIFICA SE NA POSIÇÃO JÁ EXISTE UMA CÉLULA VIVA = 1 VIZINHO
                        cont_vizinho += 1

                if cont < 3: # ALTERA A POSIÇÃO DA COLUNHA A SER ANÁLISADA
                    coluna += -1 * linha
                else:
                    coluna += linha

                if cont == 2:
                    # APÓS RODAR 3 VEZES, OS VIZINHOS SUPERIORES FORAM CHECADOS
                    # COMEÇA A VERIFICAR OS VIZINHOS INFERIORES
                    linha, coluna = 1, -1

            # VERIFICA OS VIZINHOS LATERAIS
            if j + 1 != len(matriz[i]):
                if matriz[i][j + 1] == '+':
                    cont_vizinho += 1

            if j - 1 != -1:
                if matriz[i][j - 1] == '+':
                    cont_vizinho += 1

            if cont_vizinho == 3:
                # SE VIZINHOS = 3, ENTÃO A POSIÇÃO (I, J) VAI RECEBER UMA NOVA CÉLULA
                nova_geracao.append([i, j, '+'])
            elif cont_vizinho < 2 or cont_vizinho > 3:
                # SE VIZINHOS < 2 OU > 3 A CÉLULA MORRE
                nova_geracao.append([i, j, '.'])

    atualiza_tabuleiro(matriz, nova_geracao) # MODIFICA O TABULEIRO COM BASE NAS ALTERAÇÕES CHECADAS
    imprime_tabuleiro(matriz) # IMPRIME A NOVA GERAÇÃO

# VARIÁVEIS BASE DO SISTEMA
linha = int(input())
coluna = int(input())
tabuleiro = []
cria_tabuleiro(linha, coluna, tabuleiro)
qtd_rodadas = int(input()) # DEFINE QUANTAS GERAÇÕES TERÃO
qtd_cel_viva = int(input()) # QUANTAS CÉLULAS ESTARÃO VIVAS INICIALMENTE

for x in range(qtd_cel_viva): # ATRIBUI UMA CÉLULA VIVA A UMA POSIÇÃO LINHA~COLUNA
    lin, colun = input().split(',')
    celula_vida(int(lin), int(colun), tabuleiro)

imprime_tabuleiro(tabuleiro) # GERAÇÃO INICIAL

for x in range(qtd_rodadas): # GERA AS NOVAS GERAÇÕES
    nova_celula(tabuleiro)