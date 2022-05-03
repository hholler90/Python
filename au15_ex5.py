from operator import truediv
from random import randint
computador=(0,10)
jogador=-1
cont=0

print('Pesei em um numero de 0 a 10,tente adivinhar:')

acertou=False
parlpites=0


while not acertou:
    jogador=int(input('Qual seu palpite?'))
    parlpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais ... tente mais uma vez:')
        elif jogador>computador:
            print('Menos ... tente mais uma vez:')
print('Acertou com {} tesntativas.Parabens'.format(parlpites))