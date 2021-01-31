print('='*6, 'DESAFIO 035 - ANALISANDO TRIANGULOS', '='*6)
r1 = float(input('\033[33mDigite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: \033[m'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'\033[1;30;42mCom os seguimentos {r1}, {r2} e {r3} da para fazer um triângulo\033[m')
else:
    print(f'\033[1;30;41mInflimente não da para fazer um triângulo com os seguimentos {r1}, {r2} e {r3}\033[m')
