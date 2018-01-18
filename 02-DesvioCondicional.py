leite_em_estoque = True

if leite_em_estoque:
    print("Comprei leite")
else:
    print("Comprei água")


"""Crie uma variável numérica para representar uma nota de uma prova, 
depois disso exiba a mensagem "Aprovado" **caso** a nota seja maior ou igual à 7, 
caso contrário exiba a mensagem "Reprovado"."""
nota = 5

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")


"""TRUTHY VALUE PARA O TIPO INTEIRO"""
valor = 4

if valor != 0: # -> não é necessário fazer desta forma
    print("Valor não é zero")

if valor:
    print("Valor não é zero")

"""TRUTHY VALUE PARA O TIPO STRING"""
texto = "teste"

if texto != "": # -> não é necessário fazer desta forma
    print("Texto não está vazio")

if texto:
    print("Texto não está vazio")

"""DESVIOS COM OPERADORES"""
nota1 = 7
nota2 = 10

if nota1 > 5 and nota2 >= 7:
    print("Aprovado")

deu_sol = True

if not deu_sol:
    print("Choveu")


"""NÃO TERNÁRIO"""
nota = 6
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

"""TERNÁRIO"""
print( "Aprovado" if nota >= 7 else "Reprovado")









"""Faça um algoritmo que solicite 3 notas para o usuário, 
calcule a média e indique se o aluno foi aprovado ou reprovado 
(nota precisar ser maior ou igual à sete para o aluno ser aprovado)"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = ( nota1 + nota2 + nota3 ) / 3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

"""Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, 
faça o programa descrever se o usuário fará ou já fez 18 anos neste ano."""

ano_nascimento = int (input ("Digite o ano que você nasceu: "))
idade = 2018 - ano_nascimento

if idade == 18:
    print("O usuário fará ou vez 18 anos este ano.")

""" Faça um programa que solicite ao usuário 2 valores, 
utilize uma condição ternária para escrever qual o maior valor: o primeiro ou o segundo. """

primeiro_valor = int( input("Digite um valor: "))
segundo_valor = int( input("Digite um valor: "))
print( "Primeiro" if primeiro_valor > segundo_valor else "Segundo")