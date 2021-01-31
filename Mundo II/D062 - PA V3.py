print('\033[1;31;4m-=' * 6, 'DESAFIO 062 - PROGRESSÃO ARITIMÉTICA V3', '=-' * 6)

print('\033[0;1;33m-' * 29)
print('| \033[0;30;45m Digite o primeiro termo \033[0;1;33m |')
print('|', '-' * 25, '|')
t = int(input('| R: '))

print()

print('-' * 20)
print('| \033[0;30;45m Digite a razão \033[0;1;33m |')
print('|', '-' * 16, '|')
r = int(input("| R: "))

print()

pa = 0

print('-' * 70)
print('| \033[0;30;42m', end=' ')


while pa != 10:
    print(t, end=' -> ')
    t += r
    pa += 1

print('Acabou! \033[0;33;1m |')
print('-' * 70)

print('-' * 41)
print('| \033[0;30;44m Quantos termos você quer adicionar? \033[0;33;1m |')
print('|', '-' * 37, '|')
q = int(input('| R:'))

while q != 0:
    print('-' * 200)
    print('| \033[0;30;42m', end=' ')
    while pa != 10 + q:
        print(t, end=' -> ')
        t += r
        pa += 1
    print('-' * 41)
    print('| \033[0;30;44m Quantos termos você quer adicionar? \033[0;33;1m |')
    print('|', '-' * 37, '|')
    q = int(input('| R:'))

print('Acabou! \033[0;33;1m |')
print('-' * 200)

