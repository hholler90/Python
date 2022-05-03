salbase=float(1500)
comissao=float(200)

corretor=input('Digite o nome do corretor:')
qtdevendas=int(input('Informe a quantidade de imoveis vendidos:'))
totalvendas=float(input('Informe o valor total de vendas do corretor R$'))
salfinal=salbase + (comissao*qtdevendas)+(totalvendas*0.05)
print('Salario final do corretor {} é de R${:.2f}.'.format(corretor,salfinal))
