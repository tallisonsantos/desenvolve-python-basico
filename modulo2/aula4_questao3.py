#Entrada de dados
n1=(input("Digite o nome do produto 1:"))
p1=float(input("Digite o preço unitário do produto 1:"))
q1=int(input("Digite a quantidade do produto 1:"))
n2=(input("Digite o nome do produto 2:"))
p2=float(input("Digite o preço unitário do produto 2:"))
q2=int(input("Digite a quantidade do produto 2:"))
n3=(input("Digite o nome do produto 3:"))
p3=float(input("Digite o preço unitário do produto 3:"))
q3=int(input("Digite a quantidade do produto 3:"))
#Cálculo do preço total
total=(p1*q1)+(p2*q2)+(p3*q3)
#Saída dos resultados
print(f"Total: R${total:,.2f}")