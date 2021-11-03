cores = {'azul':     '\033[34m',                        #dicionário contendo cores
         'amarelo':  '\033[33m', 
         'vermelho': '\033[31m', 
         'verde':    '\033[32m',
         'roxo':     '\033[35m',
         'ciano':    '\033[36m',
         'preto':    '\033[30m',
         'limpa':    '\033[m'
        }

def printa_colorido(lista_pecas):
    texto_com_cor = ''
    for j in range(len(lista_pecas)):
        peca = lista_pecas[j]
        peca_colorida = '[' 
        for i in range(0, 2):
            if peca[i] == 0:     
                cor = cores['verde'] + '0' + cores['limpa']
                peca_colorida += cor + ','
            elif peca[i] == 1:
                cor = cores['roxo'] + '1' + cores['limpa']
                peca_colorida += cor + ','
            elif peca[i] == 2:
                cor = cores['preto'] + '2' + cores['limpa']
                peca_colorida += cor + ','
            elif peca[i] == 3:
                cor = cores['ciano'] + '3' + cores['limpa']
                peca_colorida += cor + ','
            elif peca[i] == 4:
                cor = cores['azul'] + '4' + cores['limpa']
                peca_colorida += cor + ','
            elif peca[i] == 5:
                cor = cores['amarelo'] + '5' + cores['limpa']
                peca_colorida += cor + ','
            else:
                cor = cores['vermelho'] + '6' + cores['limpa']
                peca_colorida += cor + ','
        peca_colorida = peca_colorida[:-1] + ']  '
        texto_com_cor+='{}'.format(peca_colorida)
    return texto_com_cor

print(f'{printa_colorido([[2,1], [3, 2]])}')