print('\033[1;32;4m-=' * 6, 'DESAFIO 053 - PALÍNDROMO', '=-' * 6)       #Título

print('\033[0;33;1m-' * 22)
print('| \033[0;30;7m Digite uma Frase \033[0;33;1m |')                 #Recebe a frase
print('-' * 22)
f = str(input('| R: ')).strip().upper()                                 #Retira os espaços e deixa tudo em maiúsculas
j = ''.join(f.split())                                                  #Separa todas as palavras em módulos e junta elas novamente
# i = ''                                                                  #Iverso recebe vazio

inv = j[::-1]                                                           #Pode-se eliminar o for usando esse método. Só o python permite esse método pois envolve esquema de fatiamento
                                                                        #O inverso pega o junto e vai do início até o final voltando de 1 em 1
'''for l in range(len(j) - 1, -1, -1):                                     #Repete do tamanho da frase - 1 (Ele conta a quantidade de letras, mas se uma palavra tem 10 letras, ele lê 9, pq vai de 0 até 9) até a primeira letra pulando de 1 em.
    i += j[l]                                                           #O inverso recebe letra por letra do junto na posição da letra
'''
if inv == j:                                                              #Se o inverso for igual ao junto, então é um palíndromo, se não, não
    print('-' * 200)
    print(f'| \033[30;45m A Sua frase \033[42;1m \033[4mÉ\033[0;42m \033[45;30m um \033[42;1m \033[4mPOLÍMERO\033[0;42;30m, \033[0;30;45m pois \033[42;1m \033[4m{f}\033[0;30;42m, \033[0;45;30m ao contrário, continua sendo \033[42;1m \033[4m{inv}\033[0;42;30m! \033[0;33;1m |')
    print('-' * 200)
else:
    print('-' * 200)
    print(f'| \033[30;44m A Sua frase \033[41;1m \033[4mNÃO É\033[0;41m \033[44;30m um \033[41;1m \033[4mPOLÍMERO\033[0;41;30m, \033[0;30;44m pois \033[41;1m \033[4m{f}\033[0;41;30m, \033[0;44;30m ao contrário, fica \033[41;1m \033[4m{inv}\033[0;41;30m! \033[0;33;1m |')
    print('-' * 200)
