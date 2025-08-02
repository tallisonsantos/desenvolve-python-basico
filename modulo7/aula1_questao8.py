cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

def validar_cpf(cpf_str):
    cpf = cpf_str.replace('.', '').replace('-', '')
    
    if not cpf.isdigit() or len(cpf) != 11:
        return "Inválido"

    if cpf == cpf[0] * 11:
        return "Inválido"

    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = 0
    for i in range(9):
        soma2 += int(cpf[i]) * (11 - i)
    soma2 += digito1 * 2
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "Válido"
    else:
        return "Inválido"
    
resultado = validar_cpf(cpf_usuario)
print(resultado)