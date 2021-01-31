print('\033[31;1;4m-=' * 6, 'DESAFIO 057 - VALIDAÇÃO DE DADOS', '=-' * 6)           #Título

print('\033[0;33;1m-' * 75)

print('| \033[0;30;45m Olá! Por Favor Digite o Seu Sexo Para a Finalização do Cadastro [F/M] \033[0;33;1m |')
print('|', '-' * 71, '|')
s = str(input('| R: ')).strip().upper()[0]                                          #Recebe o sexo digitado

while s not in 'MF':                                                                #Repete enquanto o sexo não for M ou F
        print()
        print('-' * 38)
        print('| \033[30;41m Opção inválida. Tente novamente! \033[0;33;1m |')      #Mensagem de erro
        print('-' * 38)
        print()
        print('-' * 74)
        print('| \033[0;30;45m Por Favor Digite um Sexo Válido Para a Finalização do Cadastro [F/M] \033[0;33;1m |')
        print('|', '-' * 70, '|')
        s = str(input('| R: ')).strip().upper()[0]                                  #Recebe o novo sexo digitado
print()
print('-' * 44)
print('| \033[0;42;30;1m Sexo registrado com sucesso. Obrigado! \033[0;33;1m |')    #Mensagem final de conclusão
print('-' * 44)
