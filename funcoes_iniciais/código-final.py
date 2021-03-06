from ep2_cria_pecas import cria_pecas
from ep2_inicia_jogo import inicia_jogo
from ep2_adiciona_na_mesa import adiciona_na_mesa
from ep2_possiveis_posicoes import posicoes_possiveis
from ep2_quem_ganhou import verifica_ganhador
from ep2_soma_pecas import soma_pecas
from ep2_pinta_colorido import printa_colorido
from random import randint
from time import sleep
import sys

cores = {'azul':     '\033[34m',                        #dicionário contendo cores
         'amarelo':  '\033[33m', 
         'vermelho': '\033[31m', 
         'verde':    '\033[32m',
         'roxo':     '\033[35m',
         'ciano':    '\033[36m',
         'preto':    '\033[30m',
         'limpa':    '\033[m'
        }

print('-=' * 50)
sleep(1)
print(f'{cores["verde"]}BEM{cores["limpa"]} {cores["roxo"]}VINDO{cores["limpa"]} {cores["amarelo"]}AO JOGO DO{cores["limpa"]} {cores["vermelho"]}DOMINÓ{cores["limpa"]}')
sleep(1)
print('-=' * 50)
sleep(1)
inicia = input(f'\nVocê gostaria de jogar?\nDigite {cores["verde"]}sim{cores["limpa"]} para continuar e {cores["vermelho"]}não{cores["limpa"]} para parar: ').strip().lower()
sleep(1)
while inicia not in 'não':
    print('-=' * 50)
    sleep(1)
    print(f'\nEntão vamos jogar! {cores["verde"]}:){cores["limpa"]}\n')
    lista_pecas = cria_pecas() #peças criadas
    n_jogadores = int(input(f'Qual o número de jogadores que irão participar? Por favor, escolha entre {cores["amarelo"]}2{cores["limpa"]} à {cores["amarelo"]}4{cores["limpa"]} jogadores: '))
    sleep(1)
    print('-=' * 50)
    sleep(1)
    print(f'Agora que foram escolhidos os {n_jogadores} jogadores, podemos começar o jogo... Divirta-se!')
    sleep(2)
    for c in range(3, 0, -1):
        print(c)
        sleep(1)
    print(f'{cores["amarelo"]}Prepare-se!{cores["limpa"]}')
    sleep(1)
    print('-=' * 50)
    sleep(1)


    #Início do Jogo
    dic_jmm = inicia_jogo(n_jogadores, lista_pecas)             #dicionario com jogador, monte e peças
    jogador_inicial = randint(0, n_jogadores - 1)               #define o indice do jogador inicial
    jogador = jogador_inicial                                   #jogador é uma variável que vai representar quem está jogando na rodada
    jogo_fim = False                                            #define que o jogo está rodando
    joga_peca = 0                                               #cria a variavel da peça a ser jogada na mesa em cada rodada
    joga_ou_passa = 0
    pontos = []                                                 #um dicionário com os pontos de cada jogador para classificação e caso dê empate
    mao = dic_jmm['jogadores']                                  #retorna um dic com as mãos do jogadores da partida
    mesa = dic_jmm['mesa']                                      #retorna uma lista vazia de inicio
    monte = dic_jmm['monte']                                    #retorna uma lista com o monte de inicio da partida


    while jogo_fim != True:                                     #Se o jogo não tiver acabado
        
        #Vemos a mesa e quem está jogando primeiro
        if joga_ou_passa == 0:
            if len(mesa) > 0:
                sleep(0.5)
                print(f'MESA:\n{printa_colorido(mesa)}\n ')
                sleep(0.5)
            else:
                sleep(0.5)
                print(f'MESA:\n{mesa}\n')
                sleep(0.5)
            if jogador == 0:
                sleep(0.5)
                print(f'\nSua vez! Suas peças são:\n')
                # for c in mao[jogador]:
                #     sys.stdout.write(f'{c} ')
                print(f'{printa_colorido(mao[jogador])}  ')
                print('\n')
                for c in range (0, len(mao[jogador])):
                    sys.stdout.write(f'  {cores["ciano"]}{c + 1}{cores["vermelho"]}ª{cores["limpa"]}{cores["limpa"]}   ')
            else:
                print(f'\nO Jogador {cores["verde"]}{jogador + 1}{cores["limpa"]} possui {cores["amarelo"]}{len(mao[jogador])}{cores["limpa"]} peça(s)!')
            
        #Agora, cheacamos se o jogador tem peças que podem ser jogadas e qual vai ser adicionada na mesa
        pecas_possiveis = posicoes_possiveis(mesa, mao[jogador])
        
        if pecas_possiveis == []:
            
            if monte != []:                                          #jogador começa a puxar do monte
                joga_ou_passa = 1
                sleep(1)
                print(f'\nNão há peças possíveis. {cores["vermelho"]}PEGANDO DO MONTE!{cores["limpa"]}\n')
                mao[jogador].append(monte[0])
                del monte[0]
            else:                                                    #o monte acabou, a contagem de empate incrementa
                sleep(1)
                print(f'\nNão há peças no monte! {cores["vermelho"]}PASSANDO A VEZ!{cores["limpa"]}\n')
                joga_ou_passa = 0
                if jogador == n_jogadores - 1:
                    jogador = 0
                else:
                    jogador += 1
                empate += 1
            if empate == n_jogadores: #Quer dizer que todos os jogadores precisaram pegar do monte, mas ele está vazio
                jogo_fim = True     #Então, a partida acaba
                for j in mao.keys():
                    pontos.append(soma_pecas(mao[j]))   #Uma tabela dos pontos de cada jogador
                ganha = min(pontos)
                vencedor = []
                for j in mao.keys():
                    if pontos[j] == ganha:
                        vencedor.append(j + 1)
                if len(vencedor) > 1:
                    print(f'Foi empate entre os jogadores: {cores["amarelo"]}{vencedor}{cores["limpa"]}')
                else:
                    print(f'Venceu o jogador: {cores["verde"]}{vencedor}{cores["limpa"]}')
        
        
        else:                                                        #O jogador possui ao menos uma peça possivel de ser jogada    
            empate = 0                                               #A contagem de empate deve ser resetada então
            joga_ou_passa = 0

            if jogador == 0:                                         #As açoes do jogador ZERO são representadas pelo jogador    
                
                escolha = ''
                for num in pecas_possiveis:
                    escolha += f'- {cores["verde"]}{num+1}{cores["limpa"]} '                         #Informa ao jogador humano as peças que ele pode jogar
                escolha = escolha[1:]
                sleep(0.5)
                joga_peca = int(input(f'\n\nAs peças possíveis de escolha são: {escolha}\nEscolha a peça que você quer jogar: ')) -1 #retorna o indice da peça que ele quer jogar
                if joga_peca not in pecas_possiveis:
                    while joga_peca not in pecas_possiveis:
                        print('Parece-me que você escolheu uma peça que não pode ser jogada!\nQue deselegante!\nEscolha de novo!')
                        joga_peca = int(input(f'\n\nAs peças possíveis de escolha são: {escolha}\nEscolha a peça que você quer jogar: ')) -1
            
            
            else:                                                   #O computador escolhe aleatoriamente uma das peças possiveis para jogar
                joga_peca = pecas_possiveis[randint(0, len(pecas_possiveis)-1)]
            pc_peca = [mao[jogador][joga_peca]]
            mesa = adiciona_na_mesa(mao[jogador][joga_peca], mesa)   #A mesa agora recebe a peça que jogaram
            sleep(0.5)
            print(f'\nColocou: {printa_colorido(pc_peca)}\n')
            sleep(0.5)
            del mao[jogador][joga_peca]                             #É informado a todos os jogadores qual peça foi jogada
            
            
            vencedor = verifica_ganhador(mao)                           #Checa se há algum ganhador nessa rodada
            if vencedor != -1:
                jogo_fim = True
                if jogador != 0:
                    print(f'Venceu o jogador: {cores["verde"]}{jogador + 1}{cores["limpa"]}')
                else:
                    print(f'{cores["verde"]}Parabéns!{cores["limpa"]} Você venceu o jogo!')
            
            
            elif jogador == n_jogadores-1:                         #Como não há ganhador, passa a vez
                jogador = 0
            else:
                jogador+=1                                         #Garante que cada rodada vai ser cíclica 
    
    
    inicia = input(f'\nQuer jogar novamente?\n{cores["verde"]}sim{cores["limpa"]} para continuar e {cores["vermelho"]}não{cores["limpa"]} para parar.')
print(f'\nFoi um prazer jogar com você!\nAté a próxima! {cores["ciano"]}:){cores["limpa"]}') 