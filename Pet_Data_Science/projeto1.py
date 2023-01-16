num = int(input("Digite um número:"))
cont = num
fatorial = 1
if num > 0:
    print(f"{num}!",end='')
    while cont > 0:
        print(f" {cont} * ",end='')
        fatorial *= cont
        cont -= 1
    print(f" = {fatorial}")
else:
    print("O número precisa ser positivo!")