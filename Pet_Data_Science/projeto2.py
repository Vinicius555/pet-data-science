from random import randint
valor_aleatorio = randint(1,10)
tenta = 0
while True:
    chute = int(input("Informe um Número:"))
    if chute > valor_aleatorio:
        print("O valor informado e menor.")
    elif chute < valor_aleatorio:
        print("O valor informado e maior.")
    else:
        print("Parabêns você acertou!")
        break
    tenta += 1
print(f"Você acertou na sua {tenta+1 } tentativa!")