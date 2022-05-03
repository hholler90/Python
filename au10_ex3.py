peso=float(input('Qual é o seu peso:'))
altura=float(input('Qual é a sua altura:'))
imc=peso/altura**2
if imc <= 18.5:
    print('O individuo esta abaixo do peso.')
elif imc >=18.6 and imc <= 25:
    print('O individuo esta com o pesso ideal.')
elif imc >=25.1 and imc <=30:
    print('O individuo esta com sobrepeso.')
elif imc >=30.1 and imc <=40:
    print('O individuo esta com obesidade.')
elif imc >=40.1:
    print('O individuo esta com obesidade morbida.')