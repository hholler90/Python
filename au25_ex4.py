import random

jogos=int(input('O numeros de jogos gerados sera:'))


for i in range(jogos):
    l1 = [random.randint(1, 60) for x in range(0,6)]
    l1.sort()
    print(l1)
