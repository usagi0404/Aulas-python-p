import os

os.system("cls || clear")
numeros = []
positivo = 0
negativo = 0
for i in range(10):
    numero = int(input(f"Digite um numero {i+1}: "))
    numeros.append(numero)
    
    if numero >= 0:
        positivo+=numero
    else:
        negativo+=1

for i in range(len(numeros)):
    print(f"{i+1}ª numero: {numeros[i]}")

print(f"A soma de numeros positivos: {positivo} ")
print(f"Quantidade de numeros negativos: {negativo}")