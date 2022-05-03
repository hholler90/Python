idade=0
homen=0
mulher=0
continuar=False
while not continuar:
    sexo=input('Sexo [F/M]').strip().upper()
    idade=int(input('Idade:'))
    if sexo in 'M' and idade >18:
        homen+=1
    if sexo in 'F' and idade :
        mulher+=1
    if idade<0:
        continuar=True
             
print('A quantidade de homens acima de 18 anos é {} e a quantidade de mulheres é {}'.format(homen,mulher))

# JEITO DA PROF
mulher=0
homen18=0

while True:
    idade=int(input('Qual sua idade:'))
    if idade<0:
        break
    sexo=input('sexo:').upper()
    if sexo =='F':
        mulher+=1
    elif sexo == 'M' and idade>18:
        homen18+=1
print(f'Total de mulheres:{mulher} \nTotal de homens acima de 18 anos:{homen18}')