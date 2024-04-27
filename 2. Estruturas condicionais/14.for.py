import os

os.system("cls || clear")

i : int = 0

numero = int(input("Digite o numero: "))
valor = numero
valor2 = numero
fim = numero*11

for numero in range (0, fim, numero):
        print(f"Numero {valor2} vezes {i} é igual {valor*i}")
        i=i+1


