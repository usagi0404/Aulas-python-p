import os
os.system("cls || clear")
# Desafio 35
a = float(input("Digite o primeiro segmento:"))
b = float(input("Digite o segundo segmento:"))
c = float(input("Digite o terceiro segmento:"))

if a+b > c and a+c > b and b+c > a:
    print("Os segmentos podem forma um triangulo")
else:
    print("Os segmentos não podem formar um triangulo")