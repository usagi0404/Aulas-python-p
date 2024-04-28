import os

os.system("cls || clear")
numeros = []
numeromaior = 0
numeromenor = 99999
for i in range(5):
    numero = int(input(f"Digite um numero {i+1}: "))
    numeros.append(numero)
    if numero > numeromaior:
        numeromaior = numero
    if numero < numeromenor:
        numeromenor = numero

for i in range(len(numeros)):
    print(f"{i+1}º numero: {numeros[i]}")

print(f"O maior numero é: {numeromaior}")
print(f"O menor numero é: {numeromenor}")