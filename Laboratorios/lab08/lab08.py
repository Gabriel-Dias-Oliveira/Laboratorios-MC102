# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB08: PROGRAMA QUE POSSIBILITA O CADASTRO DE BENEFICIÁRIOS PARA A SOLICITAÇÃO DO AUXÍLIO EMERGENCIAL DO GOVERNO.

class Governo:
    """ REPRESENTAÇÃO DO GOVERNO

        ARMAZENA: BENEFICIÁRIOS, BENEFICIÁRIOS PENDENTES E RECURSOS
    """

    def __init__(self):
        self._beneficiarios = []
        self._recursos = 0
        self._benef_pend = []

    def imprime_benef(self):
        benef = 'Beneficiários atuais:'
        for x in range(len(self._beneficiarios)): # FOR PARA ARMAZENAR TODOS OS BENEFICIÁRIOS ATUAIS
            benef += '\n' + self._beneficiarios[x].cpf + ': ' + self._beneficiarios[x].nome

        return benef

    def imprime_recurso(self):
        return 'Recursos disponíveis: R$ ' + format(self.recursos, '.2f')

    @property
    def beneficiarios(self):
        return self._beneficiarios

    @beneficiarios.setter
    def beneficiarios(self, beneficiarios):
        self._beneficiarios.append(beneficiarios)

    @property
    def recursos(self):
        return self._recursos

    @recursos.setter
    def recursos(self, recursos):
        print('Recursos adicionados')
        self._recursos += recursos

    @property
    def benef_pend(self):
        return self._benef_pend

    @benef_pend.setter
    def benef_pend(self, benef_pend):
        self._benef_pend.append(benef_pend)

    def avalia_beneficiarios(self):
        empregos = ['desempregad', 'autonom', 'microempreendedo', 'microempreendedor']

        for benef in self._benef_pend: # VALIDA A LISTA DE BENEFICIÁRIOS PENDENTES
            if  (benef.idade >= 18) and (benef.emprego[0:-1] in empregos) and\
                (benef.status != 'Negado' or benef.status != 'Auxílio finalizado') and\
                    ((benef.renda_per_capita <= 522.50) or (benef.renda_total <= 3135)):
                # VALIDA SE O USUÁRIO POSSUI TODOS OS REQUISITOS PARA SER APROVADO

                self.beneficiarios = benef
                benef.status = 'Com auxílio' # APROVADO
            else:
                benef.status = 'Negado' # REPROVADO

        self._benef_pend.clear()
        print('Beneficiários avaliados\nLista de beneficiários atualizada')

    def envia_recursos(self):
        if (len(self._beneficiarios) * 600) > self._recursos or (self._recursos == 0 and
                                                                 len(self._beneficiarios) != 0):
            # CASO OS RECURSOS DO GOVERNO SEJA < QUE O VALOR A SER PAGO AOS BENEFICIÁRIOS
            for x in range(len(self._beneficiarios)): # PERCORRE A LISTA PAGANDO POR ORDEM DE SOLICITAÇÃO
                if self._recursos >= 600:
                    self._beneficiarios[x].temp_recebe += 1
                    self._recursos -= 600
                    self._beneficiarios[x].auxilio += 600

                    if self._beneficiarios[x].temp_recebe >= 3:
                        self._beneficiarios[x].status = 'Auxílio finalizado'
                        self._beneficiarios.remove(self._beneficiarios[x])

            return 'Recursos insuficientes'

        self._recursos -= (len(self._beneficiarios) * 600)

        for x in range(len(self._beneficiarios)):
            self._beneficiarios[x].temp_recebe += 1
            self._beneficiarios[x].auxilio += 600

            if self._beneficiarios[x].temp_recebe >= 3:
                self._beneficiarios[x].status = 'Auxílio finalizado'
                self._beneficiarios.remove(self._beneficiarios[x])

        return 'Auxílio mensal enviado'

