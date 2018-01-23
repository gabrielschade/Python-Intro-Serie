teste = None
print(teste)

if teste:
    print(teste) # -> não será executado



nome = "gabriel"
nome_maiusculo = nome.capitalize()
print(nome_maiusculo)  # -> Gabriel

nome_com_letra_alterada = nome.replace('e','a') 
print(nome_com_letra_alterada) # -> gabrial

mensagem = "Olá {0}".format(nome_maiusculo)
print(mensagem) # -> Olá Gabriel

segunda_mensagem = "Olá {0}, me chamo {1}".format(nome_maiusculo, "Python")
print(segunda_mensagem) # -> Olá Gabriel, me chamo Python

terceira_mensagem = "Olá {0}, me chamo {1}. {0}".format(nome_maiusculo, "Python")
print(terceira_mensagem) # -> Olá Gabriel, me chamo Python. Gabriel

mensagem = f"Olá {nome_maiusculo}"
print(mensagem) # -> Olá Gabriel

itens_cozinha = "prato,garfo,copo"
print(itens_cozinha.split(",")) # -> ["prato", "garfo", "copo"]

itens = itens_cozinha.split(",")
print(itens[0]) # -> prato
print(itens[1]) # -> garfo
print(itens[2]) # -> copo

#print(itens[3]) # -> erro















































""" Faça um programa que solicite o nome do usuário e depois disso faça uma saudação no formato: 
"Olá {nome digitado pelo usuário} """
nome = input("Digite seu nome: ")
print (f"Olá {nome}")




""" Faça um programa que solicite uma mensagem qualquer para o usuário e 
exiba esta mensagem com todas as letras em maiúsculo."""
mensagem = input ("Digite uma mensagem: ")
print(mensagem.upper())




""" Faça um programa que solicite a idade do usuário, verifique se o texto informado só contém números. 
Caso contenha somente números exiba a mensagem: "Você tem {idade digitada} anos.", 
caso contrário exiba a mensagem: "Você digitou uma idade inválida"."""
idade = input ("Digite sua idade: ")
if idade.isdigit():
    print(f"Você tem {idade} anos.")
else:
    print("Você digitou uma idade inválida")



""" 
Faça um programa que solicite o nome completo do usuário e exiba somente o seu segundo nome/primeiro sobrenome.
"""

nome_completo = input("Digite seu nome completo: ")
nome_completo_dividido = nome_completo.split(" ")
print(nome_completo_dividido[1])