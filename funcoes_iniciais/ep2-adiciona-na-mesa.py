def adiciona_na_mesa(peca,mesa):
    if mesa == []:
        mesa_nova = [peca]
    else:
        entrada_1 = mesa[0]
        entrada_2 = mesa[len(mesa)-1]
        dir_ou_esq = [entrada_1[0],entrada_2[1]]
        if peca[0] == dir_ou_esq[0]:
            peca.reverse()
            mesa_nova = [peca]
            for a in mesa:
                mesa_nova.append(a)
        elif peca[1] == dir_ou_esq[0]:
            mesa_nova = [peca]
            for a in mesa:
                mesa_nova.append(a)
        elif peca[0] == dir_ou_esq[1]:
            mesa_nova = mesa 
            mesa_nova.append(peca)
        else:
            mesa_nova = mesa
            peca.reverse()
            mesa_nova.append(peca)             
    return mesa_nova