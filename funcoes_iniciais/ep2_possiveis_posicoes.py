def posicoes_possiveis(mesa,mao):
    posicoes_possiveis = []
    if mesa == []:
        for i in range(len(mao)):
            posicoes_possiveis.append(i)
    else:
        ponta_1 = mesa[0]
        ponta_2 = mesa[len(mesa)-1]
        ponta_de_mesa = [ponta_1[0],ponta_2[1]]
        for i in range(len(mao)):
            checa_peca = mao[i]
            if checa_peca[0] in ponta_de_mesa or checa_peca[1] in ponta_de_mesa:
                posicoes_possiveis.append(i)
    return posicoes_possiveis