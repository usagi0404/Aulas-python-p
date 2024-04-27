import os

os.system("cls || clear")

#int exp: 7, -4, 0, 8799.
#float exp: 4.5, 0.076, -15.223, 7.0.
#bool exp: True, False.    obs:sempre a primeira letra maiúsculo.
#str exp: "olá", "7.0", "".


#(type(i)) - o type identificar o tipo do primitivo.
#(i.isnumeric()) - identifica o tipo int
#(i.isalpha()) - identifica o tipo str
#(i.isalnum()) - identifica o tanto o tipo int e str 
#(i.isupper()) - identifica só letras maiúsculas
#(i.uslower()) - identifica só letra minuscula

#Desafio 4
n = input("Digite algo: ")

print("O tipo primitivo desse valor é", type(n))
print("Só tem espaços? ", n.isspace())
print("È um numero?", n.isnumeric())
print("È um alfabético? ", n.isalpha())
print("È alfanumérico? ", n.isalnum())
print("Èsta em maiúsculo?", n.isupper())
print("Èsta em minúsculo?", n.islower())
print("Èsta capitalizado?", n.istitle())