import os

os.system("cls || clear")

nota : int
soma : int

nome : input
idade : int

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = int(input("Digite nota 1: "))
nota2 = int(input("Digite nota 2: "))
nota3 = int(input("Digite nota 3: "))
nota4 = int(input("Digite nota 4: "))

soma = (nota1+nota2+nota3+nota4)/4


print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade}")
print(f"todas suas notas: {nota1} - {nota2} - {nota3} - {nota4}")
print(f"Sua media é: {soma}")

