vel=float(input('Qual é a velocidade do carro:'))

if vel> 80:
    print('Voce foi multado! Ultrapassou o limite de 80km/h')
    multa=(vel - 80) * 7
    print('A multa custara R${:.2f}'.format(multa))
else:
    print('Esta dentro do limite permitido de velocidade')
