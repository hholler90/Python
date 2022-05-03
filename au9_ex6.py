menu=int(input('**********************\n CALCULO DE GRANDEZAS\n*****************************\n1.TENSAO em V \n2. RESISTENCIA em Ω \n3. CORRENTE em A:'))
if menu==1:
    resis=float(input('Qual é o valor da resistencia:'))
    corrente=float(input('Qual é o valor da corrente:'))
    print('O valor da tensao é {:.2f}V.'.format(resis*corrente))
elif menu==2:
    corrente=float(input('Qual é o valor da corrente:'))
    tensao=float(input('Qual é o valor da tensão:'))
    print('O valor da resistencia é {:.2f} Ω '.format(tensao/corrente))
else:
    tensao=float(input('Qual é o valor da tensão:'))
    resis=float(input('Qual é o valor da resistencia:'))
    print('O valor da corrente é {:.2f} A.'.format(tensao/resis))
    