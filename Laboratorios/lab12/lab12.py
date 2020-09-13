# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB12: PROGRAMA QUE SIMULA UMA RODADA DO FAMOSO JOGO DE CARTAS 'TRAPAÇA'.

class Cartas:
    """ REPRESENTAÇÃO DAS CARTAS

        ARMAZENA: O VALOR E O NAIPE DAS CARTAS
    """

    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def naipe(self):
        return self._naipe

    @naipe.setter
    def naipe(self, naipe):
        self._naipe = naipe

    def compara_cartas(self, carta_comp):
        '''FUNÇÃO PARA COMPARAR E AUXILIAR NA ORDENAÇÃO DAS CARTAS

        PARÂMETRO:
            carta_comp -- CARTA A SER COMPARADA

        RETURN:
            RETORNA A COMPARAÇÃO (TRUE OU FALSE) ENTRE AS DUAS CARTAS (RESPEITANDO AS EXCEÇÕES)
        '''

        try:
            # DE MODO GERAL, OS IF'S VALIDAM EXCEÇÕES:
            # 'A' SEMPRE É MAIOR QUE STRINGS NUMÉRICAS, MAS NO JOGO ISSO É FALSO
            # 'Q' < 'K', MAS NO JOGO ISSO TAMBÉM NÃO É VÁLIDO
            # COMPARAÇÃO DE STRINGS NUMÉRICAS TAMBÉM FORAM TRATADAS COMO EXCEÇÕES
            if carta_comp.valor == 'A' and (not self.valor in ['A', 'J', 'K', 'Q']):
                return (self.valor < carta_comp.valor)
            elif self.valor == 'A' and (not carta_comp.valor in ['A', 'J', 'K', 'Q']):
                return (not self.valor > carta_comp.valor)
            elif self.valor == 'Q' and carta_comp.valor == 'K':
                return (not self.valor > carta_comp.valor)
            elif carta_comp.valor == 'Q' and self.valor == 'K':
                return (self.valor < carta_comp.valor)
            elif int(self.valor) and int(carta_comp.valor):
                if int(self.valor) != int(carta_comp.valor):
                    return int(self.valor) >= int(carta_comp.valor)
                else:
                    return self.naipe >= carta_comp.naipe
        except:
            # CASO NÃO EXISTE UMA EXCEÇÃO, ENTÃO O RETORNO É A SIMPLES COMPARAÇÃO DAS CARTAS
            return str(self.valor + self.naipe) > str(carta_comp.valor + carta_comp.naipe)

    def busca_cartas(self, busca):
        '''FUNÇÃO PARA AUXILIAR NA BUSCA DAS CARTAS ALVOS

        PARÂMETRO:
            busca -- VALOR DA CARTA A SER BUSCADA

        RETURN:
            RETORNA A COMPARAÇÃO (TRUE OU FALSE) ENTRE O VALOR DAS DUAS CARTAS (RESPEITANDO AS EXCEÇÕES)
        '''

        try:
            # DE MODO GERAL, OS IF'S VALIDAM EXCEÇÕES ~ PORÉM AGORA NÃO SÃO DUAS CARTAS:
            # 'A' SEMPRE É MAIOR QUE STRINGS NUMÉRICAS, MAS NO JOGO ISSO NÃO É VERDADEIRO
            # 'Q' < 'K', MAS NO JOGO ISSO TAMBÉM NÃO É VÁLIDO
            # COMPARAÇÃO DE STRINGS NUMÉRICAS TAMBÉM FORAM TRATADAS COMO EXCEÇÕES

            if busca == 'A' and (not self.valor in ['A', 'J', 'K', 'Q']):
                return (self.valor < busca)
            elif self.valor == 'A' and (not busca in ['A', 'J', 'K', 'Q']):
                return (not self.valor > busca)
            elif self.valor == 'Q' and busca == 'K':
                return (not self.valor > busca)
            elif busca == 'Q' and self.valor == 'K':
                return (self.valor < busca)
            elif int(self.valor) and int(busca):
                return int(self.valor) > int(busca)
        except:
            return str(self.valor) > str(busca)

    def __str__(self):
        return f'{self._valor}{self._naipe}'

def imprime_cartas(lista_cartas):
    '''FUNÇÃO PARA IMPRIMIR UMA LISTA DE ITENS ~ NO CASO CARTAS

    PARÂMETRO:
        lista_cartas -- LISTA COM OS ITENS A SEREM IMPRESSOS

    RETURN:
        RETORNA A STRING RESULTANTE DA JUNÇÃO DE TODOS OS ELEMENTOS DA LISTA
    '''

    text_card = ''
    for carta in lista_cartas:
        text_card += str(carta) + ' '

    return str(text_card).strip()

