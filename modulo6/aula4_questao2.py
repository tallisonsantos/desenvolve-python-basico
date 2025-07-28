frase = input("Digite uma frase: ")

vogais_lista = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vogais = sorted([letra for letra in frase if letra in vogais_lista])
consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais_lista]

print(f"Vogais: {vogais}")
print(f"Consoantes:{consoantes}")