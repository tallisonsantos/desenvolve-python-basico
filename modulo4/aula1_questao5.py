N=int(input("Digite a quantidade de respondentes: "))
soma=0
cont=0
while(cont < N):
    idade=int(input("Digite a idade do respondente: "))
    soma+=idade
    cont+=1
print(f"A média das idades dos respondentes é: {soma/N}")    
