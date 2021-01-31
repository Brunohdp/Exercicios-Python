print('\033[1;36m-='*6, '\033[4mDESAFIO 042 - TRIÂNGULOS\033[0;1;36m', '=-'*6)      #Título

r1 = float(input('\033[mDigite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))                                        #Recebe os comprimentos das retas

print('-'*35)

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('\033[34;1;4mEQUILÁTERO\033[m!')
    elif r1 != r2 != r3 != r1:
        print('\033[33;1;4mESCALENO\033[m!')
    else:
        print('\033[32;1;4mISÓCELES\033[m!')
else:
    print('\033[41;1;30m** Os seguimentos NÃO PODEM formar um triângulo! **\033[m')
