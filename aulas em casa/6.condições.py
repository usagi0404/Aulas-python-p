import random
import os
from time import sleep
os.system("cls || clear")
# Desafio 28
print("Estou pensando em um numero de 0 a 5, vc consegue adivinhar que numero é?")
n = int(input("escolhar um numero de 0 a 5: "))
numero = [0, 1, 2, 3, 4, 5]
result = random.choice(numero)

if n == result:
    print(f"O numero que eu pensei foi {result}! vc acertou!")
else:
    print(f"O numero que eu pensei foi {result}, vc errou")


# Desafio 28
from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print("vou pensar em um numero de 0  a 5. tente adivinhar.")
jogador = int(input('em que numero eu pensei? '))
print("PROCESSANDO....")
sleep(3)
print("==="*20)
if jogador == computador:
    print(f"Eu pensei no numero {computador} e voce colocou o numero {jogador}")
    print("Parabens! voce consegui me vencer!")
else:
    print(f"GANHEI! eu pensei no numero {computador} e não no numero {jogador}")
