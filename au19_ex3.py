num=int(input('Digite o numeor inteiro:'))
media=0
soma=0
menor=num
maior=num
while True:
    num=int(input('Digite o numeor inteiro:'))
    
    if menor > num:
        menor=num
    if maior<num:
        maior=num
    media=(maior+menor)/2
    continuar=input('Voce quer continuar [S/N].').upper().strip()
    if continuar == 'N':
        break
print(f'O menor numero é {menor} e o mairo é {maior} a media entre os numeros é {media}.')