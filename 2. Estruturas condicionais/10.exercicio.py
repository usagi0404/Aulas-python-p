import os

os.system("cls || clear")

pares: int = 0
impares: int = 0

numero1 = int(input("Digite o primeiro numero: "))

if numero1 % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

numero2 = int(input("Digite o segundo numero:"))

if numero2 % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

numero3 = int(input("Digite o terceiro nmero: "))

if numero3 % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
            
numero4 = int(input("Digite o quarto numero: "))

if numero4 % 2 == 0:
        pares = pares + 1
else:
        impares = impares + 1
                
numero5 = int(input("Digite o quinto numero: "))

if numero5 % 2 == 0:
        pares = pares + 1
else:
        impares = impares + 1

soma = (numero1+numero2+numero3+numero4+numero5)

print(f"A soma de todos os números lidos são: {soma}")
print(f"Os Numeros pares são: {pares}")
print(f"Os numeros impares são: {impares}")
    