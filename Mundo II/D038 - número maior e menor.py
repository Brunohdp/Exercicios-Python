print('\033[31m-='*6, '\033[4mDESAFIO 038 - NÚMERO MAIOR E MENOR\033[0;31m', '=-'*6)
n1 = int(input('\033[33mDigite um número: '))
n2 = int(input('Digite outro número: '))
print('\033[34;1m-'*60)
if n1 < n2:
    print(f'\033[30mO primeiro número \033[36;4;1m({n1})\033[0;30m é menor que o segundo número \033[36;4;1m({n2})\033[0;30m!')
elif n1 == n2:
    print(f'\033[30mOs dois números digitados são iguais: \033[36;4;1m{n1}\033[0;30m e \033[36;4;1m{n2}\033[m!')
else:
    print(f'\033[30mO primeiro número \033[1;36;4m({n1})\033[0;30m é maior que o segundo número \033[1;36;4m({n2})\033[m!')
