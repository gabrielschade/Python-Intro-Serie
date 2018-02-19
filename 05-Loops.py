"""
Lista de dez números
"""

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


"""
Imprimindo individualmente
"""

print (numeros[0])
print (numeros[1])
print (numeros[2])
print (numeros[3])
print (numeros[4])
print (numeros[5])
print (numeros[6])
print (numeros[7])
print (numeros[8])
print (numeros[9])

"""
Utilizando laço de repetição
"""
for numero in numeros:
    print (numero)


"""
Utilizando Range
"""
print ("Utilizando range")

valor = 0
for indice in range(5):
    valor += 10
    print(valor)

"""
Utilizando Range com 2 parâmetros
"""
print ("Utilizando range com 2 parâmetros")
for valor in range(5, 10):
    print(valor)

    """
Utilizando Range com 3 parâmetros
"""
print ("Utilizando range com 3 parâmetros")
for valor in range(0, 10,2):
    print(valor)













































"""
Faça um programa que inicialize uma lista de compras com 5 itens diferentes e exiba 
todos utilizando um laço de repetição.
"""

itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
for item in itens_compra:
    print(item)







"""
Faça um programa que inicialize que crie uma lista com os valores de 1 até 10 e 
depois exiba apenas os números pares. 
"""

for numero in range(1,11):
    if numero % 2 == 0:
        print(numero)











"""
Faça um programa que exiba todos os valores ímpares entre 50 e 100 utilizando o range.
"""

for numero in range(51,101,2):
    print(numero)






















"""
Faça um programa que inicialize uma lista vazia, solicite ao usuário 10 números diferentes, um por vez. 
Caso o número digitado seja par, acrescente um ao seu valor. Depois disso, exiba os 10 números digitados.
"""
numeros = []
for numero in range(10):
    item_digitado = int ( input("Digite um valor: ") )
    if(item_digitado % 2 ==0):
        item_digitado += 1
    numeros.append(item_digitado)

for numero in numeros:
    print(numero)


























"""
Faça um programa que exiba as tabuadas de 1 até 10 no formato: "2 x 3 = 6", (utilize dois comandos `for`)
"""
for operador in range(1,11):
    for operador_2 in range(1,11):
        resultado = operador * operador_2
        print(f"{operador} X {operador_2} = {resultado}")