import random

def carregar_enforcado(caminho_enforcado):
    with open(caminho_enforcado, "r", encoding="utf-8") as f:
        conteudo = f.read()

    estagios = conteudo.strip().split("\n\n")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def escolher_palavra(caminho_palavras):
    with open(caminho_palavras, "r", encoding="utf-8") as f:
        palavras = []
        for linha in f:
            linha = linha.strip()
            if linha != "":
                palavras.append(linha)
    return random.choice(palavras).lower()

def jogar_forca():
    caminho_palavras = "gabarito_forca.txt"
    caminho_enforcado = "gabarito_enforcado.txt"

    palavra = escolher_palavra(caminho_palavras)
    estagios = carregar_enforcado(caminho_enforcado)

    letras_descobertas = ["_" for _ in palavra]
    letras_usadas = []
    erros = 0
    max_erros = 6

    print("Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")
    print(" ".join(letras_descobertas))

    while erros < max_erros and "".join(letras_descobertas) != palavra:
        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            print(f"Boa! A letra '{letra}' está na palavra.")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
        else:
            erros += 1
            print(f"Errou! A letra '{letra}' não está na palavra.")
            imprime_enforcado(erros, estagios)

        print("Palavra:", " ".join(letras_descobertas))
        print("Letras usadas:", ", ".join(letras_usadas))
        print(f"Erros: {erros}/{max_erros}\n")

    if "".join(letras_descobertas) == palavra:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Fim de jogo! A palavra era: {palavra}")
        imprime_enforcado(erros, estagios)

if __name__ == "__main__":
    jogar_forca()