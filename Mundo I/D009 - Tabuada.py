print('====== DESAFIO00 9 - TABUADA ======')
n = int(input('Digite um número para saber a tabuada dele: '))
c = 1                                                            #Variável contador recebe 1
print('=' * 16)
print(f'| TABUADA DO {n} |')
print('=' * 16)
for c in range(0, 11):                                           #Estrutura de repetição. Para o contador dentro da área de 1 até 10(sempre um número abaixo do digitado) faça:
    print('| {:<2} x {:>2} = {:>2} |'.format(n, c, n * c))                     #Mostra o número digitado vezes o número atual do contador e mostra o resultado da multiplicação

print('-' * 16)

