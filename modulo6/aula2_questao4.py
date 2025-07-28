l1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {l1} elementos da lista 1:")

lista1 = []
for i in range(l1):
    elemento = int(input())
    lista1.append(elemento)

l2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {l2} elementos da lista 2:")

lista2 = []
for i in range(l2):
    elemento = int(input())
    lista2.append(elemento)

lista3 = []
tamanho_menor = min(len(lista1), len(lista2))

for i in range(tamanho_menor):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if len(lista1) > len(lista2):
    for i in range(tamanho_menor, len(lista1)):
        lista3.append(lista1[i])
elif len(lista2) > len(lista1):
    for i in range(tamanho_menor, len(lista2)):
        lista3.append(lista2[i])

print("Lista intercalada:", *lista3)