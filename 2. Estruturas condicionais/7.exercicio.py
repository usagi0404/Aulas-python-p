import os

os.system("cls || clear")


inteiro1 = int(input("Digite o valor do produto 1: "))
inteiro2 = int(input("Digite o valor do produto 2: "))

soma = inteiro1+inteiro2
media = soma/2

produto = inteiro1 * inteiro2

if inteiro1 > inteiro2:
    print(f"O maior numero é : {inteiro1}")
    print(f"O menor numero é : {inteiro2} ")
elif inteiro1 == inteiro2:
    print("Os valores são iguais")
else :
    print(f"O maior numero é: {inteiro2}")
    print(f"O menor numero é: {inteiro1}")
 


print(f"A media é: {media}")
print(f"A soma é: {soma}")
print(f"O valor dos produtos8 é: {produto}")
