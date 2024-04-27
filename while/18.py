import os

os.system("cls || clear")

numero = 1
pares = 0
impar = 0
negativo = 0
positivo = 0
a = 0
contador = 0

while numero != 0:
    numero = int(input(f"Digite {a+1}ª numero: "))
    a+=1
    contador+=1

    if numero % 2 == 0:
        pares+=1
    else:
        impar+=1

    if numero >= 0:
        positivo+=1
    else:
        negativo+=1

print(f"numeros pares: {pares}")
print(f"Numeros impar: {impar}")
print(f"Numeros positivo: {positivo}")
print(f"Numero negativos: {negativo}")
print(f"Numeros inseridos: {contador}")