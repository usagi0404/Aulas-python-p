import os 
os.system(" cls || clear")

salario = float(input("Digite seu salario: "))
resul = 0
resul2 = 0
if salario > 1250:
    soma = salario * 0.10
    resul = salario+soma
    print(f"O seu salario de {salario:.2f} com 10% foi aumentado pra {resul}")
else:
    soma = salario * 0.15
    resul2 = salario+soma
    print(f"O seu salario de {salario:.2f} com 15% foi aumentado pra {resul2}")