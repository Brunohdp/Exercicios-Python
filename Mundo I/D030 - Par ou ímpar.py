print('='*6, 'DESAFIO 030 - PAR OU ÍMPAR', '='*6)
print('-'*30)
n = int(input('| Digite um número inteiro: '))
print('-'*30)
pi = n % 2
if pi == 0:
    print('-'*28)
    print(f'| O número {n} é PAR! |')
    print('-'*28)
else:
    print('-'*31)
    print(f'| O número {n} pe ÍMPAR! |')
    print('-'*31)
