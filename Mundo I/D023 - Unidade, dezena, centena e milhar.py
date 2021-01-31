print('=' * 6, 'DESAFIO 023 - UNIDADE, DEZENA, CENTENA E MILHAR', '=' * 6)      #Título
print('-' * 39)
n = int(input('| Digite um número de 0 até 9999: '))    #Recebe o número digitado
u = n // 1 % 10                                         #Faz a divisão inteira do número por 1 e pega o resto da divisão por 10, que é exatamente a unidade
d = n // 10 % 10                                        #Faz a divisão inteira do número por 10 e pega o resto da divisão por 10, que é exatamente a dezena
c = n // 100 % 10                                       #Faz a divisão inteira do número por 100 e pega o resto da divisão por 10, que é exatamente a centena
m = n // 1000 % 10                                      #Faz a divisão inteira do número por 1000 e pega o resto da divisão por 10, que é exatamente o milhar
print('-' * 39)
print('-' * 16)
print(f'''| Unidade: {u:>3} |
| Dezena: {d:>4} |
| Centena: {c:>3} |
| Milhar: {m:>4} |''')                                  #Exibide o resultado todo formatado
print('-' * 16)
