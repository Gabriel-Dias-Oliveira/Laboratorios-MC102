# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB07: CONSTRUÇÃO DE UM JOGO RPG DE CARTAS.

class Heroi():
    """ REPRESENTAÇÃO DO HERÓI (JOGADOR)

    ARMAZENA ATRAVÉS DE PARÂMETROS (DEFINIDO PELO JOGADOR): NOME, MAX_VIDA, DANO, BLOQUEIO, MAX_MANA
    """

    def __init__(self, nome, max_vida, dano, bloqueio, max_mana): # MÉTODO CONSTRUTOR DA CLASSE
        self.nome = nome
        self.max_vida = max_vida
        self.vida = max_vida
        self.dano = dano
        self.bloqueio = bloqueio
        self.max_mana = max_mana
        self.mana = max_mana
        self.has_insano = False # VÁLIDARÁ SE HÁ OU NÃO CARTA INSANA
        self.vet_insano = [] # GUARDARÁ OS VALORES DA CARTA INSANA
        self.has_estrela = False # VÁLIDARÁ SE HÁ OU NÃO CARTA ESTRELA
        self.vet_estrela = [] # GUARDARÁ OS VALORES DA CARTA ESTRELA
        self.insano = False # VALIDA O EFEITO INSANO ATIVADO
        self.estrela = False # VALIDA O EFEITO ESTRELA ATIVADO
        self.drenagem = False # VALIDA O EFEITO DRENAGEM ATIVADO
        self.mana_dren = 0 # GUARDA O EFEITO DA DRANAGEM (PONTOS A SEREM DRENADOS)
        self.invuneral = 0 # GUARDA O NÚMERO DE RODADAS INVUNERÁVEL
        self.dano_extra = 0 # GUARDA O DANO EXTRA

    def set_insano(self, dano_extra, rodadas, ativa_insano = False):
        self.dano_extra = dano_extra
        self.rodadas = rodadas
        self.has_insano = ativa_insano
        if self.rodadas > 0: # SE O NÚMERO DE RODADAS FOR > 0. ENTÃO, O EFEITO DEVE CONTINUAR, OU SEJA, TRUE
            self.insano = True
        else: # CASO NÃO: O EFEITO INSANO DEVE SER REMOVIDO (FALSE) E AS DEMAIS VARIÁVEIS DEVEM ADQUIRIR VALOR PADRÃO
            self.insano = False
            self.dano_extra = 0
            self.has_insano = False
            self.vet_insano = []

    def set_estrela(self, rodadas, ativa_estrela = False):
        self.invuneral = rodadas
        self.has_estrela = ativa_estrela
        if self.invuneral > 0:  # SE O NÚMERO DE RODADAS FOR > 0. ENTÃO, O EFEITO DEVE CONTINUAR, OU SEJA, TRUE
            self.estrela = True
        else: # CASO NÃO: O EFEITO ESTRELA DEVE SER REMOVIDO (FALSE) E AS DEMAIS VARIÁVEIS DEVEM ADQUIRIR VALOR PADRÃO
            self.has_estrela = False
            self.estrela = False
            self.vet_estrela = []

    def set_drenagem(self, valor, pontos):
        self.drenagem = valor

        if self.mana_dren == 0: # SE A DRENAGEM AINDA ESTIVER VALENDO 0, O JOGADOR NUNCA PEGOU ESSA CARTA, PORTANTO, A OPERAÇÃO É VÁLIDA
            self.mana_dren = pontos

    def set_vetor_insano(self, carta):
        self.vet_insano = carta

    def set_vetor_estrela(self, carta):
        self.vet_estrela = carta

    def set_vida(self, valor):
        if self.vida + valor >= self.max_vida:
            # A VIDA NUNCA PODE ASSUMIR UM VALOR > MÁXIMO DE VIDA, ENTÃO SE ISSO OCORRER, POR PADRÃO O VALOR 'MAX_VIDA' É ATRIBUIDO
            self.vida = self.max_vida
        elif self.vida + valor <= 0:
            # A VIDA NUNCA PODE ASSUMIR UM VALOR < 0, ENTÃO SE ISSO OCORRER, POR PADRÃO O VALOR 0 É ATRIBUIDO
            self.vida = 0
        else:
            self.vida += valor # SENÃO, O VALOR SERÁ ALTERADO COM BASE NO VALOR PASSADO

    def set_mana(self, pontos):
        if self.mana + pontos >= self.max_mana:
            # A MANA NUNCA PODE ASSUMIR UM VALOR > MÁXIMO DE MANA, ENTÃO SE ISSO OCORRER, POR PADRÃO O VALOR 'MAX_MANA' É ATRIBUIDO
            self.mana = self.max_mana
        elif self.mana + pontos <= 0:
            # A MANA NUNCA PODE ASSUMIR UM VALOR < 0, ENTÃO SE ISSO OCORRER, POR PADRÃO O VALOR 0 É ATRIBUIDO
            self.mana = 0
        else:
            self.mana += pontos # SENÃO, O VALOR SERÁ ALTERADO COM BASE NO VALOR PASSADO

    def set_dano(self, valor):
        self.dano = self.dano + valor

    def set_bloqueio(self, percentual):
        if self.bloqueio + percentual >= 100:
            # O BLOQUEIO É UM VALOR DE 0 ~ 100. ENTÃO SE FOR > 100, O VALOR 100 É ATRIBUIDO POR PADRÃO
            self.bloqueio = 100
        else:
            self.bloqueio = self.bloqueio + percentual

    def __str__(self): # METÓDO DE 'REPRESENTAÇÃO TEXTUAL' DA CLASSE HERÓI
        # IMPRIME TODAS AS INFORMAÇÕES NECESSÁRIAS DO HERÓI DE MODO ORGANIZADO
        return (self.nome + ' possui ' + str(self.vida) + ' de vida, ' +
                str(self.mana) + ' pontos mágicos, ' + str(self.dano) + ' de dano e ' +
                str(self.bloqueio) + '% de bloqueio')

