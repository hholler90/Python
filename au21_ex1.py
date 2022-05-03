lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maiorvalor=lista[0]
menorvalor=lista[0]
listapares=[]
ocorrencia=0
mediaelementos=0
somanegativo=0
for index in range (0,len(lista)):
    if maiorvalor < lista[index]:
        maiorvalor=lista[index]
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    if lista[index]%2==0:
        listapares.append(lista[index])#lista pares =12
    if lista[index]==lista[0]:
        ocorrencia+=1
    mediaelementos+=lista[index]
    if lista[index]<0:
        somanegativo+=lista[index]
mediaelementos/=len(lista)

print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Os numeros pares são: {listapares}')
print(f'Numero de ocorrencias do primeiro elemento: {ocorrencia}')
print(f'A media dos elementos: {mediaelementos}')
print(f'Elementos negativos: {somanegativo}')