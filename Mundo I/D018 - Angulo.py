import math                                                                         #Importa biblioteca de matemática
print('=' * 6, 'DESAFIO 018 - ANGULOS', '=' * 6)                                    #Título - Layout
print('-' * 23)
a = float(input('| Digite um ângulo: '))                                            #Recebe o ângulo digitado
print('-' * 23)
r = math.radians(a)                                                                 #Converte o ângulo para radiano
print('-' * 35)
print(f'| O angulo de {a} tem:           |\n| SENO: {math.sin(r):<26}|\n| COSSENO: {math.cos(r):<23}|\n| TANGENTE: {math.tan(r):<22}|')      #Mostra o seno, cosseno e tangente do radiano do ângulo
print('-' * 35)
