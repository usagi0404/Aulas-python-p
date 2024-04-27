import os

os.system("cls || clear")

# Criando váriaveis e atribuindo valores. //tipagem dinamica
#nome = "Alice"
#idade = 20
#peso = 70.333

# Criando váriaveis e atribuindo valores. // Tipagem estática
nome : str = "Alice"
idade : int = 20
peso : float = 70.333

# Exibindo dados para o usuário.
print (f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:3f}")