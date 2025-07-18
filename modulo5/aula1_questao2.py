import random
import math

n = int(input("Digite a quantidade de valores inteiros a serem gerados: "))

valores = [random.randint(0, 100) for i in range(n)]
soma = sum(valores)
raiz_quadrada= math.sqrt(soma)

print(f"Valores gerados: {valores}")
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")