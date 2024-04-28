import os

# Desafio 22

nome = str(input("Digite seu nome completo: ")).strip()

print(f"Nome maiúsculo: ", nome.upper())
print(f"Nome minúsculo: ", nome.lower())
print(f"Quantas letras ao todo (sem considerar espaços): ", (len(nome)-nome.count(' ')))
print(f"Quantas letras tem o primerio nome: ", (nome.find(' ')))
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}")
print(separa)
