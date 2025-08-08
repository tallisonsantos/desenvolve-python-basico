def processar_roteiro(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='latin1') as f:
        linhas = f.readlines()

    # 1. Imprime as primeiras 25 linhas
    print("Primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(f"{i+1:2d}: {linhas[i].rstrip()}")

    # 2. Número total de linhas
    total_linhas = len(linhas)
    print(f"\nTotal de linhas: {total_linhas}")

    # 3. Linha com maior número de caracteres
    max_len = 0
    linha_mais_longa = ""
    for i in range(len(linhas)):
        comprimento = len(linhas[i].rstrip('\n'))
        if comprimento > max_len:
            max_len = comprimento
            linha_mais_longa = linhas[i].rstrip('\n')
    print(f"\nLinha com maior número de caracteres ({max_len} chars):")
    print(linha_mais_longa)

    # 4. Contagem de menções
    nonato_count = 0
    iria_count = 0

    for i in range(len(linhas)):
        linha = linhas[i]
        linha = linha.replace(",", " ").replace(".", " ").replace(";", " ").replace(":", " ")
        palavras = linha.split()

        for j in range(len(palavras)):
            palavra = palavras[j].strip().casefold()
            if palavra == "nonato":
                nonato_count += 1
            elif palavra == "íria" or palavra == "iria":
                iria_count += 1

    print(f"\nMenções a 'Nonato': {nonato_count}")
    print(f"Menções a 'Íria': {iria_count}")

if __name__ == "__main__":
    caminho = "estomago.txt"
    processar_roteiro(caminho)