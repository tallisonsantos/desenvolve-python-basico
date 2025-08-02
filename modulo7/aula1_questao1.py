nome=(input("Digite seu nome: "))

tam=-1
for tam in range(len(nome)):
    tam+=1
    letras = nome[0:tam]
    print(letras)