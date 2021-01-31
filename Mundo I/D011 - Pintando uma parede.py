print('====== DESAFIO 011 - PINTANDO UMA PAREDE ======')
h = float(input('Digite a altura da parede em metros: '))
b = float(input('Digite a largura da parede em metros: '))
a = h * b
l = a/2
print('A sua parede tem a dimensão de {}x{} e a sua área é de {:.2f}m².\nVocê vai precisar de {:.2f} litros de tinta para pintá-la.'.format(h, b, a, l))
