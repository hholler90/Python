from random import triangular


lin=int(input('Numero de linhas:'))
col=int(input('Numero de colunas'))

if lin!=col:
    print('Matriz nao é trinagular')
else:
    m=[]
    triangular=True
    for i in range(lin):
        elem=[]
        for j in range(col):
            elem.append(int(input(f'M[{i+1}][{j+i}]=')))
        m.append(elem)
print('Matriz M:')
for i in range(lin):
    for j in range(col):
        print(m[i][j], end=' ')
    print()
    for i in range(lin):
        for j in range (col):
            if i<j:
                if m [i][j]!=0:
                    triangular=False
    if triangular==True:
        print('M é matriz triangular inferior.')
    else:
        print('M nao é uma matriz triangular inferior. ')