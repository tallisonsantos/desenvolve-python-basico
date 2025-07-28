import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = []
for valor in lista1:
    if valor in lista2 and valor not in interseccao:
        interseccao.append(valor)

interseccao.sort()

contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"Interseccao: {interseccao}")

print("Contagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={contagem1[valor]}, lista2={contagem2[valor]})")