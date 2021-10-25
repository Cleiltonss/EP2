from random import shuffle
def cria_pecas():
    lista_pecas = []
    dentro_lista = []
    for c in range(7):
        for d in range(c, 7):
            dentro_lista = [c, d]
            if dentro_lista not in lista_pecas:
                lista_pecas.append(dentro_lista)
    shuffle(lista_pecas)
    return lista_pecas  