class Beneficiario():
    """ REPRESENTAÇÃO DO GOVERNO

        ARMAZENA: INFORMAÇÕES PESSOAIS (PERTINENTES AO AUXÍLIO), ALÉM DO STATUS DO BENEFICIÁRIO EM RELAÇÃO A SOLICITAÇÃO
    """

    def __init__(self, nome = " ", cpf = "", status = "Perfil incompleto", renda_per_capita = 0, renda_total = 0, idade = 0, emprego = "", temp_recebe = 0):
        self._nome = nome
        self._cpf = cpf
        self._status = status
        self._renda_per_capita = renda_per_capita
        self._renda_total = renda_total
        self._idade = idade
        self._emprego = emprego
        self._temp_recebe = temp_recebe
        self._auxilio = float(0)

    @property
    def auxilio(self):
        return self._auxilio

    @auxilio.setter
    def auxilio(self, auxilio):
        self._auxilio = auxilio

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) >= 11: # FORMATA O CPF, CASO ELE VENHA SEM FORMATAÇÃO ALGUMA (OU PARCIAL)
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            self._cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
        else:
            self._cpf = cpf

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def renda_per_capita(self):
        return self._renda_per_capita

    @renda_per_capita.setter
    def renda_per_capita(self, renda_per_capita):
        self._renda_per_capita = renda_per_capita

    @property
    def renda_total(self):
        return self._renda_total

    @renda_total.setter
    def renda_total(self, renda_total):
        self._renda_total = renda_total

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def emprego(self):
        return self._emprego

    @emprego.setter
    def emprego(self, emprego):
        self._emprego = emprego

    @property
    def temp_recebe(self):
        return self._temp_recebe

    @temp_recebe.setter
    def temp_recebe(self, temp_recebe):
        self._temp_recebe = temp_recebe

    def soclicitar_beneficio(self, governo):
        if beneficiario.status == 'Perfil completo': # PERFIL COMPLETO ~ PODE SOLICITAR AUXÍLIO
            print('Auxílio solicitado, aguarde avaliação')
            beneficiario.status = 'Pendente'
            governo.benef_pend = beneficiario
        elif beneficiario.status == 'Perfil incompleto':
            print('Complete seu perfil e tente novamente')

    def recebe_auxilio(self, num_conta):
        # TRANSFERE O AUXÍLIO RECEBIDO (E ACUMULADO) ATÉ O MOMENTO PARA UMA 'CONTA PESSOAL'
        msg = 'Valor de R$ ' + format(float(self.auxilio), '.2f') + ' transferido para a conta corrente ' + num_conta
        self.auxilio = 0
        return msg

    def __str__(self):
        return 'Nome completo: ' + self._nome +\
                '\nStatus: ' + self._status +\
                '\nCPF: ' + self._cpf +\
                '\nRenda per capita: R$ ' + format(self._renda_per_capita, '.2f') +\
                '\nRenda total: R$ ' + format(self._renda_total, '.2f') +\
                '\nIdade: ' + str(self._idade) +\
                '\nEmprego: ' + str(self._emprego) +\
                '\nTempo de recebimento: ' + str(self._temp_recebe) + ' meses'

acao = ''.split(' ') # VARIÁVEL QUE DEFINE AS AÇÕES QUE O USUÁRIO ESCOLHEU
msgs_beneficiario = ['Nome inserido', 'CPF inserido', 'Renda per capita inserida',
                     'Renda total inserida', 'Idade inserida', 'Emprego inserido'] # MENSAGENS PADRÕES A SEREM USADAS

governo = Governo() # CRIANDO UM OBJETO DO TIPO 'GOVERNO'
beneficiarios = {} # ARMAZENARÁ QUALQUER NOVO BENEFICIÁRIO
nome = []
sobrenome = []

