import random

lista_original = [random.randint(-100,100) for i in range(20)]

lista_ordenada = sorted (lista_original)

indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

print("Lista ordenada (sem modificar a original):")
print(lista_ordenada)

print("Lista original:")
print(lista_original)

print(f"Índice do maior valor ({lista_original[indice_maior]}): {indice_maior}")
print(f"Índice do menor valor ({lista_original[indice_menor]}): {indice_menor}")
