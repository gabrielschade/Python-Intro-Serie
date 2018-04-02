"""
Definindo a função "Olá mundo"
"""
def ola_mundo():
    print("Olá mundo")

"""
Executando a função "Olá mundo"
""" 
ola_mundo()


"""
Entendendo como funciona a execução de uma função
"""
numero = 10
numero2 = 15
ola_mundo()
resultado = numero + numero2

"""
Elevando um número ao quadrado
"""
def elevar_ao_quadrado(numero):
    print(numero * numero)

elevar_ao_quadrado(9)
elevar_ao_quadrado(4 + 5)
nove = 9
elevar_ao_quadrado(nove)

"""
Função para somar dois números
"""
def soma(numero1, numero2):
    print(numero1 + numero2)

soma(2, 5)
soma(3, 3)
soma(10, 5)

"""
Função trabalhando com textos
"""

def saudacao(nome):
    print("Olá", nome)

"""
Função soma produzindo um resultado
"""
def soma(numero1, numero2):
    return numero1 + numero2

resultado = soma(1,2)
print(resultado) # -> 3
resultado = soma(2,2) * 3
print(resultado) # -> 12
resultado = soma(5,5) - 2 * 5
print(resultado) # -> 0
print(soma(3,7)) # -> 10
"""
Função com um return no meio
"""

def exemplo(valor):
    numero = valor * 2
    if numero > 10:
        return numero

    valor = valor + 5
    return valor

"""
Função de exemplo após ajuste para termos apenas 1 return
"""

def exemplo(valor):
    resultado = None
    numero = valor * 2
    if numero > 10:
        resultado = numero
    else:
        resultado = valor + 5
    
    return resultado

"""
Função de exemplo após ajuste para condição ternária
"""

def exemplo(valor):
    numero = valor * 2
    return numero if numero > 10 else valor + 5




































































"""
Faça um programa que escreva "Minha primeira função", esta escrita deve ser realizada a partir da chamada de uma função.
"""

def minha_funcao():
    print("Minha primeira função")

minha_funcao()


























"""
Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: 
*"{nome} possui {idade} anos."*. Esta mensagem deve ser escrita em uma função.
"""
def escrever_nome_idade(nome, idade):
    print(nome, "possui",idade,"anos.")

nome_digitado = str(input("Digite seu nome: "))
idade_digitada = int(input("Digite sua idade: "))

escrever_nome_idade(nome_digitado, idade_digitada)























"""
Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 
A multiplicação deve ser calculada em uma função.
"""
def multiplicar(numero1, numero2):
    return numero1 * numero2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = multiplicar(numero, numero2)
print(resultado)
























"""
Faça um programa que solicite ao usuário três números diferentes e exiba o dobro do maior número. 
Para fazer issos separe seu código em duas funções diferentes: 
Uma função para retornar o maior dos três números e 
outra função para dobrar o número.
"""

def obter_maior(numero, numero2, numero3):
    maior = None
    if numero > numero2 and numero > numero3:
        maior = numero
    elif numero2 > numero and numero2 > numero3:
        maior = numero2
    else:
        maior = numero3
    return maior


def dobrar(numero):
    return numero * 2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = obter_maior(numero,numero2,numero3)
print(dobrar(maior))


























"""
Faça um programa que inicialize uma lista vazia, depois disso 
solicite 5 nomes diferentes ao usuário (utilize laço de repetição). 
Cada nome digitado deve ser adicionado à lista e por fim, todos os nomes devem ser escritos no console. 
Utilize uma função para solicitar e retornar o nome digitado, 
uma função para adicionar o nome à lista (passando o nome e a lista por parâmetro) e 
outra função para escrever todos os nomes no console.
"""
def solicitar_nome():
    return str ( input("Digite um nome: ") )

def adicionar_nome_na_lista(lista, nome):
    lista.append(nome)

def escrever_nomes(lista):
    for nome in lista:
        print(nome)

nomes = []
for contador in range(0,5):
    nome = solicitar_nome()
    adicionar_nome_na_lista(nomes, nome)

escrever_nomes(nomes)