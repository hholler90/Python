termo=int(input('Informe o primeiro termo da PA:'))
ntermo=int(input('Informe o numero de termos da PA:'))
razao=int(input('Informe a razao da PA:'))

pa = [termo]
termoanterior=termo

for x in range(ntermo-1):
    termoatual=termoanterior+razao
    pa.append(termoatual)
print(pa)
soma=sum(pa)

print(f'Soma dos elementos da PA = {soma}')