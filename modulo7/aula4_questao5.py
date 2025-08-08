livros = [
    ("Os segredos da mente milionária", "T. Harv Eker", 2005, 192),
    ("Mindset", "Carol S. Dweck", 2006, 320),
    ("Hábitos Atômicos", "James Clear", 2018, 320),
    ("O Ladrão de Raios", "Rick Riordan", 2005, 377),
    ("Poder Sem Limites", "Tony Robbins", 1986, 344),
    ("Quem Mexeu no Meu Queijo?", "Spencer Johnson", 1998, 96),
    ("A Arte da Guerra", "Sun Tzu", -500, 273),
    ("A Lei da Atração", "Michael J. Losier", 2006, 272),
    ("O Poder do Hábito", "Charles Duhigg", 2012, 371),
    ("O Maior Vendedor do Mundo", "Og Mandino", 1968, 111),
]

with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = ",".join(str(campo) for campo in livro)
        arquivo.write(linha + "\n")