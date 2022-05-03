
maior=0
menor=1000

for c in range(1,6):
    peso=float(input('Qual é o seu peso?'))
    if peso > maior:
        maior=peso
    elif peso < menor:
        menor=peso
print('O maior peso é {} e o menor é {}'.format(maior,menor))