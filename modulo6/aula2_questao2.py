import random

num_elementos = random.randint(5,20)
elementos = [random.randint(1,10) for i in range(num_elementos)]

soma = sum(elementos)
media = sum(elementos)/len(elementos)

print(f"A lista elementos:{elementos}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")