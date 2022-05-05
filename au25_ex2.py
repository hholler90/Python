tupla='helicoptero','computador','psicopata','zombi','elefante'
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')