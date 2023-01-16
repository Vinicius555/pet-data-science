velocidade_permitida = 80
velocidade_atual = int(input("Informe sua velocidade:"))
if velocidade_atual <= velocidade_permitida:
    print("Não levou muta!")
elif velocidade_atual > velocidade_permitida and velocidade_atual <= velocidade_permitida + 10:
    print("Levou multa leve!")
elif velocidade_atual >= velocidade_permitida + 11  and velocidade_atual <= velocidade_permitida + 20:
    print("levou multa grave!")
else:
    print("Levou multa gravíssima!")