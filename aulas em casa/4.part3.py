import os

# Desafio 17
#Jeito tradicional
#oposto = float(input("Digite o coprimento do cateto oposto: "))
#adja = float(input("Digite o coprimento do cateto adjacente: "))
#soma = (oposto ** 2 + adja ** 2) ** (1/2)
#print(f"A hipotenusa vai medir {soma:.2f}")

#jeito com modulo:
import math
oposto = float(input("Digite o coprimento do cateto oposto: "))
adja = float(input("Digite o coprimento do cateto adjacente: "))
soma = math.hypot(oposto,adja)
print(f"A hipotenusa vai medir {soma:.2f}")