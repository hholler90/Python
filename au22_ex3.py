from random import randint
lista=[]
tamanho=0
while True:
    nomes=input('Digite o nome:')

    if nomes=='stop':
        break
    lista.append(nomes)
tamanho=len(lista)
sorteados=randint(0,tamanho)
print(f'O sorteado foi {lista[sorteados]}')