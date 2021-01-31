print('====== DESAFIO 010 - CONVERSOR PARA DOLAR ======')
n = float(input('Digite a quantidade de dinheiro que você possui: '))
d = float(input('Digite a cotação atual do Dolar: '))
c = n/d
print('Você pode comprar US${:.2f} com R${:.2f}\nA cotação atual do dolar é: R${:.2f}'.format(c, n, d))
