import os
os.system("cls || clear")
idades = []
sexos = []

for i in range(2):
    idade = int(input(f"Digite sua idade {i+1}: "))
    idades.append(idade)
    sexo = str(input("Digite seu sexo (F ou M): "))
    sexos.append(sexo)


for i in range(len(idades)):
    print(f"{i+1}ª idade: {idades[i]}")
    for i in range(len(sexos)):
        print(f"{i+1}ª sexo: {sexos[i]}")