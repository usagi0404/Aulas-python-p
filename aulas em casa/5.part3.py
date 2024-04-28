import os
# Desafio 23

#numero = int(input("Informe um numero: "))
#n = str(numero)
#print(f"Analizando o numero: {n}")
#print(f"Unidade: {(n[3])}")
#print(f"Dezena: {n[2]}")
#print(f"Centena: {n[1]}")
#print(f"Milhar: {n[0]}")


numero = int(input("Informe um numero: "))
u = numero// 1 % 10
d = numero// 10 % 10
c = numero// 100% 10
m = numero// 1000% 10
print(f"Analizando o numero: {numero}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")