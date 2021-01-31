from math import hypot                                              #Importa função hipotenusa da biblioteca math
print('=' * 6, 'DESAFIO 017 - CATETO DA HIPOTENUSA', '=' * 6)       #Título - layout
co = float(input('Digite o comprimento do cateto oposto: '))        #Recebe o valor do cateto oposto
ca = float(input('Digite o comprimento do cateto adjacente: '))     #Recebe o valor do cateto adjacente
h = hypot(co, ca)                                                   #Faz o calculo da hipotenusa usando o valor recebido das variáveis
print(f'O comprimento da hipotenusa é: {h:.2f}')                    #Mostra o resultado da conta formatado para mostrar apenas 2 números depois da vírgula