def ataque(jogador_rodada, adversario):
    ''' DEFINE COMO E QUAL É O TIPO DE ATAQUE, VALIDANDO TODOS OS POSSÍVEIS CENÁRIOS DEVIDO AO USO DAS CARTAS MÁGICAS

    PARÂMETROS:
        jogador_rodada -- JOGADOR DA RODADA
        adversario -- ADVERSÁRIO DA RODADA
    '''

    if adversario.estrela: # SE O ADVERSÁRIO ESTIVER COM O EFEITO ESTRELA:
        if not jogador_rodada.insano: # SE O JOGADOR NÃO ESTIVER COM O EFEITO INSANO:
            print(jogador_rodada.nome, 'atacou', adversario.nome)
        else:
            print(jogador_rodada.nome, 'deu um ataque insano em', adversario.nome)
            # CASO O JOGADOR TENHA A CARTA INSANA ATIVADA, A SUA DURAÇÃO DEVE SER REDUZIDA EM 1 RODADA
            jogador_rodada.set_insano(jogador_rodada.dano_extra, jogador_rodada.rodadas - 1, jogador_rodada.has_insano)

        print(adversario.nome, 'estava invulnerável')
        # A DURAÇÃO DA ESTRELA ADVERSÁRIA DEVE SER REDUZIDA EM 1 RODADA
        adversario.set_estrela(adversario.invuneral - 1, adversario.has_estrela)
        # DRENA A MANA DO ADVERSÁRIA (OBS: MANA_DREN PODE SER 0)
        adversario.set_mana(-1 * jogador_rodada.mana_dren)
    elif jogador_rodada.insano: # CASO SOMENTE O JOGADOR TENHA A CARTA INSANA ATIVADA:
        print(jogador_rodada.nome, 'deu um ataque insano em', adversario.nome)
        calculo_ataque(jogador_rodada, adversario, jogador_rodada.dano_extra)
        jogador_rodada.set_insano(jogador_rodada.dano_extra, jogador_rodada.rodadas - 1, jogador_rodada.has_insano)
    else: # OU ENTÃO O CASO COMUM ~ ATAQUE BÁSICO:
        print(jogador_rodada.nome, 'atacou', adversario.nome)
        calculo_ataque(jogador_rodada, adversario)

