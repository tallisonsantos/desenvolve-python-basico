frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

anagramas = []

for palavra in frase.split():
    if sorted(palavra.lower()) == sorted(objetivo.lower()):
        anagramas.append(palavra)

print("Anagramas:", anagramas)

        
