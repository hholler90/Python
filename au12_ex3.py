alt1=float(input('Digite a estatua do 1 pessoa:'))
alt2=float(input('Digite a estatua do 2 pessoa:'))
alt3=float(input('Digite a estatua do 3 pessoa:'))

maisalto=alt1
medio=alt2
maisbaixo=alt3

if alt1> alt2 and alt1>alt3:
    maisalto=alt1
    if alt2>alt3:
        medio=alt2
        maisbaixo=alt3
    else:
        medio=alt3
        maisbaixo=alt2
elif alt2>alt1 and alt2>alt3:
    maisalto=alt2
    if alt1>alt3:
        medio=alt1
        maisbaixo=alt3
    else:
        medio=alt3
        maisbaixo=alt1
else:
    maisalto=alt3
    if alt1>alt2:
        medio=alt1
        maisbaixo=alt2
    else:
        medio=alt2
        maisbaixo=alt1

print('Mais alto {:.2f}m. MEDIANO {:.2f}m. Mais baixo {:.2f}m'.format(maisalto,medio,maisbaixo))