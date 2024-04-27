import os

os.system("cls || clear")

desconto: int = 0
resultado: int = 0

produto = str(input("Digite o produto: "))
quantidade = float(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))


if quantidade <= 5:
    desconto = preco * 0.02
elif quantidade <= 5:
    if quantidade <= 10:
        desconto = preco * 0.03
    else:
        desconto = preco * 0.05

total = quantidade * preco
resultado = total - desconto

print(f"O total antes do desconto é: {total}")
print(f"O desconto foi de: {desconto}")
print(f"O total depois do desconto é: {resultado}")


