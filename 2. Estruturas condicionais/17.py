import os

os.system("cls || clear")

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} numero par")
    else:
        print(f"{i} numero impar")
#O laço de repetição só vai mostrar os numeros impares:
for i in range(1, 21):
    if i % 2 != 0: #if i% 2 == 1: outra forma de ter impar
        print(f"{i} numero impares")
    