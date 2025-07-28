#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
Pares=[n for n in range (20,51) if n % 2 == 0]
print(Pares)

#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lista=[1,2,3,4,5,6,7,8,9]
quadrado=[n**2 for n in lista]
print(quadrado)

#Todos os números entre 1 e 100 que sejam divisíveis por 7
divisivel7=[n for n in range(1,100) if n % 7 == 0]
print(divisivel7)

#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento 
Paridade = ["par" if n % 2 == 0 else "ímpar" for n in range(0, 30, 3)]
print(Paridade)