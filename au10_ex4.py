
menu=int(input('**********************************\n PAGAMENTO\n********************** \n 1. a vista dinheiro ou cheque  \n 2. a vista no cartao \n 3. 2x no cartao valor normal.'))
valor=float(input('Qual é o valor a ser pago:'))

a=valor - valor *0.10
b=valor - valor *0.05
c=valor - valor *0.5

if menu==1:
    print('O valor a ser pago é {:.2f} com %10 de desconto.'.format(a))
elif menu==2:
    print('O valor a ser pago é {:.2f} com %5 de desconto.'.format(b))
elif menu==3:
    print('O valor a ser pago é {:.2f} em 2x.'.format(c))
