"""
Função de soma definida e através de lambda
"""

def soma(numero1, numero2):
    return numero1 + numero2

soma_lambda = lambda numero1, numero2: numero1+numero2

print(soma(1,2))        # -> 3
print(soma_lambda(1,2)) # -> 3

"""
Função lambda sem parâmetro
"""
obter_valor = lambda: 3 + 2
cinco = obter_valor()
print(cinco)

"""
Função lambda sem parâmetro
"""
ola = lambda: print('Olá mundo')
ola()

"""
Filtrando um array
"""
numeros = [0,2,3,4,5,7]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

for par in pares:
    print(par)

"""
Função filter
"""
pares = filter(lambda valor: valor % 2 == 0,numeros)

for par in pares:
    print(par)


























"""
Faça um programa que escreva "Minha primeira função", esta escrita deve ser realizada a partir da chamada de uma 
função que foi declarada como uma expressão lambda.
"""
minha_funcao = lambda:print("Minha primeira função")
minha_funcao()























"""
Faça um programa que solicite o nome do usuário e a idade do usuário, 
depois disso exiba a mensagem: *"{nome} possui {idade} anos."*. 
Esta mensagem deve ser escrita em uma função lambda.
"""
escrever_nome_idade = lambda nome, idade: print(nome, "possui",idade,"anos.")
nome_digitado = str(input("Digite seu nome: "))
idade_digitada = int(input("Digite sua idade: "))
escrever_nome_idade(nome_digitado, idade_digitada)

























"""
Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 
A multiplicação deve ser calculada em uma função lambda.
"""
multiplicar = lambda numero1, numero2: numero1 * numero2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = multiplicar(numero, numero2)
print(resultado)




















"""
Faça um programa que solicite cinco números ao usuário, depois disso, 
exiba apenas os números maiores do que 10. 
Utilize a função `filter` para fazer isso.
"""
numeros = []
for indice in range(1,5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maiores = filter(lambda numero: numero > 10, numeros)
for maior in maiores:
    print(maior)





































"""
Faça um programa que solicite dez números ao usuário, depois disso, exiba todos números pares 
e só então exiba todos os números ímpares. 
Utilize a função `filter` para fazer isso.
"""
def escrever_array(array):
    for valor in array:
        print(valor)

numeros = []
for indice in range(1,10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

pares = filter(lambda numero: numero % 2 == 0, numeros)
impares = filter(lambda numero: numero % 2 == 1, numeros)
escrever_array(pares)
escrever_array(impares)

