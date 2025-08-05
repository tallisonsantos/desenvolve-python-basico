def palindromo(frase):
    limpa = ''.join(c.lower() for c in frase if c.isalnum())
    return limpa == limpa[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    if entrada.lower() == "fim":
        break

    if palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')