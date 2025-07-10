distancia=int(input("Digite a distância da entrega em Km:"))
peso=int(input("digite o peso do pacote em Kg:"))

if(peso>10):
    taxa=10
else:
    taxa=0

if (distancia<=100):
    frete=peso*1+taxa
    print(f"O preço do frete é: R${frete}")
if (distancia>=101 and distancia<=300):
    frete=peso*1.5+taxa
    print(f"O preço do frete é: R${frete}")
if (distancia>300):
    frete=peso*2+taxa
    print(f"O preço do frete é: R${frete}")

