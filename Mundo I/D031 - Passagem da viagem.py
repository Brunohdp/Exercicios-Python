print('='*6, 'DESAFIO 031 - PASSAGEM DA VIAGEM', '='*6)

km = float(input('Digite quantos Km a sua viagem terá: '))          #Recebe a distância

if km <= 200:                       #se for menor que 200 faz vezes 0.50 para ver o valor, se não, vezes 0.45
    p = km * 0.50
else:
    p = km * 0.45

print('-'*68)
print(f'| Você pagará R${p:<6.2f} pela sua passagem para a viagem de {km:<4}km! |')     #Mostra o resultado
print('-'*68)
