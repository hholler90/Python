soma=0
nome=input('Qual é o nome do remedio:')
valor=float(input('Qual é preço do remedio:'))
menor=valor
nomem=nome
soma+=valor
media=0
for c in range (4):
    nome=input('Qual é o nome do remedio:')
    valor=float(input('Qual é preço do remedio:'))
    
    if valor < menor:
        menor=valor
        nomem=nome
    soma+=valor
media=soma/5

print('O remedio de menor valor é o {} e seu valor é {:.2f}'.format(nomem,menor))
print('E a media dos valores é {:.2f}'.format(media))


