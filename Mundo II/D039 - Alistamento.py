from datetime import date               #Importa a função data do datetime. Vai pegar a data do computudor

print('\033[31;1m-='*6, '\033[4mDESAFIO 039 - ALISTAMENTO\033[0;31;1m', '=-'*6)     #Título

s = str(input('\033[mDigite qual é o seu sexo biológico [F/M]: ')).strip().upper()


if s == 'F':
    print('Você não precisa fazer o alistamento obrigatório!')
    r = str(input('Deseja prosseguir e se alistar mesmo assim? [S/N] ')).strip().upper()
    if r == 'S':
        n = str(input('\033[1;30mDigite o seu nome completo: ')).strip().title()            #Recebe o nome completo
        a = int(input('Digite o ano de nascimento: '))                                      #Recebe a data de nascimento
        ano = date.today().year                                                             #Recebe a data do sistema
        i = ano - a                                                                         #Faz o cálculo da idade da pessoa

        print('\033[7m-'*90, '\033[0;1;30m')

        if i < 18:                                                  #Se tiver menos de 18 diz quantos anos ainda faltam para se alistar e diz em qual ano será
            t = 18 - i                                              #Faz o cálculo de quantos anos faltam
            falta = ano + t                                         #Faz o cálculo para saber em que ano será

            print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, \033[4;35mainda terá\033[0;1;30m que se alistar no serviço militar!')
            print(f'Ainda faltam \033[34;1;4m{t} anos\033[0;30;1m para o seu alistamento.')
            print(f'Seu alistamento será em {falta}')               #Mostra as informações

        elif i == 18:                                               #Se a idade for igual a 18 anos, diz que tem que se alistar esse ano
            print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, já \033[33;4;1mestá na hora\033[0;1;30m de se alistar. Procure uma central de alistamento!')

        else:                                                       #Se nenhuma das anteriores for vdd, ou seja, se a idade for maior que 18 diz que o tempo já passou e quantos anos foram e em qual ano deveria ter se alistado
            t = i - 18                                              #Faz os cálculos de quantos anos passaram
            passou = ano - t                                        #Calcula em que ano foi

            print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, \033[31;4mperdeu\033[0;1;30m a data do alistamento.')
            print(f'Já passaram \033[31;4m{t} anos\033[0;1;30m do seu tempo para se alistar.')
            print(f'O seu alistamento foi em \033[1;35;4m{passou}')         #Mostra as informações
    else:
        print('Você está dispensada!')
else:
    n = str(input('\033[1;30mDigite o seu nome completo: ')).strip().title()            #Recebe o nome completo
    a = int(input('Digite o ano de nascimento: '))                                      #Recebe a data de nascimento
    ano = date.today().year                                                             #Recebe a data do sistema
    i = ano - a                                                                         #Faz o cálculo da idade da pessoa

    print('\033[7m-'*90, '\033[0;1;30m')

    if i < 18:                                                  #Se tiver menos de 18 diz quantos anos ainda faltam para se alistar e diz em qual ano será
        t = 18 - i                                              #Faz o cálculo de quantos anos faltam
        falta = ano + t                                         #Faz o cálculo para saber em que ano será

        print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, \033[4;35mainda terá\033[0;1;30m que se alistar no serviço militar!')
        print(f'Ainda faltam \033[34;1;4m{t} anos\033[0;30;1m para o seu alistamento.')
        print(f'Seu alistamento será em {falta}')               #Mostra as informações

    elif i == 18:                                               #Se a idade for igual a 18 anos, diz que tem que se alistar esse ano
        print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, já \033[33;4;1mestá na hora\033[0;1;30m de se alistar. Procure uma central de alistamento!')

    else:                                                       #Se nenhuma das anteriores for vdd, ou seja, se a idade for maior que 18 diz que o tempo já passou e quantos anos foram e em qual ano deveria ter se alistado
        t = i - 18                                              #Faz os cálculos de quantos anos passaram
        passou = ano - t                                        #Calcula em que ano foi

        print(f'Você, \033[32;4;1m{n}\033[m, \033[34;4;1m{i}\033[0;1;30m anos, \033[31;4mperdeu\033[0;1;30m a data do alistamento.')
        print(f'Já passaram \033[31;4m{t} anos\033[0;1;30m do seu tempo para se alistar.')
        print(f'O seu alistamento foi em \033[1;35;4m{passou}')         #Mostra as informações
