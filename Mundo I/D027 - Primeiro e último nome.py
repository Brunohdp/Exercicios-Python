print('=' * 6, 'DESAFIO 027 - PRIMEIRO E ÚLTIMO NOME', '=' * 6)
n = str(input('| Digite seu nome completo: ')).strip()                              #Recebe o nome e elimina espaços antes e depois
sp = n.split()                                                                      #Quebra o nome nos espaços
print(f'Seu primeiro nome é "{sp[0]}" e o seu último nome é "{sp[len(sp)-1]}"')     #Mostra qual o primeiro nome e o último.
                                                                                    #O último ele sabe qual é pegando o comprimento de sp e tirando 1
