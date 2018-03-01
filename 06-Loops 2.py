"""
Lista de dez números
"""

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

"""
Utilizando laço de repetição
"""
posicao = 0
while posicao < len(numeros):
    print(numeros[posicao])
    posicao += 1

"""
Criando um loop infinito
"""
#while True:
#    print("INFINITO")
"""
Utilizando o continue para pular a quinta posição
"""
posicao = 0
while posicao < len(numeros):
    posicao += 1
    if posicao == 5:
        continue
    print(numeros[posicao - 1])
    
"""
Pulando a quinta posição sem o continue
"""
posicao = 0
while posicao < len(numeros):
    posicao += 1
    if posicao != 5:
        print(numeros[posicao - 1]) 
    

"""
Utilizando o break para encerrar na quinta posição
"""
posicao = 0
while posicao < len(numeros):
    posicao += 1
    if posicao == 5:
        break
    print(numeros[posicao - 1])

"""
Alterando a comparação para encerrar na quinta posição sem o break
"""
posicao = 0
while posicao < 5:
    print(numeros[posicao])
    posicao += 1




































"""
Faça um programa que inicialize uma lista de compras com 5 itens diferentes e exiba todos utilizando 
um laço de repetição `while`.
"""

itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
posicao = 0
while posicao < len(itens_compra):
    print(itens_compra[posicao])
    posicao+=1







"""
Faça um programa que inicialize que crie uma lista com os valores de 1 até 10 e 
depois exiba apenas os números pares utilizando `while`.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0
while posicao < len(numeros):
    numero = numeros[posicao]
    if numero % 2 == 0:
        print(numero)
    posicao+=1











"""
Faça um programa que inicialize uma lista vazia, 
solicite ao usuário 10 números ímpares diferentes, um por vez. 

Caso o número digitado seja par, solicite novamente um número, até que o valor seja um número ímpar. 
Depois disso, exiba os 10 números digitados.
"""
numeros = []
numero = 0
quantidade_sobrando = 10
while quantidade_sobrando > 0:
    numero = 0
    while numero % 2 == 0:
        numero = int( input("Digite um número ímpar: ") )

    numeros.append(numero)
    quantidade_sobrando -= 1

posicao = 0
    
while posicao < len(numeros):
    print(numeros[posicao])
    posicao += 1





















"""
Faça um programa que exiba um menu para o usuário selecionar uma das três opções:
 * 1 - Olá mundo
 * 2 - Eu programo em Python
 * 3 - Laços de repetição

O programa deve solicitar ao usuário uma das 3 opções, 
caso o usuário digite um valor diferente das opções (1, 2 ou 3), 
o programa deve apresentar novamente o menu de opções até que uma delas seja escolhida.
Por fim, o programa deve exibir uma mensagem diferente para cada opção.
"""
opcao = 0
opcoes = [1, 2, 3]
while opcao not in opcoes:
    print("Selecione uma das opções abaixo: ")
    print("1 - Olá mundo ")
    print("2 - Eu programo em Python ")
    print("3 - Laços de repetição ")
    opcao = int ( input ("Selecione a opção: ") )

if opcao == 1:
    print("Olá mundo!")
elif opcao == 2:
    print("Já estou na minha sexta lição de Python!")
else:
    print("Nesta lição estou estudando o laço de repetição While")

















