from random import randrange

linha=int(input('Numeros de linhas: '))
coluna=int(input('Numeros de colunas:'))

a=[[randrange(1,11)for i in range(coluna)]for j in range (linha)]
b=[[randrange(1,11)for i in range(coluna)]for j in range (linha)]

abaixo=0
acima=0

for i in range (linha):
    for j in range (coluna):
        if i>j:
            abaixo+=a[i][j]
    if i<j:
        acima+=b[i][j]
print('Ma triz A:')
for i in range(linha):
    for j in range(coluna):
        print(a[i][j],end=' ')
    print()

print('Matriz B')
for i in range(linha):
    for j in range(coluna):
        print(b[i][j],end=' ')
    print()

print(f'Soma={abaixo+acima}')