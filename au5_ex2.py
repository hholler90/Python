from math import hypot
ca=float(input('Qual o valor do adjacente:'))
co=float(input('Qual o valor do oposto:'))
hip=hypot(co,ca)

print('O comprimento da hipotenusa é de {:.2f}'.format(hip))