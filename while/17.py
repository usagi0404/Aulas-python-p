import os

os.system("cls || clear")
numeros = []
pares = 0
impar = 0
negativo = 0
positivo = 0
i = 0

while i != 5:
    numero = int(input(f"Digite {i+1}ª numero: "))
    
    if numero % 2 == 0:
        pares+=1
    else:
        impar+=1

    if numero >= 0:
        positivo+=1
    else:
        negativo+=1
    i += 1
    
print(f"numeros pares: {pares}")
print(f"Numeros impar: {impar}")
print(f"Numeros positivo: {positivo}")
print(f"Numero negativos: {negativo}")
print(f"Numeros inseridos: {i}")