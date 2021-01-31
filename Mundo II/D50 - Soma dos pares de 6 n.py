print('\033[31;1;4m-=' * 6, 'DESAFIO 050 - SOMA DOS PARES', '=-' * 6)       #Título

s = 0                                                                       #Soma recebe 0
tp = 0
tt = 0

for c in range(1, 7):                                                       #Repete de 1 até 7 para mostras 6 números
    print('\033[0;33;1m-' * 24)
    print(f'| \033[30;46m Digite o {c}° número \033[0;1;33m |')             #Recebe o número digitado
    print('-' * 24)
    n = int(input('| R: '))
    tt += 1
    if n % 2 == 0:                                                          #Se o número divido por 2 for igual a 0, ou seja, par, a soma dos pares recebe ela mesma mais o número digitado
        s += n
        tp += 1
    print()
print('-' * 64)
print(f'''| \033[0;30;7m            Você informou um total de \033[1;4m{tt}\033[0;30;7m valores.            \033[0;1;33m |
| \033[0;30;7m A soma de todos os \033[1;4m{tp}\033[0;30;7m valores pares digitados é igual a \033[1;4m{s}\033[0;30;7m! \033[0;1;33m |''')    #Mostra a soma de todos os pares digitados
print('-' * 64)
