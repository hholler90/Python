preço=float(input('Qual o valor do produto:'))
quantidade=float(input('Qual a quantidade de produtos vendidos:'))
comissao=(preço*quantidade)*0.05
print('Comissao é igual a: {:.2f}.'.format(comissao))
