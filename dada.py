from random import randint

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

perguntar = int(input('''Escolha uma opcao para se jogar: 
[0] Pedra
[1] Papel
[2] Tesoura
 Digite sua escolha: '''))

print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[perguntar]))


if computador == 0:
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")


elif computador == 1:
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
   
elif computador == 2:
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
   
else:
    print("Operacao invalida")
