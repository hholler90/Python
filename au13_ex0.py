cont=1
while cont<=1000:
    print('Olá')
    cont += 1  #cont=cont+1
print('Fim')

soma=0
termo=1
while termo <=10:
    soma += termo
    termo+=1
print(soma)
c=1
while c<10:
    print(c)
    c+=1
print('FIM')

for cont in range(1,4000):
    print('Olá')
print('Fim')

for c in range(1,5):
    print('Aula 13')
    
for c in range (0,5):
        print(c)

for c in range (5,0,-1):
    print(c)

for c in range (0,7,2):
    print(c)

n=int(input('Digite um numero:'))
for c in range(0,n+1):
    print(c)

n=1
while n!=0:
    n=int(input('Digite um valor:'))
print('Fim')

r='s'
while r=='s':
    n=int(input('Digite um valor:'))
    r=str(input('Quer continuar [s/n]')).upper()
print('Fim')

i=int(input('Inicio:'))
f=int(input('Fim'))
p=int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s=0
for c in range(0,4):
    n=int(input('Digite um valor:'))
    s+=n
print(s)

while True:
    n1=int(input('Informe o primeiro numero:'))
    n2=int(input('Informe o segundo numero:'))
    if n2==0:
        print('Divisor nao pode ser 0. \n Programa sera encerrado.')
        break
    divisao=n1/n2
    print('{}/{}={:.2f}'.format(n1,n2,divisao))
