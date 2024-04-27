import os

os.system("cls || clear")
notas = []

for i in range(3):
    nota = float(input(F"Digite a nota {i + 1}: "))
    notas.append(nota)

print(f"Tamanho do vetor: {len(notas)}") #quantos ventores vc colocou

for i in range(len(notas)):
    print(f"{i+1}ª Nota: {notas[i]}")