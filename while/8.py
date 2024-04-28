import os

os.system("cls || claer")
poderosas = 0
quantidade = 0
idademaior = 0
idademenor = 99999
opcao = 0


while opcao == "1":
    sexo = str(input("Digite seu sexo (F ou M)): "))
    idade = int(input("Digite sua idade: "))

    if idade > idademaior:
        idademaior+=1
    else:
        idademenor+=1

    salario = float(input("Digite seu salario: "))
    quantidade+=1
    salario +=salario

print("1- adicionar mais pessoas")
print("2-mostrar resultados")
print("3-sair")
opcao = str(input("Digite sua opcao:"))

if idade == "F" and salario > 5.000:
    poderosas+= 1

    if opcao == "2":
        print(f"O salario medio é {salario}")
        print(f"A maior idade é {idademaior}")
        print(f"A menor idade é {idademenor}")
        print(f"A quantidade de mulheres com salario maior de 5 mil é {poderosas}")

    




