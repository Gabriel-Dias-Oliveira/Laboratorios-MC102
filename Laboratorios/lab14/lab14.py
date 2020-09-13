# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB14: APLICAÇÃO DE RASTREIO DE FAKE NEWS ('QUEM RECEBEU?').

def busca_usuarios(qtd_usuarios, recebeu_fake):
    '''FUNÇÃO RECURSIVA QUE MAPEIA A REDE DE FAKE NEWS

    PARÂMETRO:
        qtd_usuarios -- RECEBE A QUANTIDADE DE USUÁRIOS (NÚMERO DE VEZES QUE TERÁ RECURSÃO)
        recebeu_fake -- CONJUNTO COM O NOME DE TODOS QUE RECEBERAM FAKE NEWS

    RETURN:
        recebeu_fake -- NOME DE QUEM RECEBEU FAKE NEWS (CASO BASE DA RECURSÃO)
    '''

    # SE A QUANTIDADE DE USUÁRIOS É '0', ENTÃO JÁ FORAM ANALISADAS TODAS AS ENTRADAS!
    # DEVOLVE O CONJUNTO DE NOMES DE QUEM RECEBEU FAKE NEWS
    if qtd_usuarios == 0:
        return recebeu_fake
    else:
        acao_usuario = input().strip().split(' ')

        # SE A ENTRADA FOR DO TIPO '1' TEMOS OS GERADORES DE FAKE NEWS
        # TODOS SÃO SALVOS NO CONJUNTO DE NOMES
        if int(acao_usuario[0]) == 1:
            for user in acao_usuario[1:]:
                recebu_fake.add(user)
        elif int(acao_usuario[0]) == 2:
            # SE A ENTRADA FOR DO TIPO '2' TEMOS O COMPARTILHAMENTO DA FAKE NEWS
            # A PARTIR DA 3ª POSIÇÃO TEMOS TODOS OS AMIGOS QUE RECEBRAM A FAKE NEWS
            for user in acao_usuario[2:]:
                recebeu_fake.add(user)

        return busca_usuarios(qtd_usuarios - 1, recebu_fake)

qtd_usuarios = int(input())
recebu_fake = set()

usuarios_fake = busca_usuarios(qtd_usuarios, recebu_fake)

print('Ordenação por nome')

usuarios_fake = sorted(list(usuarios_fake)) # ORDENA A LISTA!

for user_name in usuarios_fake:
    print(user_name)