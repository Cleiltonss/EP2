def verifica_ganhador(dicionario):
    menor = 0
    for jogador, lista_pecas in dicionario.items():
        if lista_pecas == []:
            return jogador  
        elif menor <= len(lista_pecas):
            menor = len(lista_pecas)      
    if menor != 0:
        return -1 