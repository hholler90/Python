from calendar import isleap
ano=int(input('Qual é o ano:'))
if isleap(ano):
    print('O ano é bissexto.')
else:
    print('O ano nao é bissexto.')