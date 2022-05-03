soma=0
a=int(input('Qual é o primeiro numero:'))
b=int(input('Qual é o segundo numero:'))


for c in range(2):
    if a<b:
        print('ERRO 5002')
        break
    if a>b:
        soma=a+b
print(f'A soma dos valores é {soma}')