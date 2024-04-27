import os 
os.system("cls || clear")
# Desafio 33
numeros = []
maiornumero = 0
menornumero = 99999
for i in range(3):
    numero = int(input(f"DIgite {i+1}ª numero: "))
    numeros.append(numero)
    
    if numero > maiornumero:
        maiornumero = numero
    if numero < menornumero:
        menornumero = numero


for i in range(len(numeros)):
    print("==="*20)
    print(f"{i+1}º numero: {numeros[i]}")

print(f"O maior numero é: {maiornumero}")
print(f"O menor numero é: {menornumero}")