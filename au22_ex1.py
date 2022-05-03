v1=int(input('Primeiro valor:'))
v2=int(input('Segundo valor:'))
v3=int(input('Terceiro valor:'))
v4=int(input('Quarto valor:'))
lista=(v1,v2,v3,v4)
listapares=[]
for index in range (0,len(lista)):
    if lista[index]%2==0:
        listapares.append(lista[index])
print(f'O numero 9 apareceu {(lista.count(9))} vezes')
print(f'O numero 3 apareceu na posiçao {(lista.index(3))}')





print(f'Os numeros pares são: {listapares}')