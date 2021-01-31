print('=' * 6, 'DESAFIO 022 - MANIPULANDO NOME COMPLETO', '=' * 6)                  #Título - layout
n = str(input('| Digite seu nome completo: '))                                      #Recebe o nome completo
sp = n.split()                                                                      #Divide todos os nomes separados por espaços em indexações diferentes
j = ''.join(sp)                                                                     #Junta todos as indexações em uma única str sem nenhum espaço
print('-' * 80)
print(f'''| O seu nome completo com todas as letras maiúsculas é {n.upper()} |
| Seu nome completo com todas as letras minúsculas é {n.lower()} |
| Seu nome tem {len(j)} letras desconsiderando os espaços |
| Seu primeiro nome tem {len(sp[0])} letras |''')

''' ↑ - Coloca todas as letras em maiúsculas, minúsculas, mostra a quantidade de letras existente na junçao sem espaços 
para contar apenas as letras e falar quantas tem, mostra a quantidade de letras do split 0 para contar quantas 
letras tem apenas o primeiro nome'''