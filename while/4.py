import os

os.system("cls || clear")

res = "S"
contador = 0
notaf = 0

while res == "S":
    nota = float(input(f"Digite sua nota: "))
    notaf += nota
    contador += 1
    med = notaf / contador

    print("---------MENU---------")
    print("S - Insira mais uma nota")
    print("V - Ver quantas notas foram inseridas")
    print("N - Calcular a media aritmetica das notas informadas")
    res = str(input(f"Digite sua resposta: "))
    
    if res == "V":
        print(f"A quantidade de notas inseridas é {contador}")
    if res == "N":
        print(f"A media das notas inseridas é {med}")


