import os

senha = str(input("Digite a senha (tem que conter os numeros "123" nela): ")).strip()
fim = "senha" in senha.lower()

print(f"A senha contem "123"? {fim}")