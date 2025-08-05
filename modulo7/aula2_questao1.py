data_nascimento=(input("Digite uma data de nascimento:"))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia, mes, ano = data_nascimento.split("/")

mes_extenso = meses[int(mes) - 1]

print(f"Você nasceu em {int(dia)} de {mes_extenso} de {ano}.")
