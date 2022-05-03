r1 = float(input("Primeira reta : "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Teceiro reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("A reta acima pode formar o triângulo")
else:
    print("A reta acima não pode formar o triângulo")