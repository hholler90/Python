from datetime import date
anoatual=date.today().year

ano=int(input('O ano do nascimento é:'))

idade=anoatual-ano
print('Se voce nasceu em {} tem anos de idade {}. '.format(ano,idade))

if idade < 9:
    print('O atleta esta classificado como MIRIM.'.format(9-idade))
elif idade >= 9 and idade <=14:
    print('O atleta esta classificado como INFANTIL.'.format(14-idade))
elif idade >= 14 and idade <= 19:
    print('O atketa esta classificado como JUNIOR.'.format(19-idade))
elif idade >= 19 and idade <=25:
    print('O atleta esta classificado como SENIOR.'.format(25-idade))
elif idade >= 25:
    print('O atleta esta classificado como MATER.')