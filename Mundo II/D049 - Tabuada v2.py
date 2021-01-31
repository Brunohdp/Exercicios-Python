print('\033[36;1;4m-=' * 6, 'DESAFIO 049 - TABUADA V2', '=-' * 6)                       #Título

print('\033[0;33;1m-' * 47)
print('| \033[0;30;44;1m DIGITE UM NÚMERO PARA SABER A SUA TABUADA \033[0;33;1m |')     #Recebe o número para fazer a tabuada
print('-' * 47)
n = int(input('| R: '))

print('-' * 25)
print(f'| \033[1;30;41m TABUADA DO NÚMERO {n} \033[0;1;33m |')
print('-' * 25)

for c in range(1, 11):                                                          #Repete de 1 até 11 para mostrar até o número 10
    m = n * c                                                                   #Multiplica o número recebido com o c, que é a contagem da repetição
    if c == 10:                                                                 #LAYOUT - Se c for igual a 10 ele formata de forma diferente dos outros pra ficar alinhado
        print(f'| \033[0;1;30;42m    \033[4m{n:^3}x{c:>3} = {m:^3}\033[0;1;42m    \033[0;1;33m |')
    else:
        print(f'| \033[0;1;30;42m    \033[4m{n:^3}x{c:>2} = {m:^3}\033[0;1;42m     \033[0;1;33m |')     #Ambas as condições mostram o resultado da multiplicação e os números que estão sendo multiplicados.
print('-' * 25)
