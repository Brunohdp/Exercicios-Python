print('\033[31;1m-=' * 6, '\033[4mDESAFIO 036 - FINANCIANDO CASA\033[0;1;31m', '=-' * 6)            #Título

c = float(input('\033[0;1;30m| \033[36mDigite o valor da casa: \033[32mR$'))                        #Recebe o valor da casa
s = float(input('\033[0;1;30m| \033[36mDigite o seu salário: \033[32mR$'))                          #Recebe o salário
a = int(input('\033[0;1;30m| \033[36mDigite em quantos anos você vai pagar: '))                     #Recebe os anos de pagamento

print('\033[1;30m-'*94)

m = c / (a * 12)                                                                                    #Faz o cálculo da mensalidade
n = s/100*30                                                                                        #Descobre a porcentagem do salário

if n < m:                                       #Se a mensalidade da casa for superior a 30% do salário da pessoa, ela não consegue financiar, se for abaixo ela consegue
    print(f'''      \033[1;41;30;4mSINTO MUITO, MAS INFELIZMENTE VOCÊ NÃO PODE FINANCIAR ESTA CASA!\033[0;1;30m
É necessário que o valor da \033[33;4;1mmensalidade da casa\033[0;1;30m seja \033[1;37;4migual a\033[0;1;30m ou \033[1;37;4mabaixo de\033[m \033[1;4;35m30%\033[0;1;30m do seu \033[36;4;1msalário\033[0;1;30m,
o que, no seu caso, com \033[36;4;1msalário\033[0;1;30m atual de \033[1;4;32mR${s:.2f}\033[0;1;30m seria equivalente a \033[32;4mR${n:.2f}\033[0;1;30m.
A \033[33;4;1mmensalidade da casa\033[0;1;30m custa \033[1;4;32mR${m:.2f}\033[0;1;30m o que é \033[31;1;4msuperior\033[0;1;30m aos seus \033[1;4;35m30%\033[0;1;30m.''')

else:
    print(f'''      \033[46;1;4mPARABÉNS! VOCÊ PODE FINANCIAR ESTA CASA TRANQUILAMENTE!\033[0;1;30m
É necessário que o valor da \033[33;4;1mmensalidade da casa\033[0;1;30m seja \033[1;37;4migual a\033[0;1;30m ou \033[1;37;4mabaixo de\033[m \033[1;4;35m30%\033[0;1;30m do seu \033[36;4;1msalário\033[0;1;30m,
o que, no seu caso, com \033[36;4;1msalário\033[0;1;30m atual de \033[1;4;32mR${s:.2f}\033[0;1;30m seria equivalente a \033[32;4mR${n:.2f}\033[0;1;30m.
A \033[33;4;1mmensalidade da casa\033[0;1;30m custa \033[1;4;32mR${m:.2f}\033[0;1;30m o que é \033[1;34;4minferior\033[0;1;30m ou \033[1;34;4migual\033[0;1;30m aos seus \033[1;4;35m30%\033[0;1;30m.''')
