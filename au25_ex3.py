import random
l2=1
n=int(input('Informe o valor para N:'))
l1 = [random.randint(1, 10) for x in range(n)]
for i in l1:
   l2*=i
mediag=l2**1/len(l1)
print(l1)
print(f'A media geometrica é {mediag}')