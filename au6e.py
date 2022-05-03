print('##Programa de emprestimos ## \n Responda: 0 - nao e 1- sim')
nome_n=int(input('Possui nome negativado?'))

if nome_n == 1:
    print('Não pode realizar o emprestimo.')
else:
    carteiraAssinada= int(input('Possui carteira assinada?'))
    if carteiraAssinada == 0:
       print('Não pode realizar o emprestio')
    else:
        possuiCasaPropria=int(input('Possui casa propria?'))

        if possuiCasaPropria == 0:
            print('Não pode realizar o emprestimo')
        else:
            print('Concede o emprestimo')