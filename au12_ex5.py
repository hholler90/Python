from math import sqrt
from pickle import TRUE

x1=float(input('Digite a coordenada x do ponto 1'))
y1=float(input('Digite a coordenada y do ponto 1'))

x2=float(input('Digite a coordenada x do ponto 2'))
y2=float(input('Digite a coordenada y do ponto 2'))

x3=float(input('Digite a coordenada x do ponto 3'))
y3=float(input('Digite a coordenada y do ponto 3'))

l1= sqrt(pow(x2-x1,2)+pow(y2-y1,2))
l2= sqrt(pow(x3-x2,2)+pow(y3-y1,2))
l3= sqrt(pow(x3-x2,2)+pow(y3-y2,2))

cond1= True
cond2= True
cond3= True

if l1==0 or l2 == 0 or l2 ==0:
    cond1=False

if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    cond2=False
if l1<=abs(l2-l3) or l2<=abs(l1-l3) or l3<=abs(l1-l2):
    cond3=False

triangulo=True

if cond1 == False or cond2==False or cond3==False:
    triangulo=False
    print('Nenhum triangulo formado!')
    if cond1== False:
        print('Pelo menos um dos lados é igual a 0!')

    if cond2==False:
        print('Pelo menos um lado é maior que a soma dos outros dois!')

    if cond3== False:
        print('Um dos lados eé menor ou igual ao módulo da diferença! ')
elif l1==l2==l3:
    print('Triangulo equilatero.')
elif l1!=l2!=l3:
    print('Triangulo é escaleno.')
else:
    print('Triangulo é isoceles.')
if triangulo:
    print('Medida do laod 1:{:.2f} \n Medida do lado 2: {:.2f} \n Medida do lado 3: {:.2f}'.format(l1,l2,l3))