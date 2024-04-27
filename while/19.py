import os
numeros = []
pares = 0
impar = 0
positivo = 0
negativo = 0
maiornumero = 0
menornumero = 99999
contador = 0
t = 0
v = 0
n = 0
somapar = 0
pares1 = 0
impar1 = 0
soma = 0
for t in range(6):
    numero = int(input(f"Digite numero {t+1}: "))
    numeros.append(numero)
    contador+=1

    if numero % 2 == 0:
        soma+=numero
        pares+=1
        pares1 += numero
    else:
        soma+=numero
        impar+=1
        impar1 += numero

    if numero >= 0:
        positivo+=1
    else:
        negativo+=1

    if numero > maiornumero:
        maiornumero = numero

    if numero < menornumero:
        menornumero = numero

mediap = pares1/contador
mediai = impar1/contador
media = soma/contador
os.system("cls || clear")

for numero in reversed(numeros):
    print(f"{t+1}ª valor: {numero}")
    t -=1  

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impar}")
print(f"Numeros inseridos: {contador}")
print(f"Maior numero: {maiornumero}")
print(f"Menor numero: {menornumero}")
print(f"Media dos pares: {mediap:.2f}")
print(f"Media dos impar: {mediai:.2f}")
print(f"Media de todos os numeros: {media:.2f}")


