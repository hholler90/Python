n1=float(input('Qual é a primeira nota:'))
n2=float(input('Qula é a segunda nota:'))
media=float((n1+n2)/2)

print('Sua media é {:.2f}'.format(media))
if media < 5.0:
    print('O aluno foi reprovado')
elif media >= 5.0 and media <= 6.9:
    print('O aluno esta de recuperação.')
else:
    print('O aluno foi aprovado.')
