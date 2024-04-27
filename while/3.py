import os

os.system("cls || clear")

nota1 = -1
nota2 = -1
nota3 = -1
med = 0

while nota1 < 0 or nota1 > 10:
    nota1 = float(input(f"Digite sua primeira nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input(f"Digite sua segunda nota: "))

while nota3 < 0 or nota3 > 10:
    nota3 = float(input(f"Digite sua terceira nota: "))

med = (nota1 + nota2 + nota3) / 3

if med > 7:
    print(f"A media dos seus numeros é {med}, voce esta aprovado")
elif med >= 5 and med <= 6.9:
    print(f"A media dos seus numeros é {med}, voce esta em recuperação")
else:
    print(f"A media dos seus numeros é {med}, voce esta  reprovado")