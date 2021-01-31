print('\033[31;1m-='*6, '\033[4mDESAFIO 044 - COMPRANDO UM PRODUTO\033[0;1;31m', '=-'*6)    #Título

v = float(input('\033[0;30m| \033[0;33;1mDigite o preço do produto: \033[32;1mR$'))         #Recebe o valor do produto

print('\033[0;30m-'*38)
print('\033[30m|    \033[44;4mEscolha a forma de pagamento\033[0;30m    |')                 #Design
print('-'*38)

f = int(input('''| \033[32;1m[1]\033[4mDinheiro ou cheque - \033[31;1;4m10% off\033[0;30m    |
| \033[1;35m[2]\033[4mÀ vista no cartão - \033[31;1;4m5% off\033[0;30m      |
| \033[36;1m[3]\033[4mEm até 2x\033[0;30m                       |
| \033[0;30;1m[4]\033[4m3x ou mais - \033[33;1;4m3% de juros ao mês\033[0;30m |
|\033[m R: '''))                                                                            #Recebe a opção de pagamento escolhida. Se for 1 paga o valor total, se for 3 também, mas divido em 2.
                                                                                            #Se for 2 recebe 5% de desconto no valor total e paga em 1. Se for 4, escolhe em quantos meses quer pagar e é somado 3% de juros por mês.
print('\033[30m-'*38)

if f == 1:                                                                                  #Paga 1 com 10% do valor total
    nv = v - (v/100*10)
    print(f'\033[1;30mVocê receberá 10% de desconto por pagar à vista. Você pagará \033[32;4mR${nv:.2f}\033[0;30;1m!')
elif f == 2:                                                                                #Paga 1 com 5% de desconto
    nv = v - (v/100*5)
    print(f'\033[0;30;1mVocê tem um desconto de 5% no produto. Você pagará duas vezes de \033[32;4mR${nv/2:.2f}\033[0;30;1m, dando um total de \033[32;4mR${nv:.2f}\033[m!')
elif f == 3:                                                                                #Paga 2 do valor total
    print(f'\033[0;1;30mVocê pagará duas vezes de \033[32;4mR${v/2:.2f}\033[0;30;1m, dando um valor total de \033[32;4mR${v:.2f}\033[0;30;1m!')
elif f == 4:                                                                                #Escolhe em quantas quer pagar, mas com acrecimo de 3% ao mês
    r = int(input('Digite em quantas vezes você deseja pagar: '))
    j = r * (v/100*3)
    nv = v + j
    print(f'\033[0;30;1mVoce pagará {r} vezes de \033[32;4mR${nv/r:.2f}\033[0;30;1m, totalizando o valor de \033[32;4mR${nv:.2f}\033[0;30;1m, por conta dos 3% de juros ao mês!')
else:                                                                                       #Se digitar qualquer outro número dá erro
    print(f'\033[30;41;1;4m** Opção inválida. Compra de \033[42;30m{v:.2f}\033[30;41m cancelada. Tente novamente! **\033[m')
