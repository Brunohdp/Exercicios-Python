from datetime import date                                                   #importa função date da biblioteca datetime

print('\033[1;4;31m-=' * 6, 'DESAFIO 054 - CONTAGEM DE IDADE', '=-' * 6)    #Título

print('\033[0;1;33m-' * 61)
print('| \033[30;45m Digite o número de pessoas que dejesa verificar a idade \033[0;33;1m |')
print('|', '-' * 57, '|')
n = int(input('| R: '))                                                     #Recebe a quantidade de pessoas que seram analisadas as idades


s1 = 0                                                                      #Somatória de pessoas com mais de 21
s2 = 0                                                                      #Somatória de pessoas com menos de 21
ano = date.today().year                                                     #Ano recebe o ano da data atual do sistema

for c in range(0, n):                                                       #Repete de 0 até o número de pessoas determinado
    print('-' * 34)
    print('| \033[30;44m Digite seu ano de nascimento \033[0;1;33m |')      #Recebe o ano de nascimento de alguém
    print('|', '-' * 30, '|')
    a = int(input('| R: '))
    i = ano - a                                                             #A idade recebe o ano atual - o ano de nascimento digitado, ou seja, a idade atual da pessoa
    if i >= 21:                                                             #Se a idade for maior que 21, s1 recebe ela mesma mais 1, se não, s2 que recebe ele mesmo mais 1
        s1 += 1
    else:
        s2 += 1

print('-' * 90)
print(f'| \033[0;30;42m Das \033[1;45m \033[4m{n}\033[0;45m \033[0;30;42m pessoas, houveram \033[45;1m \033[4m{s1}\033[0;45m \033[0;42;30m são \033[45;1m \033[4mMAIORES DE 18 ANOS\033[0;45m \033[0;42;30m e \033[1;45m \033[4m{s2}\033[0;45m \033[0;42;30m são \033[45;1m \033[4mMENORES DE 18 ANOS\033[0;45;30m!\033[0;1;33m |')
print('-' * 90)                                                             #Exibe a quantidade de pessoas que tiveram mais de 21 e menos de 21 dentro da quantidade de pessoas determinadas.

