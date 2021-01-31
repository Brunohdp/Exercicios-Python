print('\033[36;1;4m-' * 6, 'DESAFIO 056 - ANALISADOR COMPLETO', '-' * 6)            #Título.

print('\033[0;1;33m-' * 36)
print('| \033[30;42m Quantas pessoas quer analisar? \033[0;1;33m |')                #Recebe o número de pessoas a serem analisadas.
print('|', '-' * 32, '|')
p = int(input('| R: '))

ml = 0                                                                              #Recebe a quantidade de mulheres com menos de 20 anos.
si = 0                                                                              #Recebe a somatória de idades.
mi = 0                                                                              #Recebe a idade do homem mais velho.
nmv = ''                                                                            #Nome do mais velho recebe string vazia

for c in range(0, p):                                                               #Repete o laço das perguntas de 0 até o número de pessoas a serem analisadas recebido.
    print('-' * 32)
    print(f'| \033[30;44m Digite o nome da {c+1}° pessoa \033[0;1;33m |')           #Recebe o nome da pessoa retirando os espaços antes e depois do nome e deixando todas as primeiras letras em maiúsculas.
    print('|', '-' * 28, '|')
    n = str(input('| R: ')).strip().title()

    print('-' * 33)
    print(f'| \033[30;45m Digite a idade da {c+1}° pessoa \033[0;1;33m |')          #Recebe a idade.
    print('|', '-' * 29, '|')
    i = int(input('| R: '))

    print('-' * 38)
    print(f'| \033[30;41m Digite o sexo da {c + 1}° pessoa [F/M] \033[0;1;33m |')   #Rece o sexo biológico da pessoa retirando os espaços antes e depois e deixando a letra em maiúsculo.
    print('|', '-' * 34, '|')
    s = str(input('| R: ')).strip().upper()

    si += i                                                                         #Somatória das idades rebe ela mesma e mais a idade digitada para fazer a média.

    if s == 'F' and i < 20:                                                         #Se o sexo biológico for igual a "F" de feminino e a idade for menor que 20 a variável ml recebe ela mesma + 1 pra contar a quantidadde de mulheres com menos de 20 anos  .
        ml += 1
    if s == 'M' and i > mi:                                                         #Se o sexo biológico for igual a "M" de masculino e a idade for maior que a variável mi(maior idade), essa variável vai receber essa nova idade e a variável nmv(nome mais velho) recebe o nome do homem.
        mi = i
        nmv = str(n)

m = si / p                                                                          #Faz a média de idades.

print('-' * 72)
print(f'| \033[30;44m A média das idades é \033[4m{m:<4.1f}\033[0;44m                                           \033[0;33;1m |')                          #Exibe a média das idades.
print(f'| \033[30;45m Tem \033[4m{ml:^3}\033[0;30;1;45m mulheres com menos de \033[4m20 anos\033[0;45m                               \033[0;33;1m |')    #Exibe a quantidade de mulheres com menos de 20 anos.
print(f'| \033[30;42m O homem mais velho se chama \033[4m{nmv:^10}\033[0;30;1;42m e a sua idade é de \033[4m{mi:^4}\033[0;42;1;30m anos \033[0;1;33m |')             #Exibe o nome e a idade do homem mais velho.
print('-' * 72)
