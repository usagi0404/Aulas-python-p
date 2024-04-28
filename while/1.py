import os
os.system("cls || clear")

nota1 = -1
nota2 = -1
med = 0

while nota1 < 0 or nota1 > 10:
    nota1 = int(input(f"Digite sua primeira nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = int(input(f"Digite sua segunda nota: "))

med = (nota1 + nota2) / 2

print(f"A media dos seus numeros é {med}")
