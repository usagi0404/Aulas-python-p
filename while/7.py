import os

os.system("cls || clear")
n1 = 0
contador = 0
soma = 0
pares = 0
impares = 0

while n1 != 0:
    n1 = int(input("Digite um numero? "))

    if n1 => 0:
        contador+=1
        soma+=n1
        media = soma/contador
    if n1 % 2 == 0:
        pares+=1
    else:
        impares+=1
        