def calculo_ataque(jogador_rodada, adversario, dano_adicional = 0):
    ''' FAZ O CÁLCULO DO ATAQUE REALIZADO, DESCONTANDO O DANO BLOQUEADO, SOMANDO O DANO ADICIONAL.
        ALÉM DO CONTROLE DAS CARTAS INSANAS~ESTRELA

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         adversario -- ADVERSÁRIO DA RODADA
         dano_adicional -- DANO EXTRA QUE O JOGADOR DA RODADA PODE CAUSAR NO ADVERSÁRIO
     '''

    # CÁLCULO DO DADO = DANO JOGADOR + SEU DANO ADICIONAL - DANO BLOQUEADO PELO ADVERSÁRIO
    dano = -1 * ((jogador_rodada.dano + dano_adicional) -
            int(((jogador_rodada.dano + dano_adicional) * adversario.bloqueio) / 100))

    adversario.set_vida(dano)

    if jogador_rodada.drenagem: # SE TIVER UMA CARTA DE DRENAGEM A MANA DO ADVERSÁRIO TAMBÉM SOFRE DESCONTO
        adversario.set_mana(-1 * jogador_rodada.mana_dren)

def valida_carta(jogador_rodada, carta):
    ''' FAZ UMA VALIDAÇÃO ANTES DE EVENTUALMENTE SALVAR/ATIVAR AS CARTAS INSANA~ESTRELA~DRENAGEM

     PARÂMETROS:
     jogador_rodada -- JOGADOR DA RODADA
     carta -- CARTA ENCONTRADA PELO JOGADOR

     RETORNA:
     TRUE -- CARTA NÃO PODE SER SALVA POIS O JOGADOR JÁ POSSUI OU A ATIVOU
     FALSE -- CARTA PODE SER SALVA POIS O JOGADOR NÃO POSSUI OU A ATIVOU
     '''

    # VERIFICA: SE CARTA ACHADA = I (INSANA), S (ESTRELA), D (DRENAGEM)
    # E O JOGADOR JÁ POSSUIR UMA (GUARDADA OU ATIVA) O USUÁRIO DEVER NOTIFICADO E RETORNA TRUE ~ IMPEDINDO PROCESSOS SEGUINTES
    if 'I' in carta and (jogador_rodada.has_insano or jogador_rodada.insano):
        print(jogador_rodada.nome, 'já possui a carta Insano')
        return True
    elif 'S' in carta and (jogador_rodada.has_estrela or jogador_rodada.estrela):
        print(jogador_rodada.nome, 'já possui a carta Estrela')
        return True
    elif 'D' in carta and jogador_rodada.drenagem:
        print(jogador_rodada.nome, 'já possui a carta Drenagem')
        return True

    return False # SENÃO RETORNA FALSE E PERMITE A CONTINUAÇÃO DO PROCESSO DE ARMAZENAMENTO DA NOVA CARTA

def ativa_imediato(jogador_rodada, carta):
    ''' APLICA OS EFEITOS DAS RESPECTIVAS CARTAS DE ATIVAÇÃO IMEDIATA ENCONTRADA

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA DE ATIVAÇÃO ENCONTRADA
     '''

    # VERIFICA QUAL É O CARACTER DA CARTA MÁGICA ENCONTRADA E APLICA O RESPECTIVO EFEITO
    if carta[1] == 'E':
        jogador_rodada.set_mana(int(carta[2])) # ADICIONA MANA AO USUÁRIO
    elif carta[1] == 'D':
        jogador_rodada.set_drenagem(True, int(carta[2])) # ATIVA O EFEITO DE DRENAGEM
    elif int(carta[2]) <= int(jogador_rodada.mana): # SE O USUÁRIO TIVER MANA, ATIVA AS SEGUINTES CARTAS:
        if carta[1] == 'C':
            jogador_rodada.set_vida(int(carta[3])) # ADICIONA VIDA
        elif carta[1] == 'F':
            jogador_rodada.set_dano(int(carta[3])) # ADICIONA DANO
        else:
            jogador_rodada.set_bloqueio(int(carta[3])) # ADICIONA BLOQUEIO

        jogador_rodada.set_mana(-1 * int(carta[2])) # POR FIM, SUA MANA É DESCONTADA
    else:
        print(jogador_rodada.nome, 'não possui mana suficiente para a mágica') # CASO NÃO TENHA MANA, O JOGADOR É AVISADO

def imprime_carta(jogador_rodada, carta):
    ''' IMPRIME QUAL CARTA FOI ENCONTRADA PELO USUÁRIO

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA ENCONTRADA PELO JOGADOR
     '''

    # VERIFICA QUAL É O CARACTER DA CARTA PARA IMPRIMIR A RESPECTIVA MENSAGEM
    if carta == 'C':
        nome = 'Cura'
    elif carta == 'F':
        nome = 'Força'
    elif carta == 'P':
        nome = 'Proteção'
    elif carta == 'E':
        nome = 'Éter'
    elif carta == 'D':
        nome = 'Drenagem'
    elif carta == 'I':
        nome = 'Insano'
    else:
        nome = 'Estrela'

    print(jogador_rodada.nome, 'encontrou a carta', nome)

