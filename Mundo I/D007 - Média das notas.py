print('|====== DESAFIO 007 - MÉDIA DE NOTAS ======|')
n1 = float(input('| Digite a primeira nota: '))         #Recebe primeira nota e converte para float
n2 = float(input('| Digite a segunda nota: '))          #Recebe segunda nota e converte para float
m = (n1+n2)/2                                           #Soma as duas notas e divide por 2
print('---------------------------------------------')  #Layout
print('| A média entre as notas {} e {} é: [{}] |'.format(n1, n2, m))   #Exibe as duas notas e a média delas
if m >= 7:                                                              #Se a nota for maior que sete diz que o aluno foi aprovado, se não, diz que foi reprovado
    print('| Aluno APROVADO! |')
else:
    print('| Aluno REPROVADO! |')
