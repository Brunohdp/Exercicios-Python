print('=' * 6, 'DESAFIO 026 - POSIÇÃO DO A', '=' * 6)
print('-' * 70)
s = str(input('| Digite uma frase: ')).lower().strip()                            #Recebe a frase, joga tudo para minúsculo e tira os espaços excedentes antes e depois se houver
print('-' * 70)
print('-' * 59)
print(f'''| A letra "A" aparece {s.count("a"):^3} vezes                           |
| A primeira vez que ela aparece, ela está na posição {s.find("a")+1:<3} |
| A última vez que ela aparece, ela está na posição {s.rfind("a")+1:<5} |''')     #Conta quantas vezes a letra 'a' aparece,
print('-' * 59)                                                                   #qual é a primeira e a última posição dela.
                                                                                  #Porém, ele vai somar 1 nos dois, para mostrar a posição como nós veríamos.
                                                                                  #A gente não vê a primeira letra e diz que tá na posição 0, a gente diz que tá na posição 1