def limpar_e_salvar():
    with open("frase.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    texto_limpo = ""
    for char in texto:
        if char.isalpha() or char.isspace():
            texto_limpo += char

    palavras = texto_limpo.split()

    with open("palavras.txt", "w", encoding="utf-8") as f:
        for palavra in palavras:
            f.write(palavra + "\n")

    with open("palavras.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    print("Conteúdo de palavras.txt:")
    print(conteudo)

if __name__ == "__main__":
    limpar_e_salvar()