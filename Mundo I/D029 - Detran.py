print('=' * 6, 'DESAFIO 029 - DETRAN', '=' * 6)
print('-' * 44)
vel = int(input('| Digite qual é a velocidade do veículo: '))                       #Recebe velocidade
if vel > 80:                                                                        #Se maior que 80 é multado e recebe o valor. A multa é R$7 para cada km acima. Se não, fala para seguir viagem
    m = (vel - 80) * 7
    print('-'*63)
    print('| Você ultrapassou o limite de velocidade de 80Km/h. MULTADO! |')
    print(f'| A sua multa é de R${m:<6.2f}!                                  |')
    print('-'*63)
else:
    print('-'*67)
    print('| Você está dentro do limite de velocidade de 80Km/h. Boa viagem! |')
    print('-'*67)
