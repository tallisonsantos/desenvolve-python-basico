n = int(input("Digite o n: "))

maior = 0

while n>0:
    x = int(input("Digite o x:"))
    if x > maior:
        maior = x
    n=n-1
print(f"{maior}")