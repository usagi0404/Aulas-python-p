import os

os.system("cls || clear")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade <= 65:
        print("Pode votar")
    else:
        print("não precisa votar")
else:
    print("Não precisa votar")