import os
os.system("cls || clear")
# Desafio 31

viagem = float(input('Qual é a distancia de sua viagem?: '))

if viagem <= 200:
    valor = viagem * 0.50
    print(f"Voce está preste a começar uma viagem de {viagem}km.")
    print(f"A sua viagem vai custar R${valor:.2f}")
else:
    valor2 = viagem * 0.45
    print(f"Voce está preste a começar uma viagem de {viagem}km.")
    print(f"A sua viagem vai custar {valor2:.2f}")

# Desafio 32
from datetime import date
print("==="*20)
print("Digite 0 se quer analisar o ano atual")
ano = int(input("Digite um ano que deseja analisar se é ou não bissexto: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O Ano {ano} é bissexto")
else:
    print(f"O Ano {ano} não é bissexto")