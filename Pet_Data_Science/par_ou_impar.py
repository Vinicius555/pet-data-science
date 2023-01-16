while True:
    print("="*20)
    print("Par ou Ímpar")
    print("="*20)
    per = str(input("Deseja Jogar(s/n)?")) 
    if per == "s":
        try:
            num = int(input("Digite um Número:"))
            if num % 2 == 0:
                print(f"O número {num} e Par.")
            else:
                print(f"O número {num} e Ímpar.")
        except:
                print("Digite apenas Números!")     
    else:
        break
print("=="*25)
print("Obrigado Por jogar meu jogo!:)")
    