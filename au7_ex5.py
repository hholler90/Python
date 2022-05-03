n1=float(input('Digite um numero positivo qualquer:'))
n2=float(input('Digite o segundo numero positivo:'))
menu=int(input('Menu 1 = media pondera com 2 e 3 pesos respequitivos. 2= Quadrado da soma dos dois numeros. 3= Cubo de menor numero.'))
def menor(n1,n2):
    min=n1
    if  n2<min:
     min=n2
     return min
if menu ==1:
    print('A média penderada dos numeros é {} e {} com pesos 2 e 3 respectivamente é:{:.2f}'.format(n1,n2,(n1*2+n2*3)/5))
elif menu==2:
    print('O quadrado da soma dos dois numeros {} e {} é: {:.2f}.'.format(n1,n2,(n1-n2)**2))
elif menu==3:
    print('O do menor numero é {} e o seu cubo é {:.2f}.'.format(menor(n1,n2),(n1,n2)**3))
else:
    print('A opçao é invalida.')