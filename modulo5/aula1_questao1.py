n1= float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

diferenca = abs(n1 - n2)
diferenca_arredondada = round(diferenca, 2)

print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")