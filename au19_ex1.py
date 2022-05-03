num = int(input('Digite um número de termo para sequência Fibonacci: '))

cont = 1

anterior = 0
proxima = 1
soma = 1

while cont <= num:
     print(anterior, end='-')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
print('Fim')
#jeito da prof

#0-1-1-2-3

n=int(input('Quantos termos voce quer mostrar?'))
t1=0
t2=1

print(f'{t1}->{t2}', end='')
cont=3
while cont<=n:
    t3=t1+t2
    print(f'-> {t3}',end='')
    t1=t2
    t2=t3
    cont+=1
print('-> Fim!')
