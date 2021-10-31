def inicia_jogo(n_jog, lista_pecas):
    dic_final = {'jogadores': {}}
    for i in range(0, n_jog):        
        dic_final['jogadores'][i] = lista_pecas[0:7]
        del lista_pecas[0:7]
    dic_final['monte'] = lista_pecas
    dic_final['mesa'] = []
    return dic_final    