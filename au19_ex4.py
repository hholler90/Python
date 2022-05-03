while True:
    num=int(input('Digite o numero:'))
    if num<0:
        print('O programa foi finalizado.')
        break
    for c in range(1,11):
        print(f'{num}x{c}={num*c}')
