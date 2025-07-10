genero=input("Digite seu gênero (M/F):")
idade=int(input("Digite sua idade:"))
tempo=int(input("Digite seus anos de serviço:"))

a = (genero=='F'and idade>=60) or (genero=='M'and idade>=65)
b = tempo>=30
c = idade>=60 and tempo>=25
aposentar = a or b or c

print(f"Pode se aposentar:{aposentar}")