def ativa_insano(jogador_rodada, carta):
    ''' APLICA TODOS OS EFEITOS DA CARTA INSANA ENCONTRADA

     PARÂMETROS:
        jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA INSANA ENCONTRADA PELO JOGADOR
     '''

    jogador_rodada.set_mana(-1 * int(carta[2]))
    # ATIVA A CARTA INSANA: DANO EXTRA, NUM. RODADAS, HAS_INSANO = FALSE (DEIXA DE TER UMA CARTA SALVA)
    jogador_rodada.set_insano(int(carta[4]), int(carta[3]), False)
    print(jogador_rodada.nome, 'ativou a carta Insano')

def ativa_estrela(jogador_rodada, carta):
    ''' APLICA TODOS OS EFEITOS DA CARTA ESTRELA ENCONTRADA

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA ESTRELA ENCONTRADA PELO JOGADOR
     '''

    jogador_rodada.set_mana(-1 * int(carta[2]))
    # ATIVA A CARTA ESTRELA: NUM. RODADAS INVUNERÁVEL, HAS_ESTRELA = FALSE (DEIXA DE TER UMA CARTA SALVA)
    jogador_rodada.set_estrela(int(carta[3]), False)
    print(jogador_rodada.nome, 'ativou a carta Estrela')

def ativa_carta_especial(jogador_rodada, carta):
    ''' AVALIA SE O JOGADOR TEM TOTAL CAPACIDADE DE ATIVAR A CARTA INSANA~ESTRELA ENCONTRADA

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA ENCONTRADA PELO JOGADOR
     '''

    # BLOCO QUE VÁLIDA O CENÁRIO DE ATIVAÇÃO DA CARTA INSANA
    if len(jogador_rodada.vet_insano) > 0 and carta == 'I': # SE A LISTA 'INSANA' TEM ALGUM ITEM:
        if jogador_rodada.mana >= int(jogador_rodada.vet_insano[2]) and not jogador_rodada.insano:
            # SE O JOGADOR POSSUI MANA E JOGADOR NÃO ESTÁ NA CONDIÇÃO INSANA: ATIVA ->
            ativa_insano(jogador_rodada, jogador_rodada.vet_insano)
        elif jogador_rodada.insano:
            print(jogador_rodada.nome, 'já ativou a carta Insano')
        else:
            print(jogador_rodada.nome, 'não possui mana suficiente para a mágica')
    elif len(jogador_rodada.vet_insano) == 0 and carta == 'I':
        print(jogador_rodada.nome, 'não possui a carta Insano')

    # BLOCO QUE VÁLIDA O CENÁRIO DE ATIVAÇÃO DA CARTA ESTRELA
    if len(jogador_rodada.vet_estrela) > 0 and carta == 'S':
        if jogador_rodada.mana >= int(jogador_rodada.vet_estrela[2]) and not jogador_rodada.estrela:
            # SE O JOGADOR POSSUI MANA E JOGADOR NÃO ESTÁ NA CONDIÇÃO ESTRELA: ATIVA ->
            ativa_estrela(jogador_rodada, jogador_rodada.vet_estrela)
        elif jogador_rodada.estrela:
            print(jogador_rodada.nome, 'já ativou a carta Estrela')
        else:
            print(jogador_rodada.nome, 'não possui mana suficiente para a mágica')
    elif len(jogador_rodada.vet_estrela) == 0 and carta == 'S':
        print(jogador_rodada.nome, 'não possui a carta Estrela')

def salva_inventario(jogador_rodada, carta):
    ''' SALVA NOS RESPECTIVO INVENTÁRIO A CARTA INSANA~ESTRELA. POSSIBILITANTO SEU USO POSTERIORMENTE

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         carta -- CARTA ENCONTRADA PELO JOGADOR
     '''

    # SALVA A CARTA NA RESPECTIVA LISTA
    if carta[1] == 'I':
        jogador_rodada.set_vetor_insano(carta)
        jogador_rodada.has_insano = True
    else:
        jogador_rodada.set_vetor_estrela(carta)
        jogador_rodada.has_estrela = True

