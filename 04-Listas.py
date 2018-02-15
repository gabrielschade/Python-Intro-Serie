""" Lista vazia"""
lista_de_compras = []

""" Lista com itens"""
lista_de_compras = ["Pão", "Água", "Leite", "Ovos"]

print(lista_de_compras[0])
print(lista_de_compras[1])
print(lista_de_compras[2])
print(lista_de_compras[3])

print(lista_de_compras[-1])
print(lista_de_compras[-2])
print(lista_de_compras[-3])
print(lista_de_compras[-4])

""" Alterando um elemento da lista """

lista_de_compras[2] = "Suco de Laranja"

""" Adicionando um item na lista """

lista_de_compras.append("Café")
print(lista_de_compras[4])

if "Café" in lista_de_compras:
    print("Preciso comprar café")

print( len(lista_de_compras) )

del lista_de_compras[3]
print(lista_de_compras)




















""" 
Faça um programa que inicialize uma lista com o nome das pessoas da sua família.
"""

familia = ["Gabriel", "Anderson", "Luluzinha", "Mariazinha", "Joãozinho"]
print(familia)








"""
Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes de cidades, 
um por vez, cada vez que o usuário digitar um nome, o programa deve incluir este nome na lista de cidades.
"""

cidades = []

cidade = input("Digite o nome da primeira cidade: ")
cidades.append(cidade)

cidades.append(input("Digite o nome da segunda cidade: "))
cidades.append(input("Digite o nome da terceira cidade: "))
print(cidades)


"""
Faça um programa que inicialize uma lista com vários números diferentes, depois disso, 
solicite ao usuário um número, verifique se o número está ou não na lista e 
exiba uma mensagem notificando o usuário do resultado.
"""

numeros = [1,3,6,10,5,23]
numero_digitado = int(input("Digite um número: "))
if numero_digitado in numeros:
    print(f"O número {numero_digitado} está na lista")
else:
    print(f"O número {numero_digitado} não está na lista")


"""
Faça um programa onde o usuário digita 5 nomes diferentes, depois disso solicite um número de 0 até 4 e 
remova o elemento desta posição.
"""

nomes = []
nomes.append(input("Digite o primeiro nome: "))
nomes.append(input("Digite o segundo nome: "))
nomes.append(input("Digite o terceiro nome: "))
nomes.append(input("Digite o quarto nome: "))
nomes.append(input("Digite o quinto nome: "))

posicao_para_excluir = int( input("Escolha uma posição de 0(zero) até quatro para excluir da lista: "))
del nomes[posicao_para_excluir]
print(nomes)
