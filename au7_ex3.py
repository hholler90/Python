salario=float(input('O salario é:'))

print('O seu salario aumentara para 10% ou 15% {:.1f} '.format(salario))
print('O almento do salario sera de {:.2f}'.format(salario*0.10 if salario <= 1250.00 else salario*0.15 ))