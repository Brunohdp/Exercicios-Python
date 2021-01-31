print('\033[31;1;4m-=' * 6, 'DESAFIO 047 - PARES ENTRE 1 E 50', '=-' * 6)       #Título

for c in range(1, 51):                                                          #Repete de 1 até 51 para mostrar até o número 50.
    if c % 2 == 0:                                                              #Se o c divido por 2 tiver resto igual a 0, então ele é par, logo mostra o c
        print(c)

for n in range(2, 51, 2):                                                       #Repete de 2 até 50 pulando de 2 em 2 ocasionando na msm resposta
    print(n, end='')
