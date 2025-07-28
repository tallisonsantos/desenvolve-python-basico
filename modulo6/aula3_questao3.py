import random

lista = [random.randint(-10,10) for i in range(20)]
print(f"Original: {lista}")

max_inicio = max_fim = None
temp_inicio = None
max_len = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        temp_inicio = i
        while i < len(lista) and lista[i] < 0:
            i += 1
        temp_fim = i
        if temp_fim - temp_inicio > max_len:
            max_inicio, max_fim = temp_inicio, temp_fim
            max_len = temp_fim - temp_inicio
    else:
        i += 1

if max_inicio is not None:
    del lista[max_inicio:max_fim]

print("Editada:", lista)
