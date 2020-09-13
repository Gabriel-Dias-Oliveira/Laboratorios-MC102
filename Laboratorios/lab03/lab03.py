# GABRIEL DIAS DE OLIVEIRA, RA: 176495
# LAB03: PROGRAMA PARA AVALIAR QUAL O TRATAMENTO IDEAL PARA UMA PESSOA COM SUSPEITA DE COVID-19.

# O PROGRAMA BASEIA-SE EM IF's PARA A TOMADA DAS DECISÕES.
# CADA ENTRADA GERA UM NOVO CENÁRIO 'DIFERENTE'

sintomas = int(input('Você apresenta pelo menos 4 dos sintomas principais do COVID-19? '
      '(Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)\n'
      '(1) sim\n'
      '(2) não\n'))

if sintomas == 1:
      testado = int(input('Você realizou o teste do COVID-19 desde que esses sintomas surgiram?\n'
            '(1) não\n'
            '(2) sim, deu positivo\n'
            '(3) sim, deu negativo\n'))

      if testado == 1:
            print('Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19')
      elif testado == 2:
            estado_grave = int(input('Você se encontra em estado grave de saúde?\n'
                  '(1) sim\n'
                  '(2) não\n'))

            if estado_grave == 1:
                  print('Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado')
            elif estado_grave == 2:
                  grupo_risco = int(input(
                        'Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; '
                        'fumante; pessoa de extremos de idade, seja criança ou idoso)\n'
                        '(1) sim\n'
                        '(2) não\n'))

                  if grupo_risco == 1:
                        print('Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado')
                  elif grupo_risco == 2:
                        print('Baseado em suas respostas, a orientação é que você entre em isolamento')
                  else:
                        print('Opção inválida, recomece a avaliação')
            else:
                  print('Opção inválida, recomece a avaliação')
      elif testado == 3:
            print('Baseado em suas respostas, a orientação é que você permaneça em distanciamento social')
      else:
            print('Opção inválida, recomece a avaliação')
elif sintomas == 2:
      contato_doente = int(input('Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?\n'
            '(1) sim\n'
            '(2) não\n'))

      if contato_doente == 1:
            print('Baseado em suas respostas, a orientação é que você entre em isolamento')
      elif contato_doente == 2:
            print('Baseado em suas respostas, a orientação é que você permaneça em distanciamento social')
      else:
            print('Opção inválida, recomece a avaliação')
else:
      print('Opção inválida, recomece a avaliação')