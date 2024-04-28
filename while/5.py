import os

os.system("cls || clear")

notas = 0
contador = 0
opcao = "S"

while opcao == "S":
    nota = float(input("Digite uma nota: "))
    contador += 1
    notas += nota
    print("S - Deseja inserir mais uma nota? ")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a media das notas")
    opcao = str(input("Selecione o que deseja: "))
if opcao == "P":
    print(f"foram inseridas {contador} notas")
elif opcao == "N":
    media = notas/contador
    print(f"A media é {media:.2f}")
else:
    print("Resposta incorreta tente novamente")
    opcao == "S"
