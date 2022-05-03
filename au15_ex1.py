from datetime import date
anoatual=date.today().year
cont1=0
cont2=0
for ano in range(1,8):
    ano=int(input('Em que ano voce nasceu?'))
    
    if anoatual-ano >=18:
        cont1 +=1
    elif anoatual-ano < 18:
        cont2 +=1
print('O numero de pessoas que ja atingiram a maioridade é {} e as que ainda nao atingiram é {}'.format(cont2,cont1))