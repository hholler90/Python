
cont=0
lista=[]
mid=0
n=int(input('Informe quantos numeros serao informados:'))

while cont<n:
    num=int(input('Infome um numero:'))
    lista.append(num)
    cont+=1
mid=int(len(lista)/2)
c=lista[mid]
f=1
print('Calculando {}! = '.format(c),end='')
while c>0:
    print('{}'.format(c),end='')
    print('x'if c> 1 else '=',end='')
    f*=c
    c-=1
    print(f'{f}')