while acao[0].upper() != 'X': # ENQUANTO FOR != X O CÓDIGO CONTINUA A SER EXECUTADO
    acao = input('').split(' ')

    if len(acao) == 1 and acao[0].upper() == 'BENEFICIARIO': # AÇÕES BÁSICAS DE UM BENEFICIÁRIO INEXISTENTE
        beneficiario = Beneficiario()
        cadastro_info = {1: '', 2: '', 3: 0,
                         4: 0, 5: 0, 6: ''}

        imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                        10: 'Status: ' + beneficiario.status, 11: 'CPF: ' + beneficiario.cpf, 12: beneficiario}

        while acao[0].upper() != 'F': # ENQUANTO FOR != F O CÓDIGO CONTINUA A SER EXECUTADO
            acao = input('').strip().split(' ')

            try:
                if int(acao[0]) in range(1, 7): # FORMATAÇÃO PARA CASO O USUÁRIO TENHA FEITO UMA ENTRADA SEM CONTEÚDO
                    if len(acao) == 1 and (int(acao[0]) in range(1, 3) or int(acao[0]) == 6):
                        acao.append('') # SE A ENTRADA FOR DO TIPO TEXTO ~ ''
                    elif len(acao) == 1 and int(acao[0]) in range(3, 6):
                        acao.append(0) # NUMÉRICA ~ 0

                    cadastro_info[int(acao[0])] = acao[1] # O DICIONÁRIO NA POSIÇÃO ESPECÍFICA ARMAZENA ESSA INFORMAÇÃO

                    if int(acao[0]) in range(1, 3) or int(acao[0]) == 6:
                        if int(acao[0]) == 1: # SE FOR UM NOME, O CONTEÚDO É DIVIDIDO
                            nome = acao[1]
                            sobrenome = acao[2:]

                    # OS RESPECTIVOS ATRIBUTOS DO BENEFICIÁRIO ARMAZENAM ESSAS INFORMAÇÕES

                        beneficiario.nome = (f'{"".join(nome)} {" ".join(sobrenome)}').upper()
                        cadastro_info[1] = beneficiario.nome
                        beneficiario.cpf = cadastro_info[2]
                        beneficiario.emprego = cadastro_info[6].lower()
                    elif int(acao[0]) in range(3, 5): # ATRIBUTOS 'FLOAT'
                        beneficiario.renda_per_capita = float(cadastro_info[3])
                        beneficiario.renda_total = float(cadastro_info[4])
                    else: # ATRIBUTO 'INT'
                        beneficiario.idade = int(cadastro_info[5])

                    if ('' not in cadastro_info.values() and ' ' not in cadastro_info.values()) \
                            and 0 not in cadastro_info.values(): # SE NADA ESTIVER VAZIO OU '0' ~ PERFIL COMPLETO
                        beneficiario.status = 'Perfil completo'

                    print(msgs_beneficiario[int(acao[0]) - 1])

                    imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                                    10: 'Status: ' + beneficiario.status, 11: 'CPF: ' + beneficiario.cpf, 12: beneficiario}
                elif int(acao[0]) in range(9, 13):
                    print(imprime_info[int(acao[0])])
                else:
                    if int(acao[0]) == 7: # SOLICITA O AUXÍLIO
                        beneficiario.soclicitar_beneficio(governo)

                        imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                                        10: 'Status: ' + beneficiario.status, 11: 'CPF: ' + beneficiario.cpf, 12: beneficiario}
                    elif int(acao[0]) == 8: # TRANSFERE O AUXÍLIO QUE TEM ACUMULADO
                        print(beneficiario.recebe_auxilio(acao[1]))
            except: # SE UM ERRO ACONTECE O USUÁRIO DESEJA SAIR ~ DIGITANDO F
                acao[0] = 'F' # AÇÃO PASSA A VALER F ~ O PROGRAMA PARA AS OPERAÇÕES DE BENEFICIÁRIO
                beneficiarios[beneficiario.cpf] = beneficiario # GUARDA O NOVO BENEFICIÁRIO
    elif acao[0].upper() == 'GOVERNO': # AÇÕES DO GOVERNO
        imprime_gov = {3: governo.imprime_recurso(), 4: governo.imprime_benef()}

        while acao[0].upper() != 'F':
            acao = input('').split(' ')

            try:
                if int(acao[0]) in range(3, 5): # PERMITE O CONTROLE DAS INFORMAÇÕES DO GOVERNO
                    print(imprime_gov[int(acao[0])])
                elif int(acao[0]) == 2:
                    governo.recursos = float(acao[1])
                elif int(acao[0]) == 1: # AVALIA OS BENEFICIÁRIOS PENDENTES
                    governo.avalia_beneficiarios()
                elif int(acao[0]) == 5: # ENVIA O AUXÍLIO COM BASE NO RECURSO ATUAL
                    print(governo.envia_recursos())

                imprime_gov = {3: governo.imprime_recurso(), 4: governo.imprime_benef()}
            except:
                acao[0] = 'F'
    elif len(acao) > 1: # CASO CONTRÁRIO ~ O USUÁRIO ESTÁ TENTANDO ACESSAR UM BENEFICIÁRIO JÁ EXISTENTE
        # MESMAS OPERAÇÕES DO CADASTRO DO BENEFICIÁRIO, MAS ALTERANDO UM BENEFICIÁRIO JÁ CADASTRADO
        cpf = acao[1]

        if len(cpf) >= 11:
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

        beneficiario = beneficiarios[cpf]

        while acao[0].upper() != 'F':

            acao = input('').split(' ')

            try:
                imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                                10: 'Status: ' + beneficiario.status, 11: 'CPF: ' + beneficiario.cpf, 12: beneficiario}
                if int(acao[0]) in range(1, 7):
                    if len(acao) == 1 and (int(acao[0]) in range(1, 3) or int(acao[0]) == 6):
                        acao.append('')
                    elif len(acao) == 1 and int(acao[0]) in range(3, 6):
                        acao.append(0)

                    cadastro_info[int(acao[0])] = acao[1]

                    if int(acao[0]) in range(1, 3) or int(acao[0]) == 6:
                        # ALTERA AS INFORMAÇÕES DO BENEFICIÁRIO INFORMADO
                        if int(acao[0]) == 1:
                            nome = acao[1]
                            sobrenome = acao[2:]

                        beneficiario.nome = (f'{"".join(nome)} {" ".join(sobrenome)}').upper()
                        cadastro_info[1] = beneficiario.nome
                        beneficiario.cpf = cadastro_info[2]
                        beneficiario.emprego = cadastro_info[6].lower()
                    elif int(acao[0]) in range(3, 5):
                        beneficiario.renda_per_capita = float(cadastro_info[3])
                        beneficiario.renda_total = float(cadastro_info[4])
                    else:
                        beneficiario.idade = int(cadastro_info[5])

                    if ('' not in cadastro_info.values() and ' ' not in cadastro_info.values())\
                            and 0 not in cadastro_info.values():
                        beneficiario.status = 'Perfil completo'

                    print(msgs_beneficiario[int(acao[0]) - 1])

                    imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                                    10: 'Status: ' + beneficiario.status, 11: beneficiario.cpf, 12: beneficiario}
                if int(acao[0]) in range(9, 13): # IMPRIME AS RESPECTIVAS INFORAÇÕES
                    print(imprime_info[int(acao[0])])
                else:
                    if int(acao[0]) == 7: # SOLICITA O AUXÍLIO ~ CASO NÃO TENHA FEITO NO CADASTRO
                        beneficiario.soclicitar_beneficio(governo)

                        imprime_info = {9: 'Nome completo: ' + beneficiario.nome,
                                        10: 'Status: ' + beneficiario.status, 11: 'CPF: ' + beneficiario.cpf, 12: beneficiario}
                    elif int(acao[0]) == 8: # RECEBE O AUXÍLIO
                        print(beneficiario.recebe_auxilio(acao[1]))
            except:
                acao[0] = 'F'
                beneficiarios[cpf] = beneficiario