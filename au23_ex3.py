import random 
n=int(input('Informe o valor para N:'))
l1 = [random.randint(1, 10) for x in range(n)]

l2 = [random.randint(1, 10) for x in range(n)]

l3=[]
for i in range(n):
    l3.append(l1[i]+l2[i])
print(l1)
print(l2)
print(l3)
