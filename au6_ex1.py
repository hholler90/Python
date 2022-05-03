from random import randint
computador=randint(0,5)
print('Vou pensar em um nuemro entr 0 e 5,tente adivinhar')
jogador= int(input('Em que numero estour penando?'))
 
if jogador==computador:
    print('Parabens, voce acertou!')
else:
    print('Ganhei, estava pensando no numero {}, voce errou!'.format(computador))