def lista_cartas(lista_cartas):
    '''ALGORITMO DE ORDENAÇÃO (INSERTION SORT) PARA ORDENAR A LISTA DE CARTAS

     PARÂMETRO:
        lista_cartas -- LISTA COM OS ITENS A SEREM ORDENADOS
    '''

    n = len(lista_cartas)

    # INSERTION SORT ~ COM BASE NAS RELAÇÕES ESTABELECIDAS NO MÉTODO DA CLASSE
    for i in range(n):
        aux = lista_cartas[i]
        j = i

        while j > 0 and lista_cartas[j - 1].compara_cartas(aux):
            lista_cartas[j] = lista_cartas[j - 1]
            j = j - 1

        lista_cartas[j] = aux

def busca_binaria(lst_cartas, carta_alvo, cart_achadas):
    '''ALGORITMO DE BUSCA NA LISTA DE CARTAS

    PARÂMETRO:
        lst_cartas -- LISTA COM OS ITENS A SEREM BUSCADOS
        carta_alvo -- TIPO (VALOR) DA CARTA ALVO
        cart_achada -- LISTA CONTENDO (QUE VAI CONTER) AS CARTAS DO TIPO DESEJADO

    RETURN:
       LISTA COM AS CARTAS ACHADAS
    '''

    n = len(lst_cartas)
    e = 0
    d = n - 1

    while e <= d:
        m = (e + d) // 2

        if lst_cartas[m].valor == carta_alvo:
            # SE O VALOR DA CARTA DESEJADA FOR ACHADO NA LISTA, ENTÃO PODEMOS FAZER UMA BUSCA APRIMORADA
            # BUSCANDO ASSIM AS DEMAIS (ATÉ 4) CARTAS DO TIPO DESEJADO

            cart_achadas = [x for x in lst_cartas if x.valor == carta_alvo]
            return cart_achadas
        elif not lst_cartas[m].busca_cartas(carta_alvo):
            e = m + 1
        elif lst_cartas[m].busca_cartas(carta_alvo):
            d = m - 1

    return cart_achadas

def adiciona_pilha(mao_bot, pilha):
    '''ADICIONA AS CARTAS DA PILHA A MÃO DO BOT!

    PARÂMETRO:
        mao_bot -- LISTA CONTENDO AS CARTAS ATUAIS DO BOT
        pilha -- LISTA CONTENDO AS CARTAS DA PILHA
    '''
    for carta in pilha:
        carta = Cartas(carta[:-1], carta[-1])
        mao_bot.append(carta)

    lista_cartas(mao_bot)

mao_bot = input().strip().upper().split()
pilha = input().strip().upper().split()
carta_alvo = input().strip().upper()
adv_duvidou = input().strip().upper()
lst_cartas = []
lista_cart_alv = []
blefou = False

for carta in mao_bot:
    carta = Cartas(carta[:-1], carta[-1])
    lst_cartas.append(carta)

lista_cartas(lst_cartas) # ASSEGURA QUE A MÃO VAI ESTAR ORDENADA

lista_cart_alv = busca_binaria(lst_cartas, carta_alvo, lista_cart_alv) # COMEÇA A BUSCA PELA CARTA ALVO DA RODADA

if len(lista_cart_alv) != 0:
    # CASO ALGUMA CARTA SEJA ACHADA, ENTÃO O BOT NÃO BLEFOU
    # REMOVE AS CARTAS JOGADAS DA MÃO DO BOT
    lst_cartas = [x for x in lst_cartas if x not in lista_cart_alv]
else:
    blefou = True
    # AQUI COMEÇA A BUSCA PELAS CARTAS DO MENOR VALOR DA MÃO DO BOT
    lista_cart_alv = busca_binaria(lst_cartas, lst_cartas[0].valor, lista_cart_alv)

print('Jogada: ' + imprime_cartas(lista_cart_alv))

if adv_duvidou == 'N':
    print('Nenhum bot duvidou')

    # SE NENHUM BOT DUVIDOU, AS CARTAS JOGADAS SÃO ADICIONADAS A PILHA
    for carta in lista_cart_alv:
        pilha.append(carta)

    lst_cartas = [x for x in lst_cartas if x not in lista_cart_alv] # MÃO DO BOT ~ APÓS A JOGADA
else:
    print('Um bot adversário duvidou')

    if blefou:
        # SE HOUVER DUVIDA E BLEFE, ENTÃO A PILHA É ADICIONADA A MÃO DO JOGADOR
        print('O bot estava blefando')
        adiciona_pilha(lst_cartas, pilha)
    else:
        print('O bot não estava blefando')

    pilha.clear()

print('Mão: ' + imprime_cartas(lst_cartas))

print('Pilha: ' + imprime_cartas(pilha))

if len(lst_cartas) == 0:
    # SE A MÃO DO BOT ESTIVER VAZIA, ENTÃO ELE VENCEU O JOGO!!
    print('O bot venceu o jogo')