produtos=   (   'leite',4.99,
                'arroz',15.90,
                'batata',8.55,
                'feijao',13.89,
            'ovos',6.60)
print('-'*30)
print('            TABELA      ')
print('-'*30)
for pos in range(0,len(produtos)):
    if pos% 2==0:
        print(f'{produtos[pos]:.<20}',end=' ')
    else:
        print(f'R${produtos[pos]:.>3.2f}')