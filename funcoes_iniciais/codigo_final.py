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
    dic_jmm = inicia_jogo(n_jogadores, lista_pecas)     #dicionario com jogador, monte e peças
    jogador_inicial = randint(0, n_jogadores - 1)       #define o indice do jogador inicial
    jogador = jogador_inicial                           #jogador é uma variável que vai representar quem está jogando na rodada
    jogo_fim = False                                    #define que o jogo está rodando
    joga_peca = 0                                       #cria a variavel da peça a ser jogada na mesa em cada rodada
    pontos = []                                         #um dicionário com os pontos de cada jogador para classificação e caso dê empate
    mao = dic_jmm['jogadores']                          #retorna um dic com as mãos do jogadores da partida
    mesa = dic_jmm['mesa']                              #retorna uma lista vazia de inicio
    monte = dic_jmm['monte']                            #retorna uma lista com o monte de inicio da partida


    while jogo_fim != True:                             #Se o jogo n tiver acabado

        #Vemos a mesa e quem está jogando primeiro
        
        print('MESA: \n{}'.format(mesa))
        if jogador == 0:
            print('Jogador: Você com {} peça(s)'.format(len(mao[jogador])))
        else:
            print('Jogador: {} com {} peça(s)'.format((jogador+1),(len(mao[jogador]))))

        #Agora, cheacamos se o jogador tem peças que podem ser jogadas e qual vai ser adicionada na mesa
        pecas_possiveis = posicoes_possiveis(mesa,mao[jogador])

        if pecas_possiveis == []:
            if monte != []:                                          #jogador começa a puxar do monte
                print('Não tem peças possíveis. PEGANDO DO MONTE!')
                mao[jogador].append(monte[0])
                del monte[0]
            else:                                                    #o monte acabou, a contagem de empate incrementa
                print('Não há peças no monte! PASSANDO A VEZ!')
                jogador +=1
                empate+=1
            if empate==n_jogadores:                                 #Quer dizer que todos os jogadores precisaram pegar do monte, mas ele está vazio
                jogo_fim = True                                     #Então, a partida acaba
                for j in mao.keys():
                    pontos.append(soma_pecas(mao[j]))               #Uma tabela dos pontos de cada jogador
                ganha = min(pontos)
                vencedor = []
                for j in mao.keys():
                    if soma_pecas(mao[j]) == ganha:
                        vencedor.append(j+1)
                if len(vencedor)>1:
                    print('Empataram os jogadores: {}'.format(vencedor))
                else:
                    print('Venceu o jogador: {}'.format(vencedor))


        else:                                                        #O jogador possui ao menos uma peça possivel de ser jogada    
            empate = 0                                               #A contagem de empate deve ser resetada então

            if jogador == 0:                                         #As açoes do jogador ZERO são representadas pelo jogador

                escolha = ''
                for num in pecas_possiveis:
                    escolha += ',{}'.format(num+1)                   #Informa ao jogador humano as peças que ele pode jogar
                escolha = escolha[1:]

                joga_peca = int(input('Escolha qual peca jogar: {}'.format(escolha))) -1 #retorna o indice da peça que ele quer jogar


            else:                                                   #O computador escolhe aleatoriamente uma das peças possiveis para jogar
                joga_peca = randint(0,len(pecas_possiveis)-1)

            mesa = adiciona_na_mesa(mao[jogador][joga_peca],mesa)   #A mesa agora recebe a peça que jogaram
            print('Colocou: {}'.format(mao[jogador][joga_peca]))
            del mao[jogador][joga_peca]                             #É informado a todos os jogadores qual peça foi jogada

            vencedor = verifica_ganhador(mao)                           #Checa se há algum ganhador nessa rodada
            if vencedor != -1:
                jogo_fim = True
                if jogador!=0:
                    print('Venceu o jogador: {}'.format(jogador+1))
                else:
                    print('Parabéns! Você venceu o jogo!')


            elif jogador == n_jogadores-1:                         #Como não há ganhador, passa a vez
                jogador = 0
            else:
                jogador+=1                                         #Garante que cada rodada vai ser cíclica




    inicia = input('Quer iniciar um jogo? (sim/não)')
print('Foi um prazer jogar com vc!')