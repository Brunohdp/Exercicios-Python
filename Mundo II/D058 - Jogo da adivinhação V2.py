from random import randint
from time import sleep                                                              #Importa a função de geração de número inteiro aleatório e de delay bibliotecas random e time, respectivamente

print('\033[1;4;31m-=' * 6, 'DESAFIO 059 - JOGO DA ADIVINHAÇÃO V2', '=-' * 6)       #Título

print('\033[0;1;33m-' * 64)
print('| \033[0;30;7m                   \033[4mVamos Jogar Um Jogo!\033[0;30;7m                     \033[0;33;1m |')
# print('|', '-' * 60, '|')                                                           #Layout
print('| \033[0;30;7m \033[4mEu Te Desafio A Adivinhar Em Que Número Eu Estou Pensando\033[0;30;7m! \033[0;33;1m |')
print('-' * 64)
print()

print('-' * 66)
print('| \033[0;30;45m Vamos Lá! Digite Um Número Entre \033[1;44m \033[4m1\033[0;44m \033[0;30;45m E \033[1;44m \033[4m10\033[0;44m \033[0;30;45m E Veja Se Acerta \033[0;33;1m |')
print('|', '-' * 62, '|')
n = int(input('| R: '))                                                             #Recebe o número digitado pelo jogador
c = randint(1, 10)                                                                  #Recebe um número aleatório para comparar com o digitado
t = 1                                                                               #Tentativas recebe 0
print()

print('-' * 20)
print('| \033[0;30;41m PROCESSANDO... \033[0;33;1m |')                              #Efeito de processamento
print('-' * 20)
sleep(1)
print()

while n != c:                                                                       #Enquanto a resposta não for não repete
    print('-' * 79)
    print(f'| \033[0;30;41m       Poxa, Você Errou! Eu Pensei No Número \033[1;43m \033[4m{c}\033[0;43m \033[0;30;41m E você digitou \033[1;43m \033[4m{n}\033[0;43m \033[0;41;30m!       \033[0;33;1m |')
    print('-' * 79)
    print()
    print('-' * 79)
    print('| \033[0;30;44m   Tente De Novo! Digite Outro Número Entre \033[1;45m \033[4m1\033[0;45m \033[0;30;44m E \033[1;45m \033[4m10\033[0;45m \033[0;30;44m E Veja Se Acerta.   \033[0;33;1m |')
    print('|', '-' * 75, '|')
    n = int(input('| R: '))                                                         #Recebe o número digitado pelo jogador
    c = randint(1, 10)                                                              #Recebe um número aleatório para comparar com o digitado

    print()
    print('-' * 20)
    print('| \033[0;30;41m PROCESSANDO... \033[0;33;1m |')                          #Efeito de processamento
    print('-' * 20)
    sleep(1)
    print()

    t += 1

print('-' * 80)
print(f'| \033[0;30;42m Parabéns, Você Acertou! Nós 2 Pensamos No Número \033[41;1m \033[4m{c:^3}\033[0;41m \033[0;30;42m. Você É Bom, Heim?! \033[0;33;1m |')
print(f'| \033[0;30;7m                   Você Tentou \033[4;44m {t} \033[0;30;7m vezes até acertar HAHA!                  \033[0;1;33m |')
print('| \033[0;30;7m               Foi Super Legal Jogar Com Você. Até a Próxima!               \033[0;33;1m |')
print('-' * 80)
