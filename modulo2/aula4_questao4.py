#Entrada de dados
valor=int(input("Digite um valor inteiro em R$:"))
#Cálculo da quantidade de notas
notas_100=valor//100
valor=valor%100
notas_50=valor//50
valor=valor%50
notas_20=valor//20
valor=valor%20
notas_10=valor//10
valor=valor%10
notas_5=valor//5
valor=valor%5
notas_2=valor//2
valor=valor%2
notas_1=valor//1
valor=valor%1
#Saída dos resultados
print(f"{notas_100} notas de R$100,00")
print(f"{notas_50} notas de R$50,00")
print(f"{notas_20} notas de R$20,00")
print(f"{notas_10} notas de R$10,00")
print(f"{notas_5} notas de R$5,00")
print(f"{notas_2} notas de R$2,00")
print(f"{notas_1} notas de R$1,00")
