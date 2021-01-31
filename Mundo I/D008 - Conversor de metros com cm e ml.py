print('====== DESAFIO 008 - CONVERSOR DE METROS EM CM E ML ======')
m = float(input('Digite um valor em metros: '))             #Recebe valor em metros
km = m/1000
hm = m/100
dm = m/10
dc = m*10
cm = m*100                                                  #Multiplica o valor de metros em 100 para converter para cms
mm = m*1000                                                 #Multiplica o valor de cms em 100 para converter para mls
print(f'{m} metros é igual à:\n{km} Km;\n{hm} Hm;\n{dm} Dm;\n{dc} Dc;\n{cm} Cm;\n{mm} Mm;')      #Exibe a quantidade de metros convertida em todos os valores
