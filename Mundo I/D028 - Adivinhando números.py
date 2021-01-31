from random import randint
from time import sleep

print()
print('\033[4:35m', '=' * 6, 'DESAFIO 028 - ADIVINHANDO NÚMEROS', '=' * 6, '\033[m')                                #Título
print()

n = randint(0, 5)                                                                           #Randomiza um número de 0 a 5

print('\033[33m-=-' * 25)
print(' |\033[1m Estou pensando em um número entre 0 a 5. Tente adivinhar qual é... :D \033[m\033[33m|')         #Desafia o jogador
print('-=-' * 25)

print('-' * 36)
r = int(input('| Você consegue adivinhar?? hihihi |\n| R: '))                               #Recebe a resposta
print('-' * 36, '\033[m')

print('\033[4;31mPROCESSANDO...\033[m')

sleep(2)

if r == n:                                                                                  #Se acertar dá parabéns, se não, diz que ele ganhou
    print('\033[31:42m-' * 72)
    print(f'| \033[1:4mPARABÉNS!! Você acertou! Eu estava pensando no número {n}. Você é Bom!\033[m\033[31:42m |')
    print('-' * 72)
else:
    print('\033[7:30m-' * 62)
    print(f'| \033[1:4mHA EU GANHEI! Eu estava pensando no número {n} e não no {r} HAHA!\033[m\033[7:30m |')
    print('-' * 62)
