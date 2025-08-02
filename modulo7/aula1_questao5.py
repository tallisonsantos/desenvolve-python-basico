frase = (input("Digite uma frase: "))

contador = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        contador += 1
        indices.append(i)
    
print(f"{contador} vogais")
print(f"Indices {indices}")


