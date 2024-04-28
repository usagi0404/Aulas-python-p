import os

os.system("cls || clear")
notas = []
media = 0
soma = 0
calculo = 0
for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
    soma+=1
    calculo+=nota
    media = calculo/soma

for i in range(len(notas)):
    print(f"{i + 1}ª nota: {notas[i]}")

print(f"Media: {media:.2f}")