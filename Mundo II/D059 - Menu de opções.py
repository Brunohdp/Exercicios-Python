print('\033[1;31;4m-=' * 6, 'DESAFIO 059 - MENU DE OPÇÕES', '=-' * 6)

print('\033[0;33;1m-'*53)
print('| \033[0;30;44m Digite números inteiros para fazer as operações \033[0;33;1m |')             #Design
print('|', '-' * 49, '|')
print('| \033[0;40m Digite o primeiro número \033[0;33;1m |')
print('|', '-' * 26, '|')
n1 = int(input('| R: '))                                                    #Recebe primeiro número
print('-' * 29)
print('| \033[0;40m Digite o segundo número \033[0;1;33m |')
print('|', '-' * 25, '|')
n2 = int(input('| R: '))                                                    #Recebe segundo número
print('-' * 29)
print()

r = int(0)                                                                  #Indica que resposta = 0 para iniciar loop

while r != 6:                                                               #Enquanto resposta for diferente de 6 (sair) mantém o loop
    print('-' * 25)
    print('| \033[0;40m Escolha A Operação: \033[0;33;1m |')                #Exibe todas as operações matemáticas disponíveis para fazer com os 2 números inteiros
    print('|', '-' * 21, '|')
    r = int(input('''| \033[0;30;41m [1]Somar            \033[0;33;1m |
| \033[0;30;42m [2]Subtrair         \033[0;33;1m |
| \033[0;30;44m [3]Multiplicar      \033[0;33;1m |
| \033[0;30;45m [4]Maior            \033[0;33;1m |
| \033[0;30;46m [5]Novos números    \033[0;33;1m |
| \033[0;30;47m [6]Sair             \033[0;33;1m |
| R:'''))                                                                   #Recebe o número equivalente a operação escolhida
    if r == 1:                                                              #Se a resposta for 1, soma os dois números e exibe os resultados
        s = n1 + n2
        print('-' * 46)
        print(f'| \033[0;30;41m A Soma de \033[45;1m{n1:^4}\033[0;30;41m com \033[45;1m{n2:^4}\033[0;30;41m é igual a: \033[45;1m{s:^4}\033[0;30;41m! \033[0;33;1m |')
        print('-' * 46)
    elif r == 2:                                                            #Se a resposta for 2, subtrai os dois números e exibe o resultado
        sub = n1 - n2
        print('-' * 46)
        print(f'| \033[0;30;42m A subtração de \033[45;1m{n1:^4}\033[0;30;42m com \033[45;1m{n2:^4}\033[0;30;42m é igual a: \033[45;1m{sub:^4}\033[0;30;42m! \033[0;33;1m |')
    elif r == 3:                                                            #Se a resposta for 3, multiplica os números e exibe o resultado
        m = n1 * n2
        print('-' * 56)
        print(f'| \033[0;30;44m A multiplicação entre \033[45;1m{n1:^4}\033[0;30;44m e \033[45;1m{n2:^4}\033[0;30;44m é igual a: \033[45;1m{m:^4}\033[0;30;44m! \033[0;33;1m |')
        print('-' * 56)
    elif r == 4:                                                            #Se a resposta for 4, faz a comparação entre os números e diz qual é o maior, caso haja um
        maior = 0                                                           #Define a variável que recebe o maior valor é 0 para poder ser substituído depois
        if n1 == n2:                                                        #Se os dois números forem iguais, diz que não tem maior
            print()
            print('-' * 71)
            print(f'| \033[0;30;45m Não tem número maior entre eles, ambos tem o mesmo valor de \033[44;1m{n1:^4}\033[0;30;45m! \033[0;33;1m |')
            print('-' * 71)
            print()
            print()
        else:
            if n1 > n2:                                                     #Se primeiro número for maior que o segundo, então maior recebe o primeiro número e diz que ele é maior
                maior = n1
            else:                                                           #Se não, o segundo número é maior e diz que ele é o maior
                maior = n2
            print()
            print('-' * 49)
            print(f'| \033[0;30;45m Entre \033[44;1m{n1:^4}\033[0;30;45m e \033[44;1m{n2:^4}\033[0;30;45m, o maior número é o \033[44;1m{maior:^4}\033[0;30;45m! \033[0;33;1m |')
            print('-' * 49)
            print()
            print()
    elif r == 5:                                                            #Se a resposta for 5, permite a pessoa digitar os 2 novos números para refazer as equações
        print()
        print('-' * 41)
        print(f'| \033[0;30;46m Digite Os Números Novos, Por Favor! \033[0;33;1m |')
        print('|', '-' * 37, '|')
        print('| \033[0;30;7m Digite o primeiro número \033[0;33;1m |')
        print('|', '-' * 26, '|')
        n1 = int(input('| R:'))
        print('-' * 29)
        print('| \033[0;30;7m Digite o segundo número \033[0;1;33m |')
        n2 = int(input('| R:'))
        print('-' * 29)
        print()
print()
print('-' * 19)
print('| \033[0;40m Até a próxima \033[0;33;1m |')
print('-' * 19)
