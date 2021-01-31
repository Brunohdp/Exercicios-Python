print('='*6, 'DESAFIO 034 - AUMENTO NO SALÁRIO', '='*6)
n = str(input('Digite o nome do funcionário: '))                    #Recebe nome do funcionário
s = float(input('Digite o salário do funcionário: '))               #Recebe o salário
if s >= 1250.00:                                                    #Se for maior que 1250 ganha um acrescimo de 10%, se for abaixo aumento de 15%
    ns = s/100*10+s
    print(f'O salário de {n} teve um acrescimo de 10% indo de R${s:.2f} para R${ns:.2f}.')
else:
    ns = s/100*15+s
    print(f'O salário de {n} teve um acrescimo de 15% indo de R${s:.2f} para R${ns:.2f}.')
