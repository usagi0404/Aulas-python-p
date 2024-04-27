import os
os.system("cls || clear")

# Desafio 24
cidade = str(input("Digite o lugar que vc mora: ")).strip()
print(cidade[:5].upper() == "SANTO")
# Desafio 25

nome = str(input("Qual e o seu nome completo? ")).strip()
resul = 'silva' in nome.lower()
print(f'Seu nome tem silva? {resul}')