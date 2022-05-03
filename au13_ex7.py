m= 'M'
f= 'F'
sexo= ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa, [F] para feminino ou [M] para masculino: ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Digite certo, JAGUARA!!!!!!!')
    if sexo=='M':
        print('O sexo é Masculino')
    elif sexo=="F":
        print('O sexo é FEMININO')

# segundo modo
sexo=input('Informe seu sexo [M/F]:').strip().upper()
while sexo not in 'MF':
    sexo=input('Dados invalidos. por favor, informe seu sexo [M/F]:').strip().upper()
print('Sexo {} registro com sucesso.'.format(sexo))