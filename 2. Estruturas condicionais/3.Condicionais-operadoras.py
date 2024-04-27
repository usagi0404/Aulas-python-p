import os

os.system("cls || clear")

idade : int 

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("não votar")
else:
    print("pode votar")

print("=== Fim ===")