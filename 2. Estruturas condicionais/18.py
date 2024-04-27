import os

os.system("cls || clear")

j = 1
soma = 0

for i in range (0, 5, 1):
    numero = int(input(f"Digite {j}º numero: "))
    j += 1
    soma += numero

print(f"A soma de todos os numeros é: {soma}")

