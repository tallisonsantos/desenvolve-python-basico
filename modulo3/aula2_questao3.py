idade=int(input("Digite sua idade:"))
jogos=(input("Já jogou pelo menos 3 jogos de tabuleiro (True/False)?"))
venceu=int(input("Quantos jogos já venceu?"))

ingressar= (idade>=16 or idade<=18)and(jogos=='True'or jogos=='true')and(venceu>=1)

print(f"Pode entrar no clube: {ingressar}")

