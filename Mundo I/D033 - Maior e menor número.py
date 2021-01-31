print('='*6, 'DESAFIO 033 - NÚMERO MAIOR E MENOR', '='*6)
a = int(input('Digite o número 1: '))                       #Recebe os 3 números
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))

if a < b and a < c:             #Verifica qual é o menor
    menor = a
else:
    if b < a and b < c:
        menor = b
    else:
        if c < a and c < b:
            menor = c


if a > b and a > c:             #Verifica qual é o maior valor
    maior = a
else:
    if b > a and b > c:
        maior = b
    else:
        if c > a and c > b:
            maior = c

print('-'*10)
print(f'O menor número é {menor}')              #Mostra qual o menor e o maior valor
print(f'O maior número é {maior}')
