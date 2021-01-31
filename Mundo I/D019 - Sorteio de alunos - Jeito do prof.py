import random                                                           #Importa biblioteca de aleatorização
print('=' * 6, 'DESAFIO 019 - SORTEIO DE ALUNOS', '=' * 6)              #Título - layout
n1 = str(input('Aluno 1: '))                                            #Variáveis recebem nomes de alunos
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4]                                                #Cria uma lista com todos os nomes dentro
a = random.choice(lista)                                                #A biblioteca irá sortear um nome a partir dos que existem na lista
print(f'O(a) aluno(a) sorteado(a) para apagar o quadro foi: {a}!')      #Mostra quem foi o(a) aluno(a) sorteado(a)