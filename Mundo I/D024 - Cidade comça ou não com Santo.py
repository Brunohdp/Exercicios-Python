print('=' * 6, 'DESAFIO 024 - CIDADE SANTO', '=' * 6)
print('-' * 45)
c = str(input('| Digite o nome da sua cidade: ')).strip().capitalize()              #Recebe o nome da cidade, retira todos os espaços excedentes antes e depois do nome e formata o nome para que fique apenas com a primeira letra maiúscula.
print('-' * 45)
s = c.find('Santo')                                                                 #Procura a palavra santo no nome da cidade

if s == 0:                                                                          #Se o começo do nome da cidade estiver no índice 0, então a cidade começa com a palavra santo, caso contrário, não começa
    print('-' * 75)
    print(f'| O nome da sua cidade é {c:^15} e ela COMEÇA com o nome "Santo"! |')
    print('-' * 75)
else:
    print('-' * 79)
    print(f'| O nome da sua cidade é {c:^15} e ela NÃO COMEÇA com o nome "Santo"! |')
    print('-' * 79)
