n=int(input('Quanto numero serao mediados:'))
soma=0
for c in range(n):
    numero=float(input('Digite as medias:'))
    soma+=numero
    media=soma/n
print('A quandidade de medias é {} e a media é {:.2f}.'.format(n,media))
