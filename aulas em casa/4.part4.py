import math
# from math import radians, sin, cos, tan
#degrees = 180
angulo = float(input("Digite o angulo que vc deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O angulo de {angulo} tem o SENO de {seno:2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O angulo de {angulo} tem o COSSENO de {cosseno:2f}")
tangente = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem a TANGENTE de {tangente:2f}")