lista=['janaina','jose','maria','carlos']

#for n in range (0,len(lista)):
    #print(lista[n],end=' ')

lista.append('jorge')
print(lista)

lista.insert(0,'jorge')
print (lista)

lista.sort()#sort para ordenar alfabetica
print(lista) 

lista.sort(reverse=True)#ordena ao contrario com numeros negativos remove o inverso
print(lista)

del lista[3]#para remover da lista

lista.remove('janaina')#REMOVE UM ESPECIFICO

lista.pop()#remove a ultima ou alguma especifica dentro do ()

lista.clear()#elimina a lista

listaa=lista#vincula as listas

listaa=lista[:]#desvincula as listas

lista.extend(listaa)#junta duas listas diferentes

print(lista.cont('jose'))#conta quantos jose tem na lista #usar len pra contar quantos nomes tem na lista

print(lista.index('janaina'))#mosta em que posiçao o nome esta

for indice,nome in enumerate(lista):
    print(f'{nome}esta armazenado no indice{indice}')#mostra os elementos da lista e onde estao no vetor

a=[[2,1,-5],[3,7,0],[6,4,8]]

print(a[0][0]+a[0][1]+a[0][2])#para somar // # usar , ao inves de + para so listar 

soma_a=0
lin=len(a)
col=len(a[0])
for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]
print(soma_a)#soma as listas