def acoes(jogador_rodada, adversario):
    ''' VÁLIDA SE A AÇÃO QUE O USUÁRIO ESTÁ TENTANDO FAZER É VÁLIDA. ACIONANDO OS EVENTOS REFERENTES A AÇÃO DESEJADA

     PARÂMETROS:
         jogador_rodada -- JOGADOR DA RODADA
         adversario -- ADVERSÁRIO DA RODADA
     '''

    magias_base = ['I', 'S']

    while True:
        acoes = input('').split(' ')

        if 'X' in acoes: # SE A AÇÃO CONTER UM X ~ ELA É DO TIPO MX, ENTÃO:
            print(jogador_rodada.nome, 'não encontrou nenhuma carta')
        elif 'A' in acoes: # A ~ ATAQUE
            ataque(jogador_rodada, adversario)
            break
        elif 'M' in acoes: # SE COMEÇAR COM M, ENTÃO DEVE SER ANÁLISADA QUAL É A CARTA
            imprime_carta(jogador_rodada, acoes[1])

            if not valida_carta(jogador_rodada, acoes) and acoes[1] in magias_base:
                salva_inventario(jogador_rodada, acoes)
            elif not acoes[1] in magias_base:
                ativa_imediato(jogador_rodada, acoes)
        elif 'I' in acoes: # I ~ ATIVA INSANO
            ativa_carta_especial(jogador_rodada, acoes[0])
        elif 'S' in acoes: # S ~ ATIVA ESTRELA
            ativa_carta_especial(jogador_rodada, acoes[0])

def vitoria(heroi_snow, heroi_sunny):
    ''' VERIFICA SE ALGUM JOGADOR GANHOU APÓS A REALIZAÇÃO DE ALGUM ATAQUE, OU SEJA, VIDA ADVERSÁRIO = 0

     PARÂMETROS:
         heroi_snow -- JOGADOR DO REINO SNOW
         heroi_sunny -- JOGADOR DO REINO SUNNY

     RETORNO:
         TRUE -- CASO ALGUM USUÁRIO TENHA VIDA = 0
         FALSE -- CASO OS DOIS USUÁRIOS TENHA VIDA > 0
     '''

    if heroi_snow.vida == 0:
        print('O herói', heroi_sunny.nome, 'do reino Sunny Kingdom venceu o duelo')
        return True
    elif heroi_sunny.vida == 0:
        print('O herói', heroi_snow.nome, 'do reino Snowland venceu o duelo')
        return True

    return False

# VARIAVEIS BASICAS DO SISTEMA:
rodada = 1

nome = input('')
max_vida = int(input(''))
dano = int(input(''))
bloqueio = int(input(''))
max_mana = int(input(''))

heroi_snow = Heroi(nome, max_vida, dano, bloqueio, max_mana) # CRIA O HERÓI SNOW

nome = input('')
max_vida = int(input(''))
dano = int(input(''))
bloqueio = int(input(''))
max_mana = int(input(''))

heroi_sunny = Heroi(nome, max_vida, dano, bloqueio, max_mana) # CRIA O HERÓI SUNNY

print('O reino Snowland indicou o herói', heroi_snow.nome)
print('O reino Sunny Kingdom indicou o herói', heroi_sunny.nome)

jogada = 0
ganhador = False

while not ganhador: # ENQUANTO NÃO TIVER UM GANHADOR O JOGO OCORRERÁ
    jogadador = input('').split(' ')

    if '1' in jogadador: # SE O JOGADOR CONTER '1', ENTÃO O HERÓI SNOW JOGARÁ
        print('Rodada', str(rodada) + ': vez de', heroi_snow.nome)
        acoes(heroi_snow, heroi_sunny)
        jogada += 1

        if jogada == 2: # A CADA 2 JOGADAS TEM O FIM DE UM TURNO, O STATUS DOS HERÓIS APARECE
            print(heroi_snow)
            print(heroi_sunny)
            jogada = 0
            rodada += 1
    else: # SENÃO O HERÓI SUNNY JOGARÁ
        print('Rodada', str(rodada) + ': vez de', heroi_sunny.nome)

        acoes(heroi_sunny, heroi_snow)
        jogada += 1

        if jogada == 2: # A CADA 2 JOGADAS TEM O FIM DE UM TURNO, O STATUS DOS HERÓIS APARECE
            print(heroi_snow)
            print(heroi_sunny)
            jogada = 0
            rodada += 1

    if vitoria(heroi_snow, heroi_sunny):
        print(heroi_snow)
        print(heroi_sunny)
        ganhador = True