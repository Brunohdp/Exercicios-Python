print('\033[36;1;4m-=' * 6, 'DESAFIO 055 - SELETOR DE PESOS', '=-' * 6)         #Título

print('\033[0;1;33m-' * 38)
print('| \033[30;41m Quantas pessoas deseja analisar? \033[0;33;1m |')          #Recebe a quantidade de pessoas a serem analisadas
print('|', '-' * 34, '|')
n = int(input('| R: '))

maior = 0                                                                       #Determina que maior recebe o valor 0
menor = 0                                                                       #Determina que menor recebe o valor 0

for c in range(0, n):                                                           #Repete de 0 até o número de pessoas determinado
    print('-' * 32)
    print(f'| \033[30;45m Digite o peso da {c+1}° pessoa \033[0;1;33m |')       #Recebe o peso da pessoa
    print('|', '-' * 28, '|')
    kg = float(input('| R: '))
    if c == 1:                                                                  #Se o contador for 1, tanto o maior quanto o menor peso recebe o peso dela para fazer futuras comparações
        maior = kg
        menor = kg
    else:
        if kg > maior:                                                              #Se o peso for maior que o maior determinado, então o mair recebe o peso, se tornando o novo maior
            maior = kg
        if kg < menor:                                                              #Se o peso for menor que o menor determinado, então o menor recebe o peso, se tornando o novo menor
            menor = kg

print('-' * 65)
print(f'| \033[30;42m Das {n} pessoas, o maior peso foi de {maior:^4.1f} e o menor foi {menor:^4.1f}! \033[0;1;33m |')
print('-' * 65)                                                                 #Exibe o maior e menor peso digitado dentro da quantidade de pessoas determinadas

