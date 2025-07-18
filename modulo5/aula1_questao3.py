import random

aleatorio = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite < aleatorio:
        print("Muito baixo, tente novamente!\n")
    elif palpite > aleatorio:
        print("Muito alto, tente novamente!\n")
    else:
        print(f"Correto! O número é {aleatorio}.")
        break