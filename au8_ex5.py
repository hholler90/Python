from random import shuffle
n1=str(input('Qual é o nome do aluno:'))
n2=str(input('Qual é o nome do aluno:'))
n3=str(input('Qual é o nome do aluno:'))
n4=str(input('Qual é o nome do aluno:'))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('Qual a ordem de trabalho dos alunos{}.'.format(lista))