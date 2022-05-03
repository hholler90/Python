frase=str(input('Digite uma frase:')).upper()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao {}.'.format(frase.find('A')))
print('A ultima letra A apareceu na posiçao {}.'.format(frase.rfind('A')))