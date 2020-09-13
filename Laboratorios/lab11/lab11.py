# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB11: PROGRAMA DE CADASTRO E ORDENAÇÃO DE PAÍSES A PARTIR DE ALGUM CRITÉRIO ESTABELECIDO.

class Pais:
    """ REPRESENTAÇÃO DOS PAÍSES

        RECEBE OS DADOS DOS PAÍSES: NOME, POPULAÇÃO, PIB, LONGEVIDADE, QUALIDADE EDUCACAO, RENDA E DESIGULDADE
    """

    def __init__(self, nome='', populacao=0, pib=0, longevidade=0, qual_edu=0, renda=0, desigualdade=0):
        self._nome = nome
        self._populacao = populacao
        self._pib = pib
        self._longevidade = longevidade
        self._qual_edu = qual_edu
        self._renda = renda
        self._desigualdade = desigualdade

        # CÁLCULO DO IDH COM BASE NAS INFORMAÇÕES ANTERIORES
        self._idh = int((self._desigualdade * (self._longevidade + self._qual_edu + self._renda)) / 3)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def populacao(self):
        return self._populacao

    @populacao.setter
    def populacao(self, populacao):
        self._populacao = populacao

    @property
    def pib(self):
        return self._pib

    @pib.setter
    def pib(self, pib):
        self._pib = pib

    @property
    def longevidade(self):
        return self._longevidade

    @longevidade.setter
    def longevidade(self, longevidade):
        self._longevidade = longevidade

    @property
    def qual_edu(self):
        return self._qual_edu

    @qual_edu.setter
    def qual_edu(self, qual_edu):
        self._qual_edu = qual_edu

    @property
    def renda(self):
        return self._renda

    @renda.setter
    def renda(self, renda):
        self._renda = renda

    @property
    def desigualdade(self):
        return self._desigualdade

    @desigualdade.setter
    def desigualdade(self, desigualdade):
        self._desigualdade = desigualdade

    @property
    def idh(self):
        return self._idh

    @idh.setter
    def idh(self, idh):
        self._idh = idh

    def __str__(self):
        '''REPRESENTAÇÃO TEXTUAL DOS PAÍSES

        RETURN:
            SAÍDA INDICANDO O NOME, POPULAÇÃO, PIB E IDH DOS PAÍSES
        '''
        return f'{self._nome} {self._populacao} {self._pib} {self._idh}'

def cadastro_paises(list_paises):
    '''CADASTRA OS PAÍSES NO SISTEMA

       PARÂMETROS:
       list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO

       RETURN:
           TRUE -- TODAS AS INFORMAÇÕES ESTÃO NO INTERVALO CORRETO
           FALSE -- ALGUMA INFORMAÇÃO ESTÁ FORA DO INTERVALO
    '''

    num_paises = int(input())

    for x in range(num_paises):
        # PRA MELHOR VISUALIZAÇÃO CADA INFORMAÇÕES FOI COLOCADA EM UMA VARIAVEL
        nome, populacao, pib, longevidade, educao, renda, desigualdade = input().strip().split(' ')

        # CHECAGEM DE INFORMAÇÕES
        if int(longevidade) <= 0:
            print('Longevidade fora do intervalo')
            return False
        elif int(educao) < 0 or int(educao) > 10:
            print('Educação fora do intervalo')
            return False
        elif int(desigualdade) < 0 or int(desigualdade) > 10:
            print('Desigualdade fora do intervalo')
            return False

        pais = Pais(nome, int(populacao), int(pib), int(longevidade),
                    int(educao), int(renda), int(desigualdade))

        list_paises.append(pais) # SALVA O PAIS

    return True

def imprime_pais(lista_paises):
    '''IMPRIME OS PAÍSES DE UMA LISTA

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''

    # FOR A SER UTILIZADO MAIS DE UMA VEZ NAS FUNÇÕES DE ORDENAÇÃO
    for pais in lista_paises:
        print(pais)

def lista_ordem_cad(list_paises):
    '''IMPRIME OS PAÍSES NA ORDEM DE CADASTRO

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''

    print('Ordenado por Cadastro')

    imprime_pais(list_paises)

