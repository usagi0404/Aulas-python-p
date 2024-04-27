import os

os.system("cls || clear")
i = 0
contador = 0
soma = 0
numero = 0

while numero >= 0:
    numero = int(input("Digite um numero: "))
    
    if numero >= 0:
        contador += 1
        soma +=numero
        media = soma/contador

print(f"Media: {media}")