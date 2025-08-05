import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) > 3:
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = primeira + ''.join(meio) + ultima
            resultado.append(palavra_embaralhada)
        else:
            resultado.append(palavra)

    return ' '.join(resultado)


frase = (input("Digite uma frase: "))
resultado = embaralhar_palavras(frase)
print(resultado)