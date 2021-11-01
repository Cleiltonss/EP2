from ep2_cria_pecas import cria_pecas
from ep2_inicia_jogo import inicia_jogo
from ep2_adiciona_na_mesa import adiciona_na_mesa
from ep2_possiveis_posicoes import posicoes_possiveis
from ep2_quem_ganhou import verifica_ganhador
from ep2_soma_pecas import soma_pecas
from random import randint
from time import sleep, strftime

inicia = input('Quer iniciar um jogo? (sim/não)')
sleep(1)
while inicia != 'não':
    lista_pecas = cria_pecas() #peças criadas
    n_jogadores = int(input('Qual o número de jogadores [2/3/4 jogadores]? '))
    print('-=' * 40)
    print(f'Agora que foram escolhidos os {n_jogadores} jogadores, podemos começar o jogo!')
    sleep(1)
    print('Divirta-se! :)')
    sleep(1)
    print('-=' * 40)
    sleep(1)


    #Início do Jogo
    dic_jmm = inicia_jogo(n_jogadores, lista_pecas) #dicionario com jogador, monte e peças
    jogador_inicial = randint(0, n_jogadores - 1)
    jogador = jogador_inicial
    jogo_fim = False
    joga_peca = 0
    mao = dic_jmm['jogadores']#retorna um dic de keys '0' a '3'
    mesa = dic_jmm['mesa']#retorna uma lista cheia ou vazia
    monte = dic_jmm['monte']#retorna uma lista vazia
    while jogo_fim != True:
        if jogador == 0:
            print('Jogador: Você com {} peça(s)'.format(len(mao[jogador])))
        else:
            print('Jogador: {} com {} peça(s)'.format((jogador+1),(len(mao[jogador]))))
        peg_monte = True
        while peg_monte:
            pecas_possiveis = posicoes_possiveis(mesa,mao[jogador])
            if pecas_possiveis == []:
                if monte != []:
                    print('Não tem peças possíveis. PEGANDO DO MONTE!')
                    mao[jogador].append(monte[0])
                    del monte[0]
                else:
                    print('Não há peças no monte! PASSANDO A VEZ!')
                    peg_monte = False
            else:
                escolha = ''
                for num in pecas_possiveis:
                    escolha += ',{}'.format(num+1)
                if jogador == 0:
                    joga_peca = int(input('Escolha qual peca jogar: {}'.format(escolha))) -1
                else:
                    joga_peca = randint(0,len(pecas_possiveis)-1)
                    
                peg_monte = False
                
                mesa = adiciona_na_mesa(mao[jogador][joga_peca],mesa)
                del mao[jogador][joga_peca]
        vencedor = verifica_ganhador(mao)
        if vencedor == -1:
            jogador+=1        
            if jogador==n_jogadores:
                jogador =0
        else:
            jogo_fim = True
            print('Venceu o jogador: {}'.format(jogador))
    inicia = input('Quer iniciar um jogo? (sim/não)')
print('Foi um prazer jogar com vc!')                    