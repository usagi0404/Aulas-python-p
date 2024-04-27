import os

os.system("cls || clear")

res = "S"
contador = 0
notaf = 0

while res != "N" or res != "n":
    nota = int(input(f"Digite sua nota: "))
    res = str(input(f"Deseja continuar(S ou N)?: "))
    notaf += nota
    contador += 1
    med = notaf / contador

print(f"A media dos seus numeros é {med}")
