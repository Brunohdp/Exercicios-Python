print('\033[31m-='*6, '\033[4m DESAFIO 040 - MÉDIA', '=-'*6)
n1 = float(input('\033[0;30mDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('\033[1;36m-'*50)

if m < 5:
    print(f'\033[0;30mSua média é \033[32;1;4m{m}\033[0;30m. Você está \033[31;1;4mREPROVADO\033[m!')
elif 5 <= m <= 6.9:
    print(f'\033[0;30mSua média é \033[32;1;4m{m}\033[0;30m. Você está de \033[1;4;34mRECUPERAÇÃO\033[m!')
else:
    print(f'\33[0;30mSua média é \033[32;1;4m{m}\033[0;30m. Você está \033[32;1;4mAPROVADO\033[m!')
