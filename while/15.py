import os
os.system("cls || clear")
numeros = []
resul = 0
for i in range(5):
    numero = int(input(f"Digite um numero {i+1}: "))

    if numero < 0:
        numero = 0
    numeros.append(numero)

for i in range(len(numeros)):
    print(f"{i+1}ª numero: {numeros[i]}")