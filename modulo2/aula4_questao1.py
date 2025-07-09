#Entrada de dados
comprimento = int(input("Digite o comprimento:"))
largura     = int(input("Digite a largura:"))
preco_m2    = float(input("Digite o valor do m² da região:"))
#Cálculo da área e do preço total
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
#Saída dos resultados
print(f"O terreno possui 31{area_m2}m² e custa R${preco_total:,.2f}")