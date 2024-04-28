import os

os.system("cls || clear")
n =0
t =0
v =[]
while t != 6:
    n= int(input(f"Digite o {t+1} valor: "))

    if n >=0 and n %2 == 0:
        t += 1
        v.append(n)
os.system("cls || clear")

for n in reversed(v):
    print(f"{t}ª valor: {n}")
    t -=1   