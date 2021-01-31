from datetime import date                               #Importa biblioteca para pegar data e hora do pc

print('='*6, 'DESAFIO 032 - ANO BISSEXTO', '='*6)

ano = int(input('| Digite o ano que quer analisar ou digite 0 para analisar o ano atual: '))    #Recebe ano digitado

if ano == 0:                                            #Se o valor digitado for 0 ele vai pegar o ano da data de hoje e colocar na variável ano
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:   #Se o ano for divisível por 4 e por 400, ou quando dividido por 100 o resto é diferente de 0 então ele diz que o ano é bissexto, se não, diz que não é
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')
