valor=float(input('Qual é o valor da camiseta:'))
quantidade=int(input('Quantas camisas vao ser compradas:'))
vtotal=quantidade*valor
print('O valor total fica  {}.'.format(vtotal))
if quantidade <=5:
    print('Voce pagara {:.2f} %3 de desconto pelas camisetas'.format(vtotal - vtotal*0.03))
elif quantidade >=5 and quantidade <= 10:
    print('Voce pagara {:.2f} %5 de desconto pelas camisetas'.format(vtotal - vtotal*0.05))
elif quantidade >10:
    print('O valor a ser pago é {:.2f} %10 de desconto pelas camisetas.'.format(vtotal - vtotal*0.07))