import os

os.system("cls || clear")

desconto: int = 0
resultado: int = 0
preco: int = 0

decisao = int(input("Digite o item que queira comprar (morango - 1, maça - 2)"))
quantidade = float (input("Digite sua quantidade: "))


match (decisao):
    case 1:
        if quantidade <= 5:
            preco = quantidade * 2.50
        else:
            preco = quantidade * 2.20
        if quantidade > 8 or preco > 25:
            desconto = preco * 0.10
    case 2:
        if quantidade <= 5:
            preco = quantidade * 1.80
        else:
            preco = quantidade * 1.50
        if quantidade > 8 or preco > 25:
            desconto = preco * 0.10

total = quantidade * preco
resultado = total - desconto

print(f"O total antes do desconto é: {total}")
print(f"O deconto foi de: {desconto}")
print(f"O total depoi do desconto é: {resultado}")
    



