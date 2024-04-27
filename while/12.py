import os

os.system("cls || clear")
notas = []
soma = 0
contador = 0
media = 0
for i in range(4):
    nota = float(input(f"Digite nota {i+1}: "))
    notas.append(nota)
    soma+=nota
    contador+=1
    media = soma/contador

    
for i in range(len(notas)):
        print(f"{i+1}ª nota: {notas[i]}")

print(f"media: {media:.2f}")
