import os
os.system("cls || clear")
km = float(input("Digite quanto de velosidade está seu carro:  "))

# DESAFIO 30
if km > 80:
    multa = (km-80)*7
    print("VOCE ESTA ACIMA DO LIMITE DE VELOSIDADE!!")
    print("O LIMITE DE VELOSIDADE E NO MINIMO 80KM/h!!")
    print(f"VOCE FOI MULTADO POR R${multa}")
print("Tenha um Bom dia! Dirija com segurança")

# DESAFIO 31
# Outra forma de descobrir se um numero é impar ou par é (numero %2 = resultado se for 1 é impar se 0 é par)
numero = int(input("DIgite um numero: "))

if numero %2 == 0:
    print(f"O numeor {numero} é um numero par")
else:
    print(f"O numero {numero} é um numero impar")