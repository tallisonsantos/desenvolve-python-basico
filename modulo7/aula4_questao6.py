def processar_spotify(caminho_arquivo):
    musica_mais_tocada_por_ano = {}

    with open(caminho_arquivo, "r", encoding="latin-1") as f:
        for _ in range(5):
            print(f.readline().rstrip())

    with open(caminho_arquivo, "r", encoding="latin-1") as f:
        cabecalho = f.readline() 

        for linha in f:
            linha = linha.strip()

            if '"' in linha:
                continue

            campos = linha.split(",")

            if len(campos) < 9:
                continue 

            try:
                track_name = campos[0]
                artist_name = campos[1]
                released_year = int(campos[3])
                streams = int(campos[8])
            except:
                continue

            if released_year < 2012 or released_year > 2022:
                continue

            
            if released_year not in musica_mais_tocada_por_ano or streams > musica_mais_tocada_por_ano[released_year][3]:
                musica_mais_tocada_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    lista_final = []
    for ano in range(2012, 2023):
        if ano in musica_mais_tocada_por_ano:
            lista_final.append(musica_mais_tocada_por_ano[ano])

    print(lista_final)


if __name__ == "__main__":
    caminho = "spotify-2023.csv"
    processar_spotify(caminho)