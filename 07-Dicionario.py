"""
Declarando um dicionário
"""
pessoa = {
    "nome": "Gabriel",
    "sobrenome": "Schade",
    "idade": 27
}

"""
Alterando um valor de um dicionário
"""
pessoa["sobrenome"] = "Schade Cardoso"

"""
Obtendo o valor de um dicionário
"""
nome_da_pessoa = pessoa["nome"]


"""
Imprimindo o nome completo
"""
print( pessoa["nome"], pessoa["sobrenome"] )

"""
Erro por chave inválida
"""
#cpf = pessoa["cpf"]

"""
Obtendo uma valor de forma segura
"""

cpf = pessoa.get("cpf", None)
print (cpf)


"""
Obtendo todas as chaves de um dicionário
"""
chaves = pessoa.keys()
for chave in chaves:
    print (chave)

"""
Obtendo todos os valores de um dicionário
"""
valores = pessoa.values()
for valor in valores:
    print (valor)

"""
Obtendo todas as chaves e valores de um dicionário
"""
chaves = pessoa.keys()
for chave in chaves:
    valor = pessoa[chave]
    texto = chave + ": " + str(valor)
    print ( texto )

"""
Obtendo todas as chaves e valores de um dicionário em uma linha
"""
chaves = pessoa.keys()
for chave in chaves:
    print (  chave, ":", str( pessoa[chave]) )

"""
Apagando um item chave-valor do dicionário
"""

del pessoa["sobrenome"]
#print (pessoa["sobrenome"])































"""
Faça um programa que crie um dicionário para definir um produto, contendo sua descrição e seu preço.
"""
produto = {
    "descrição": "Água",
    "preço": 2.00
}





























"""
Faça um programa que inicialize uma lista de compras com 5 itens diferentes, 
onde cada item é um dicionário contendo a descrição e preço do produto. 
Depois disso, percorra a lista e exiba as informações de cada item.
"""

lista_compras = [
    {"descrição": "Água", "preço": 2.00},
    {"descrição": "Leite", "preço": 3.00},
    {"descrição": "Carne", "preço": 18.00},
    {"descrição": "Pizza", "preço": 9.00},
    {"descrição": "Chocolate", "preço": 6.50},
]

for item_compra in lista_compras:
    print("Produto:", item_compra["descrição"], "por", str(item_compra["preço"]), "reais.")




"""
Utilize a lista de compras do programa anterior para identificar qual o produto mais barato e 
qual o produto mais caro da lista de compras.
"""

mais_barato = None
mais_caro = None
indice = 0
while indice < len(lista_compras):
    item_compra = lista_compras[indice]
    if indice == 0:
        mais_caro = item_compra
        mais_barato = item_compra
    else:
        if item_compra["preço"] > mais_caro["preço"]:
            mais_caro = item_compra

        if item_compra["preço"] < mais_barato["preço"]:
            mais_barato = item_compra

    indice = indice + 1

print("Produto mais caro: ", mais_caro["descrição"], "por", mais_caro["preço"],"reais")
print("Produto mais barato: ", mais_barato["descrição"], "por", mais_barato["preço"],"reais")





















"""
Faça um programa que tenha uma lista com 5 de pessoas, onde cada pessoa tem seu nome e sobrenome 
armazenado em um dicionário, depois disso, exiba todos os nomes e sobrenomes. 
Para complicar um pouco as coisas, vamos simular que estes dados foram obtidos da web e com isso 
recebemos algumas inconsistências.
Duas das cinco pessoas possuem o dicionário onde as chaves estão em maiúsculo e 
os outros três em minúsculo.
"""

pessoas = [
    {"nome": "Joãozinho", "sobrenome": "da Silva" },
    {"NOME": "Mariazinha", "SOBRENOME": "de Souza" }, 
    {"nome": "Gabriel", "sobrenome": "Schade" },
    {"NOME": "Joana", "SOBRENOME": "da Silva" },
    {"nome": "Everton", "sobrenome": "Schmit" },
]

for pessoa in pessoas:
    nome = pessoa.get("nome", None)
    sobrenome = pessoa.get("sobrenome", None)
    if not nome:
        nome = pessoa.get("NOME", None)
    if not sobrenome:
        sobrenome = pessoa.get("SOBRENOME", None)

    print(nome, sobrenome)
