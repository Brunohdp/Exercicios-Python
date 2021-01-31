print('\033[31;1;4m-=' * 6, 'DESAFIO 060 - FATORIAL V2', '=-' * 6)

print('\033[0;33;1m-' * 27)
print('| \033[0;30;44m Digite o seu fatorial \033[0;33;1m |')
print('|', '-' * 23, '|')
f = int(input('| R: '))
print()
m = 1

print('-' * 53)
print(f'| \033[0;30;42m O fatorial de \033[1;45m{f:^3}\033[0;30;42m é igual a ', end='\033[1;45m ')

while f != 0:
    print(f, end='x')
    m *= f
    f -= 1
print(f' ={m:^5}\033[0;30;42m! \033[0;1;33m |')
print('-' * 53)
