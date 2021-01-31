print('=' * 6, 'DESAFIO 025 - SILVA NO NOME', '=' * 6)      #Título

print('-' * 60)
n = str(input('| Digite seu nome completo: '))              #Recebe o nome
print('-' * 60)
s = 'Silva' in n                                            #Procura o nome Silva dentro da srt

if s == True:                                               #Se tiver, ou seja, for True, então ele escreve que tem,
    print('-' * 28)                                         #Caso contrário, escreve que não.
    print(f'| Você tem "Silva" no nome |')
    print('-' * 28)
else:
    print('-' * 32)
    print('| Você não tem "Silva" no nome |')
    print('-' * 32)
