import os
# Desafio 26
frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"Ela aparece na primeira vez na posição {(frase.find('A')+1)}")
print(f"A ultima posição que A apareceu foi na posição {(frase.rfind('A')+1)} ")

# Desafio 27
n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"seu ultimo nome é {nome[len(nome)-1]}")