
cont=soma=0

while True:
    n=int(input('Qual é o numero inteiro:'))
    if n ==999:
        break
    cont+=1
    soma+=n
    
print(f'O total de numeros é {cont} e a soma deles é {soma}')