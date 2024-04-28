import os

os.system("cls || clear")

# Ordem de precedência
# 1 - ();
# 2 - **;            ## ('** = ao cubo || pow(4,3)) <-- outra forma
# 3 - * , /, //, %;  ##('//'= divisão inteira, '/'= divisão real, '%' = resto da divisão)
# 4 - +, -;
# Extra - \n = coloca em baixo || \t = coloca espaço;

# Desafio 5
n1 = int(input("Digite um numero: "))

sucess = n1+1
antece = n1-1

print(f"O seu numero é {n1}\nseu sucessor é {sucess}\ne seu antecessor é {antece}")

# Desafio 6
raiz : float
numero = int(input("Digite um numero: "))

dobro =  numero*2           #numero+numero
triplo =  numero*3          #dobro+numero
raiz = numero**(1/2)

print(f"O seu numero é {numero}\nseu dobro é {dobro}\nseu triplo é {triplo}\ne a raiz quadrada é {raiz}")

# Desafio 7
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))

soma = (nota1+nota2)/2

print(f"Media: {soma}") #{.1f}

# Desafio 8
m1 = float(input("Digite seu numero: "))

cm = m1*100
mm = m1*1000

print(f"Tem {m1} metros\ncentimetros é {cm}\nmilimetros é {mm}")

# Desafio 9
i : int = 0
tabuada = int(input('Digite um numero pra tabuada: '))

for i in range(1,11):
    print(f'{tabuada} X {i} = {tabuada * i}')
    