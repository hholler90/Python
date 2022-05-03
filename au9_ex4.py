from datetime import date
anoatual=date.today().year

ano=int(input('O ano do nascimento é:'))

idade=anoatual-ano

print('Se voce nasceu em {} tem anos de idade {}. '.format(ano,idade))

if idade < 18:
    print('Voce ira se alistar em {} anos.'.format(18 - idade))
    print('Voce devera se alistar em {} anos.'.format(anoatual+(18-idade)))

elif idade == 18:
    print('Voce deve se alistar nesse ano {} .'.format(anoatual))

elif idade > 18:
    print('Voce deveria ter se alistade há {} anos.'.format(idade-18))
    print('Voce deveria ter se alistado nao ano de {}.'.format(anoatual - (idade - 18)))

