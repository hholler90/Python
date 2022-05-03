menu=int(input('**********************************\n AUMENTO \n********************** \n 1. PROGRAMADOR  \n 2. ANALISTA S \n 3. ANALISTA BD \n 4. NENHUMA DAS OPÇOES.'))

salario=float(input('Qual é o salario do funcionario:'))

a=salario + (salario*30/100)
b=salario + (salario*20/100)
c=salario + (salario*15/100)
d=0
if menu==1:
    print('O aumento do seu salario sera de {:.2f} R$.'.format(a))
elif menu==2:
    print('O aumento do seu salario sera de {:.2f} R$. '.format(b))
elif menu==3:
    print('O aumento do seu salario sera de {:.2f} R$. '.format(c))
elif menu==4:
    print('O seu salario nao tera ajuste.'.format(d))

