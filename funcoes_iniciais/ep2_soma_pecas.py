def soma_pecas(mao):
    pontos = 0
    for i in range(len(mao)):
        peca = mao[i]
        pontos += peca[0]
        pontos += peca[1]
    return pontos