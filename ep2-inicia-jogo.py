#função inicia jogo
from random import shuffle, randint
import pecas

def inicia_jogo(n_jogad):
    lista_pecas = []
    lista_pecas.append(shuffle(pecas))
    pecas_jogad = []
    quebra_laco = True
    while quebra_laco:
        peca_aleatoria = lista_pecas(randint(0, 27))
        if peca_aleatoria not in pecas_jogad:
            pecas_jogad.append(peca_aleatoria)
        if len(pecas_jogad) == 7:
            quebra_laco = False



    
