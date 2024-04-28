import os


os.system("cls || clear")

numeros = []
repet = 0
while numeros == repet:

    for i in range(6):
        numero = float(input(f"Digite nota {1+i}: "))
    numeros.append(numero)

if numero[i] % 2 != 0 and numero[i] < 0:
    repet+=numero[i]
while numeros == repet:

    for i in range(len(numeros)):

        print(f"{i+1}ª nota: {numeros[i]}")

