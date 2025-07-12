N=int(input("Digite o total de experimentos: "))

cont=0
soma_sapo=0
soma_rato=0
soma_coelho=0

while cont<N:
    quantia=int(input("Quantidade de cobaias utilizadas: "))
    tipo=(input("Tipo de cobaia: "))
    if tipo=='S':
        soma_sapo+=quantia
    elif tipo=='R':
        soma_rato+=quantia
    elif tipo=='C':
        soma_coelho+=quantia
    cont+=1
total=soma_coelho+soma_rato+soma_sapo
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {soma_coelho}")
print(f"Total de ratos: {soma_rato}")
print(f"Total de sapos: {soma_sapo}")
print(f"Percentual de coelhos: {(soma_coelho/total)*100:.2f} %")
print(f"Percentual de ratos: {(soma_rato/total)*100:.2f} %")
print(f"Percentual de sapos: {(soma_sapo/total)*100:.2f} %")