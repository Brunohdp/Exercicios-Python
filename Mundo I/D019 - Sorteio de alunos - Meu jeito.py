import random
print('=' * 6, 'DESAFIO 019 - SORTEIO DE ALUNOS', '=' * 6)
a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
al = random.randint(1, 4)
if al == 1:
    print(f'O aluno que irá apagar o quadro é {a}!')
else:
    if al == 2:
        print(f'O aluno que irá apagar o quadro é {b}!')
    else:
        if al == 3:
            print(f'O aluno que irá apagar o quadro é {c}!')
        else:
            print(f'O aluno que irá apagar o quadro é {d}!')