frase = (input("Digite uma frase: "))

vogais = "aeiouAEIOU"

nova_frase = ''.join(['*' if c in vogais else c for c in frase])
print(nova_frase)
