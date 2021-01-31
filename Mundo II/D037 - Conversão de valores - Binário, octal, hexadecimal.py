print('\033[36;1;4m-='*6, 'DESAFIO 037 - CONVERSÃO DE VALORES', '=-'*6)                            #Título

print('\033[0;30;1m-'*28)
n = int(input('| \033[45;1;30;4mDigite um número inteiro\033[0;1;30;45m\033[0;30;1m |\n| R: '))    #Recebe o número inteiro

print('-'*28)
print('\033[0;30;1m| \033[30;1;42m Escolha uma conversão: \033[0;30;1m |')                         #Fala pra escolher uma conversão
print('-'*28)

c = int(input('''| \033[44;30m[1]\033[4mBinário\033[0;44m              \033[0;30;1m |
| \033[45;30m[2]\033[4mOctal\033[0;45m                \033[0;30;1m |
| \033[43;30m[3]\033[4mHexadecimal\033[0;43m          \033[0;30;1m |
| R: '''))                                                                                         #Recebe a escolha de conversão
print('-'*28)

if c == 1:                                                                                          #Se for 1, converte para binário
    print('-'*47)
    print(f'| \033[42;1;30m{n:^5}\033[0;44;30;1m convertido para binário é igual a \033[42;1;30m{bin(n)[2:]:^5}\033[0;30;1m |')
    print('-'*47)
elif c == 2:                                                                                        #Se não, se for 2, converte para octal
    print('-'*47)
    print(f'| \033[42;30;1m{n:^5}\033[0;1;45;30m convertido para octal é igual a \033[42;30m{oct(n)[2:]:^5}\033[0;30;1m |')
    print('-'*47)
elif c == 3:                                                                                               #Se não for nenhum, ele converte para hexadecimal
    print('-'*47)
    print(f'| \033[42;30;1m{n:^5}\033[0;1;43;30m convertido para hexadecimal é igual a \033[42;30;1m{hex(n)[2:]:^5}\033[0;30;1m |')
    print('-'*47)
else:
    print('-'*46)
    print(f'| \033[1;30;41m** OPÇÃO INVÁLIDA, TENTE OUTRA ESCOLHA! **\033[0;30;1m |')
    print('-'*46)
