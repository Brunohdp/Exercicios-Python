print('=' * 6, 'DESAFIO 017 - CATETO DA HIPOTENUSA', '-' * 6)   #Título - layout
co = float(input('Digite o valor do cateto oposto: '))          #Recebe o valor do cateto oposto digitado
ca = float(input('Digite o valor do cateto adjacente: '))       #Recebe o valor do cateto adjacente digitado
h = ((ca ** 2) + (co ** 2)) ** (1/2)                            #Faz a soma dos catetos² e tira a raiz para se obter a hipotenusa
print(f'O valor da hipotenusa é: {h:.2f}²')                     #Mostra o resultado formatado para mostrar apenas 2 números depois da vírgula