idade=int(input('Idade:'))
maisnovo=idade
maisvelho=idade

while True:
    idade=int(input('Idade:'))
    if idade<0:
        break
    if idade<maisnovo:
        maisnovo=idade
    elif idade>maisvelho:
        maisvelho=idade
media=(maisnovo+maisvelho)/2

print(f'Menor idade: {maisnovo} \n Maior idade: {maisvelho} \n Media das duas idades={media:.2f}')