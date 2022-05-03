soma=0
cont=0

for soma in range(1,500):
    if soma%3==0:
        if soma%2!=0:
            soma+=1
            cont+=1
            print(soma)
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
