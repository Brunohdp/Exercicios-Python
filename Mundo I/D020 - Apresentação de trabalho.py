import random                                                           #Importa a biblioteca random
print('-' * 6, 'DESAFIO 020 - APRESENTAÇÃO DE TRABALHO', '-' * 6)       #Título - layout
a1 = str(input('Aluno 1: '))                                            #Recebe os nomes dos alunos
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]                                                #Cria uma lista com os alunos das variáveis
a = random.shuffle(lista)                                               #Embaralha os ítens da lista
print(f'A ordem de apresentação de trabalhos é:\n {lista}')             #Mostra a ordem de apresentação