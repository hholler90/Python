
tentativa=2
stop=False
while not stop :
    nome=input('Digite o seu nome:')
    senha=int(input('Digite a senha:'))
    if senha != 123456 and tentativa ==2:
        tentativa-=1
        print('A senha esta incorreta!,Voce tem mais 2 tentativas ')
    elif senha != 123456 and tentativa ==1:
        tentativa-=1
        print('A senha esta incorreta!,Voce tem mais 1 tentativas')
    elif senha != 123456 and tentativa ==0:
        stop=True
        tentativa-=1
        print('A sua senha foi bloqueada')
    elif senha ==123456:
        stop=True
        print('Olá {} . Seja bem vindo ao nosso banco!'.format(nome))

# jeito da prof

for c in range (3,0,-1):
    senha= int (input('senha:'))
    if senha== 123456:
        print('Ola, seja bem vindo ao nosso banco')
        break
    elif senha != 123456:
        print('Senha incorreta! Voce ainda tem {} tentativa(s)'.format(c=1))
        if c==1:
            print('sua senha foi bloqueada.')
            break