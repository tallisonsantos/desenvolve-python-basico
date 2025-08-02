numero = (input("Digite o número: "))

if len(numero) == 8:
    numero ='9'+ numero
    numero = numero[0:5] +'-' + numero[5:10]
    print(numero)
elif len(numero) == 9 and numero[0] == '9':
    numero = numero[0:5] +'-' + numero[5:10]
    print(numero)
else:
    print(f"Número Inválido")