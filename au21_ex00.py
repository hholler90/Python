dias=('domingo','segunda','terça','quarta','quinta','sexta','sabado')#tupla
print(dias[3])

texto='python'
tuple(texto)
print(tuple(texto))


lista=[1,2,3,4]
lista[2]=8
print(tuple(lista))

lista=[3,5]
tupla2=(1,2,lista[0],lista[1])
tupla1=(1,2,lista)
#print(tupla)
#print(tupla[2])
#print(len(tupla2))
print(tupla2.count(2))
lista=['python',1,2,'java']
print(lista)

meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n=1
while n<4:
    mes=int(input('Escolha um mes[1-12]:'))
    if 1<=mes<13:
        print(f'O mes é {meses[mes-1]}')
        n+=1
meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
#meses.append('janaina')
#print(meses[:-3])
#print(meses*2)
#meses+=['janaina','zé']
#print(meses)
for mes in meses:
    print(mes,end=' ')
