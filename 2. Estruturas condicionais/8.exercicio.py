import os

os.system("cls || clear")

login = str(input("Digite seu login: "))
senha = int(input("Digite sua senha: "))

if login == "Alice":
    if senha == 1234:
        print("Bem-vindo")
    else:
        print("Login ou senha inválido")
else: 
        print("Login ou senha inválido")
        