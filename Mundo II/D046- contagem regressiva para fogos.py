from time import sleep                                                              #Importa a função sleep(delay) da biblioteca time
import emoji                                                                        #Importa a biblioteca de emojis

print('\033[36;1;4m-=' * 6, 'DESAFIO 046 - FOGOS', '=-' * 6, '\033[0;32;1;4m')      #Título

for c in range(10, -1, -1):                                                         #Conta de 10 até 0 de 1 em 1 levando 1 segundo para a contagem do próximo número
    print(c)
    sleep(1)
print(emoji.emojize('\033[0;30;1;4;41mBOOOOMMMM!!! :boom: :fireworks: :boom:\033[m', use_aliases=True))     #Mostra o fim da contagem e explosões de fogos
