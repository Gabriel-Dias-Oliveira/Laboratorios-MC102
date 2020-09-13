# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB10: CONSTRUÇÃO DE UM RESPONDENATOR 300 ~ ENCONTRA A MELHOR RESPOSTA PARA UMA PERGUNTA.

from PontStop import * # IMPORTAÇÃO DO ARQUIVO COM STOP WORDS ~ PONTUAÇÕES E PALAVRAS QUE NÃO CARACTERIZAM UM TEXTO

def padronizacao(palavra):
    '''PADRONIZA O TEXTO COM LETRAS MINÚSCULAS

    PARÂMETROS:
        palavra -- FRASE A SER PADRONIZADA

    RETURN:
        PALAVRA EM MINÚSCULAS
    '''
    return palavra.lower()

def tokenizacao(palavra):
    '''TOKENIZAÇÃO DO TEXTO SEPARANDO-O A PARTIR DOS ESPAÇOS (' ')

    PARÂMETROS:
        palavra -- FRASE A SER SEPARADA

    RETURN:
        LISTA DE PALAVRAS OBTIDADAS
    '''
    return palavra.split(' ')

def limpeza(conjunt_frase):
    '''LIMPEZA ~ REMOVE TODAS AS STOP WORDS

    PARÂMETROS:
        conjunt_frase -- LISTA DE PALAVRAS DA FRASE

    RETURN:
        LISTA DE PALAVRAS SEM STOP WORDS
    '''

    # FOR PARA PERCORRER AS PALAVRAS DA LISTA E AS PONTUAÇÕES
    for x in range(len(conjunt_frase)):
        for caracter in pontuacoes:
            # SUBSTITUI TODAS AS PONTUAÇÕES POR '' ~ REMOVENDO-A
            conjunt_frase[x] = conjunt_frase[x].strip().replace(caracter, '')

    conjunt_frase = set(conjunt_frase)
    conjunt_frase.discard('') # DESCARTA OS ESPAÇOS

    return list(conjunt_frase.difference(stop_words, '')) # REMOVE TODAS AS STOP WORDS

def reescrita(conjunt_frase, dicionario):
    '''REESCRITA ~ SUBSTITUI TODAS AS PALAVRAS QUE POSSUEM UM SINÔNIMO NO DICIONÁRIO

    PARÂMETROS:
        conjunt_frase -- LISTA DE PALAVRAS DA FRASE
        dicionario -- ARMAZENA OS SINÔNIMOS, QUE SUBSTITUIRÃO AS PALAVRAS DO CONJUNTO

    RETURN:
        LISTA DE PALAVRAS REESCRITA
    '''

    # PERCORRE O DICIONÁRIO VENDO SE A PALAVRA DA LISTA POSSUÍ SINÔNIMO
    for x in range(len(conjunt_frase)):
        for c, v in dicionario.items():
            if conjunt_frase[x] in v:
                # SE POSSUIR O SUBSTITUI
                conjunt_frase[x] = conjunt_frase[x].replace(conjunt_frase[x], c)

    return conjunt_frase

def descritor(conjunt_frase):
    '''GERA O CONJUNTO DESCRITOR DA FRASE

    PARÂMETROS:
        conjunt_frase -- LISTA DE PALAVRAS DA FRASE

    RETURN:
        CONJUNTO DE PALAVRAS
    '''
    return set(conjunt_frase)

# VARIÁVEIS BASE DO SISTEMA

sinonimos = input()
resposta_ideal = '42' # RESPOSTA PADRÃO
dicionario = {}
respostas = []

while sinonimos != '}': # CARÁCTER QUE INDICA O FIM DO DICIONÁRIO
    sinonimos = input()

    if sinonimos != '}':
        sinonimos = sinonimos.split(':')
        chave = sinonimos[0]
        sinonimos = (''.join(sinonimos[1:])).split(',')

        dicionario[chave] = sinonimos

pergunta_integral = input() # GUARDA A PERGUNTA NA FORMA COMO FOI FEITA

# PASSA A PERGUNTA POR TODAS AS ESTAPAS DE MUDANÇAS
pergunta = pergunta_integral.strip()
pergunta = padronizacao(pergunta)
pergunta = tokenizacao(pergunta)
pergunta = limpeza(pergunta)
pergunta = reescrita(pergunta, dicionario)
pergunta = descritor(pergunta)

numero_respostas = int(input())

for x in range(numero_respostas):
    # RECEBE 'N' RESPOSTAS PARA A PERGUNTA
    resposta = input()
    respostas.append(resposta)

print('Descritor pergunta:', ','.join(sorted(pergunta))) # IMPRIME DESCRITOR PERGUNTA

for x in range(len(respostas)):
    # PASSA CADA RESPOSTA PELAS ETAPAS DE PADRONIZAÇÃO

    resposta = padronizacao(respostas[x])
    resposta = tokenizacao(resposta)
    resposta = limpeza(resposta)
    resposta = reescrita(resposta, dicionario)
    resposta = descritor(resposta)

    print(f'Descritor resposta {x + 1}: {",".join(sorted(resposta))}') # IMPRIME SEU DESCRITOR

    if pergunta.issubset(resposta):
        # SE A PERGUNTA FOR UM SUBCONJUNTO DA RESPOSTA, ENTÃO ELA É IDEAL
        resposta_ideal = respostas[x]

# IMPRIME A RESPOSTA IDEAL!
print(f'\nA resposta para a pergunta "{pergunta_integral}" é "{resposta_ideal}"')