def lista_nomes(list_paises):
    '''IMPRIME OS PAÍSES ORDENADOS PELO NOME

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''
    n = len(list_paises)

    # INSERTION SORT
    for i in range(n): # FOR PRA PERCORRER AS POSIÇÕES DA LISTA
        aux = list_paises[i]
        j = i

        while j > 0 and list_paises[j - 1].nome > aux.nome:
            # DESLOCA OS ELEMENTOS 'MAIORES' QUE O DA POSIÇÃO ATUAL
            list_paises[j] = list_paises[j - 1]
            j = j - 1

        # INSERE O ELEMENTO NA POSIÇÃO CORRETA
        list_paises[j] = aux

    print('Ordenado por Nome')

    imprime_pais(list_paises)

def lista_populacao(list_paises):
    '''IMPRIME OS PAÍSES ORDENADOS PELA POPULÇÃO

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''
    n = len(list_paises)

    # INSERTION SORT ~ COM BASE NA POPULAÇÃO
    for i in range(n):
        aux = list_paises[i]
        j = i

        while j > 0 and list_paises[j - 1].populacao < aux.populacao:
            # FAZ A ORDENAÇÃO EM ORDEM DECRESCENTE!!
            list_paises[j] = list_paises[j - 1]
            j = j - 1

        list_paises[j] = aux

    print('Ordenado por População')

    imprime_pais(list_paises)

def lista_pib(list_paises):
    '''IMPRIME OS PAÍSES ORDENADOS PELO PIB

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''
    n = len(list_paises)

    # INSERTION SORT ~ COM BASE NO PIB
    for i in range(n):
        aux = list_paises[i]
        j = i

        while j > 0 and list_paises[j - 1].pib < aux.pib:
            # FAZ A ORDENAÇÃO EM ORDEM DECRESCENTE!!
            list_paises[j] = list_paises[j - 1]
            j = j - 1

        list_paises[j] = aux

    print('Ordenado por PIB')

    imprime_pais(list_paises)

def lista_idh(list_paises):
    '''IMPRIME OS PAÍSES ORDENADOS PELO IDH

    PARÂMETROS:
        list_paises -- LISTA COM OS PAÍSES CADASTRADOS ~ ATÉ O MOMENTO
    '''
    n = len(list_paises)

    # INSERTION SORT ~ COM BASE NO IDH
    for i in range(n):
        aux = list_paises[i]
        j = i

        while j > 0 and list_paises[j - 1].idh < aux.idh:
            # FAZ A ORDENAÇÃO EM ORDEM DECRESCENTE!!
            list_paises[j] = list_paises[j - 1]
            j = j - 1

        list_paises[j] = aux

    print('Ordenado por IDH')

    imprime_pais(list_paises)

paises_cad = [] # LISTA PRA CONTROLE DOS PAISES
valida_laco = True # CONTROLA O LAÇO

while valida_laco:
    acoes = int(input())
    copia_lista = paises_cad.copy() # CÓPIA DA LISTA ~ PODE SER ALTERADA!

    if acoes in range(1, 7):
        if acoes == 1:
            # SE AS INFORMAÇÕES APRESENTAREM ERRO, ENTÃO O LAÇO PARA
            valida_laco = cadastro_paises(paises_cad)
        elif acoes == 2:
            lista_ordem_cad(paises_cad)
        elif acoes == 3:
            lista_nomes(copia_lista)
        elif acoes == 4:
            lista_populacao(copia_lista)
        elif acoes == 5:
            lista_pib(copia_lista)
        else:
            lista_idh(copia_lista)
    else:
        # SE O VALOR ESTIVER FORA DO RANGE, ENTÃO PARA O LAÇO
        valida_laco = False