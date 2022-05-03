n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))

opcao=0

while opcao !=5:
    print('''[1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opcao=int(input('Qual é a sua opcao:'))

    if opcao == 1:
        soma=n1+n1
        print(f'A soma entre {n1} e {n2} = {soma}')
    elif opcao ==2:
        produto=n1*n2
        print(f'O produto entre {n1} e {n2} = {produto}')
    elif opcao == 3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'Entre{n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe novos numeros:')
        n1=int(input('Primeiro numero '))
        n2=int(input('Segundo numero:'))
    elif opcao==5:
        print('Finalizado')
    else:
        print('Opçao invalida.')
    print('#'*10)
print('FIM')