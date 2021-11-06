from random import shuffle
def cria_pecas():
    lista_pecas = []
    for c in range(0,7):
        for d in range(0,7):
            if [c,d] not in lista_pecas and [d,c] not in lista_pecas:
                lista_pecas.append([c,d])            
    shuffle(lista_pecas)
    return lista_pecas 