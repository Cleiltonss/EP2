from ep2_cria_pecas import cria_pecas
from ep2_inicia_jogo import inicia_jogo
from ep2_adiciona_na_mesa import adiciona_na_mesa
from ep2_possiveis_posicoes import posicoes_possiveis
from ep2_quem_ganhou import verifica_ganhador
from ep2_soma_pecas import soma_pecas
from random import randint
from time import sleep

lista_pecas = cria_pecas() #peças criadas
n_jogadores = int(input('Qual o número de jogadores [2/3/4 jogadores]? '))
print('-=' * 40)
print(f'Agora que foram escolhidos os {n_jogadores} jogadores, podemos começar o jogo!')
sleep(2)
print('Divirta-se! :)')
sleep(2)
print('-=' * 40)
sleep(1)
dic_jmm = inicia_jogo(n_jogadores, lista_pecas) #dicionario com jogador, monte e peças


#Início do Jogo
jogador_inicial = randint(0, n_jogadores - 1)
i = 0
while i < n_jogadores: 
    if jogador_inicial == 0:
        for jmm, dic_jogadores in dic_jmm.items(): #jmm são os jogadores, monte e mesa, respectivamente.
            if jmm == 'jogadores':
                for numero_jogador, pecas in dic_jogadores.items():
                    if numero_jogador == jogador_inicial:
                        escolha_peca = int(input(f'É a vez do jogador {jogador_inicial}.\nPor favor, escolha uma peça dentre suas 7: {pecas}')) 
                        
    else:
        for jmm, dic_jogadores in dic_jmm.items(): #jmm são os jogadores, monte e mesa, respectivamente.
            if jmm == 'jogadores':
                for numero_jogador, pecas in dic_jogadores.items():
                    if numero_jogador == jogador_inicial:
                        escolha_peca = randint(0, 6)
    i += 1 
                    