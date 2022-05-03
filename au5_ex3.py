from importlib.resources import read_binary
from math import sin,cos,tan,radians
angulo=float(input('Qual é o angulo:'))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print('O valor de seno é {:.2f} o de cossno é {:.2f} e da tangente é {:.2f} para o angulo {:.2f}'.format(seno,cosseno,tangente,angulo))