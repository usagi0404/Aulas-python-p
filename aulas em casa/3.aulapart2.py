import os

os.system("cls || clear")

# Desafio 10

real = float(input("Digite quanto de dinheiro vc tem: R$"))

dolar = real/5.12

print(f"Com R${real} vc pode comprar US${dolar:.2f}")

# Desafio 11

largura = float(input('Digite quanto de largura: '))
altura = float(input('digite quanto de altura: '))


area = largura*altura
lt = area/2

print(f"Sua area de {largura}X{altura} é {area}m e precisa de {lt}L de tinta para pintar")

# Desafio 12
# preçodoproduto*desconto/100 (calculo com desconto)

produto = float(input('quanto vale o produto?R$ '))

  
produto2 = produto*5/100
novoprodut = produto - produto2

print(f"O produto custava {produto} com desconto de 5% agora vale {novoprodut}")

# Desafio 13

salario = float(input("Digite seu salario: "))

salario2 = salario*15/100
novosalari = salario+salario2

print(f"Seu salario de R${salario} com o desconto de 15% ficar R${novosalari}")

# Desafio 14

c = float(input("Quanto graus cº: "))

f = c*1.8+32

print(f"A conversão de {c}cº em fº é {f}fº")

# Desafio 15

carro = float(input("Quanto kl o carro pecorreu?? "))
dias = int(input("Quantos dias o carro foi alugado?: "))

preco = dias*60
km = carro*0.15
final = preco+km

print(f"O carro foi alugado por {dias} e andou por {carro}km")
print(f"O preço cobrado foi R${final}")