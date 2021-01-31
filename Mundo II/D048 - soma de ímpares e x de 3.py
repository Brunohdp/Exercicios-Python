print('\033[32;1;4m-=' * 6, 'DESAFIO 048 - SOMA DE ÍMPARES E X DE 3', '=-' * 6)     #Título
soma = 0
cont = 0

for c in range(1, 500):                             #Repete de 1 até 500
    if c % 3 == 0 and c % 2 == 1:                   #Se o c divido por 3 for igual a 0, ou seja, múltiplo de 3 e c divido por 2 for igual a 1, ou seja, ímpar, ele mostra o c
        print(c, end=' ')
        soma += c
        cont += 1

print()
print(f'\033[0;1;30;42mA soma de todos os {cont} valores é: {soma}!\033[0m')