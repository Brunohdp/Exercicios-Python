from datetime import date                                           #Importa função date da biblioteca, usada para pegar a data do pc
print('\033[36;1m-='*6, 'DESAFIO 041 - NATAÇÃO', '=-'*6)            #Título

a = int(input('\033[0;30mDigite o seu ano de nascimento: '))        #Recebe o ano de nascimento
i = date.today().year - a                                           #Calcula a idade
print('\033[37m-'*70)

if i <= 9:              #Se for menor ou igual a 9 anos, é classificado como mirim
    print(f'\033[0;30mCom a sua idade de \033[35;1;4m{i}\033[0;30m anos, você se encaixa na categoria \033[31;4;1mMIRIM\033[0;30m!')
elif i <= 14:           #Se for menor ou igual a  14 anos, é classificado como infantil
    print(f'\033[0;30mCom a sua idade de \033[35;1;4m{i}\033[0;30m anos, você se encaixa na categoria \033[32;4;1mINFANTIL\033[0;30m!')
elif i <= 19:           #Se for menor ou igual a  19 anos, é classificado como junior
    print(f'\033[0;30mCom a sua idade de \033[35;1;4m{i}\033[0;30m anos, você se encaixa na categoria \033[33;4;1mJUNIOR\033[0;30m!')
elif i == 25:           #Se for menor ou igual a  25 anos, é classificado como sênior
    print(f'\033[0;30mCom a sua idade de \033[35;1;4m{i}\033[0;30m anos, você se encaixa na categoria \033[34;4;1mSÊNIOR\033[0;30m!')
else:                   #Se não for nenhuma das anteriores é maior que 20, portanto, é classificado como Master
    print(f'\033[0;30mCom a sua idade de \033[35;1;4m{i}\033[0;30m anos, você se encaixa na categoria \033[36;4;1mMASTER\033[0;30m!')
