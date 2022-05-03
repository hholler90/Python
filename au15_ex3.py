somaidade=0
maioridadeh=0
nomemaisvelho=''
mulherm=0
media=0
for p in range(1,5):
    nome=input('Nome:').strip()
    idade=int(input('Idade:'))
    sexo=input('Sexo [F/M]').strip().upper()
    somaidade+=idade
    if p==1 and sexo in 'M':
        maioridadeh=idade
        nomemaisvelho=nome
    if sexo in 'M'and idade>maioridadeh:
        maioridadeh=idade
        nomemaisvelho=nome

    if sexo in 'F' and idade <20:
        mulherm+=1

media=somaidade/4
print('A media de idade do grupo é de {} anos'.formt(media))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridadeh))
print('Ao todo sao {} mulheres com menos de 20 anos'.formta(mulherm))