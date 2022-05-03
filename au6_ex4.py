distancia = float(input("Qual a distância da sua viagem? "))

print("Você está prestes a começar uma viagem de {:.1f}Km.".format(distancia))
print("E o preço da sua viagem será de R${:.2f}".format(distancia*0.5 if distancia <= 200 else distancia*0.45))