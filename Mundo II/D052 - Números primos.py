print('\033[1;4;33m-=' * 6, 'DESAFIO 052 - NÚMEROS PRIMOS', '=-' * 6)       #Título

print('\033[0;1;33m-' * 22)
print('| \033[30;7m Digite um número \033[0;1;33m |')                       #Recebe o número para ser analisado e ver se é primo ou não
print('-' * 22)
n = int(input('| R: '))

print('-' * 200)
print('|', end=' ')

t = 0                                                                       #Total de dividos recebe 0

for c in range(1, n + 1):                                                   #Conta de 1 até o número digitado mais 1 para exibir até o número digitado
    if n % c == 0:                                                          #Se o resto do número divido pelo contador for == a 0 o fundo do número fica verde se não, vermelho
      print('\033[30;42m', end=' ')
      t += 1
    else:
        print('\033[30;41m', end=' ')
    print(c, end=' \033[0;1;33m')
print(' |')
print('-' * 200)

if t == 2 and n % 2 == 1:                                                  #Se o total de divisões for 2 e o número for ímpar, então é primo, se não, não
    print('-' * 97)
    print(f'| \033[0;30;42m O número \033[1;4;41m{n:^5}\033[0;30;42m foi dividido \033[41m \033[0;4;1;30;41mAPENAS {t}\033[0;41m \033[30;42m vezes e é um número \033[1;41m \033[4mIMPAR\033[0;41m \033[0;30;42m, por isso ele é \033[41;1m \033[4mPRIMO\033[0;41m \033[0;42;30m! \033[0;33;1m |')
    print('-' * 97)
else:
    print('-' * 83)
    print(f'| \033[0;30;41m O número \033[1;4;44m{n:^5}\033[0;30;41m foi dividido \033[44m \033[1;4m{t}\033[0;44m \033[0;30;41m vezes e por isso ele \033[44;1m \033[4mNÃO É\033[0;44m \033[0;30;41m um número \033[44;1m \033[4mPRIMO\033[0;44m \033[0;30;41m\033[0;33;1m |')
    print('-' * 83)
