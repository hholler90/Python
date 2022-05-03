from random import choice
n1=input('Qual o nome do aluno:')
n2=input('Qual o nome do aluno:')
n3=input('Qual o nome do aluno:')
n4=input('Qual o nome do aluno:')
lista=[n1,n2,n3,n4]
escolha=choice(lista)
print('O aluno escolhido é {}.'.format(escolha))