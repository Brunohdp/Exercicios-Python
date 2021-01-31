print('====== DESAFIO 013 - NOVO SALÁRIO ======')
n = str(input('Digite o nome do funcionário: '))
s = float(input('Digite o atual salário do funcionário: R$'))
a = s/100*15 + s
print(f'O novo salário do(a) {n}, após 15% de aumento é R${a:.2f}')
