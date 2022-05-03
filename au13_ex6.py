n1=int(input('Digite o primeiro termo da PA:'))
razao=int(input('Digite a razao da PA:'))
decimo =n1 +(10-1)*razao

for c in range(n1,decimo+razao,razao):
    formula=n1+razao
    print(c,end='==>')
print('Fim')