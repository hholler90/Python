km=float(input('Quantos quilometros o carro percorreu:'))
dias=float(input('Por quantos dias o carro foi usado:'))
dia=dias*60
kms=km*0.15
print('O total gasto foi de {:.2f}R$.'.format(dia+kms))