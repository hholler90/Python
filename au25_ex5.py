from random import randrange
soma=0
linha=int(input('Numeros de linhas: '))
coluna=int(input('Numeros de colunas:'))

a=[[randrange(0,2)for i in range(coluna)]for j in range (linha)]
for i in range (linha):
    for j in range (coluna):
        soma+=a[i][j]
for i in range(linha):
    for j in range(coluna):
        print(a[i][j],end=' ')
    print()
if soma==0:
    print('A matriz é numa')
else:
    print('Nao é nula')
