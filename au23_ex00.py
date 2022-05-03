dias=('domingo','segunda','terça','quarta','quinta','sexta','sabado')

semana=list(dias)

print(f'A variavem semana é do tipo {type(semana)} e contem os dias da semana {semana}')
#converte a tupla em lista

nim=[]
for n in range(0,10):
    num=n**2
    num.append(n**2)
print(num)

lista1= [x**2 for x in range(10)]
print(lista1)
#lista comprimida
lista2=[x for x in range(1,20) if x%2==0]
print(lista2)

lista3=[i for i in "HACKATHON" if i in ['A','E','I','O','U']]

lista4=[1,2,3,]
lista4=[i**3 for i in lista4]#atribuir novos valores aos elementos da lista atreves de uma operaçao