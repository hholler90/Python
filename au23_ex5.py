atleta=[]
tempo=[]

for x in range(7):
    nome=input('Informe o nome do nadador:')
    tempos=float(input('Informe o tempo do nadador:'))
    atleta.append(nome)
    tempo.append(tempos)

imelhor=tempo.index(min(tempo))#imprime o indice do melhor tempo
ipior=tempo.index(max(tempo))#Inprime o indice do pior tempo
mediatempo=sum(tempo)/len(tempo)

print(f'{atleta[imelhor]} tem o melhor tempo.')
print(f'{atleta[ipior]} tem o piot tempo.')
print(f'Media dos tempos:{mediatempo:.2f}.')