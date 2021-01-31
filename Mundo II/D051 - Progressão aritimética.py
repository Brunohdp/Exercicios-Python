print('\033[32;1;4m-=' * 6, 'DESAFIO 051 - PROGRESSÃO ARITIMÉTICA', '=-' * 6)       #Título

print('\033[0;33;1m-' * 29)

print('| \033[1;30;45m Digite o primeiro termo \033[0;33;1m |')                     #Recebe o primeiro termo, o número que começará a progressão aritimética
print('-' * 29)
t = int(input('| R: '))

print('-' * 20)

print('| \033[30;45m Digite a razão \033[0;1;33m |')                                #Recebe a razão, o número que será somado ao primeiro termo para formar o segundo e assim sucessivamente até o número de termos determinado ser atingido
print('-' * 20)
r = int(input('| R: '))

print('-' * 74)
print('| \033[30;44m', end=' ')

for c in range(0, 10):                                                              #Repete de 0 a 10, mostrando 10 números. Se fosse de 1 a 10 seria exibido 9 números!
    print(f'{t:>3}', end=' ->')                                                     #Mostra o termo um ao lado do outro separado por vírgulas
    t += r                                                                          #Termo recebe ele mesmo + a razão.

print(' ACABOU! \033[0;1;33m |')
print('-' * 74)
