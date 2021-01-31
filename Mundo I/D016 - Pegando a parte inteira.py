#import math                                                             #Importa a biblioteca math que acrescenta funções matemáticas
from math import trunc                                                  #Inporta somente a função trunc da biblioteca math
print('=' * 6, 'DESAFIO 016 - PRGANDO A PARTE INTEIRA', '=' * 6)        #Título
r = float(input('| Digite um número real: '))                           #Recebe o número digitado em float
print('-' * 36)                                                         #Layout
print(f'| A porção inteira de {r:^5} é: {trunc(r):^4}|')                #Quebra a parte inteira do número digitado e mostra ela
print('-' * 36)                                                         #Layout
