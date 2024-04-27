
#len(frase)
#frase.count('o') - Exp: frase.count('o, 0, 13')
#frase.find('deo')
#'curso' in frase = 'true'

# Transformação
# frase.replace('python', 'Android')
# frase.upper() - Transforma letras minuscula em letra maiuscula
# frase.lower()  -transforma letras maiuscula em minuscula
# frase.capitalize() - ela pega todas as letras e deixar em minuscula menos a primeira.
# frase.title() - ela analisa e colocar apenas a primeira letra de uma palavra em maiusculo toda vez que vc adicionar um espaço.
# frase.strip() - remover todos os espaços inutil apenas dos lado (exp:XXaprenda pythonXX)
# frase.rstrip() - remover apenas os ultimos espaços.
# frase.lstrip() - remover apenas os da esquerda.
# import randiant - gera um numero aleatorio (exp: computador = randiant(0, 5))
# Divisão
# frase.split() dividir uma straing em uma lista (exp 0-(bom)1-(dia))
# '-'.join(frase) - adiciona traços nos espaços

import os
frase = "curso em video Python"
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('curso' in frase)
print(frase.find('Video'))
print(frase.lower().find('Video'))

print("""According to various official materials from Sega, Sonic is described 
as a character who is "like the wind": a drifter who lives as he wants, 
and makes life a series of events and adventures.""")

print(frase.split())
