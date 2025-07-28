numeros = []

while True:
    try:
        num = int(input("Digite um número inteiro: "))
        numeros.append(num)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    if len(numeros) >= 4:
        continuar = input("Deseja adicionar mais um número? (s/n): ")
        if continuar == 'n':
            break

print(f"Lista original: {numeros}")
print(f"3 primeiros elementos: {numeros[:3]}")
print(f"2 últimos elementos: {numeros[-2:]}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Elementos de índice par: {numeros[0::2]}")
print(f"Elementos de índice ímpar: {numeros[1::2]}")