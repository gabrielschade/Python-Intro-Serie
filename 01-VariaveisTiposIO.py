"""
Faça um algoritmo para resolver a equação z = x + y - 4, 
armazenando o resultado na variável z. 
Considere que os valores iniciais de x e y são, 
respectivamente, 10 e 5. Depois disso exiba o resultado.
"""
x = 10
y = 5
z = x + y - 4
print(z)

"""
Faça um algoritmo para resolver a equação z = a * a - b + c, 
armazenando o resultado na variável z.
Considere que os valores iniciais de a, b e c são, 
respecitvamente, 4, 6 e 10. Depois disso exiba o resultado.
"""

a = 4
b = 6.5
c = 10.5
z = a * a - b + c
print(z)












"""################### EXEMPLOS DESCRITOS NO ARTIGO ###################"""
nome = input("Qual seu nome? ")
print(nome)

verdade = True
mentira = False

sol_pela_manha   = True
chuva_pela_tarde = False

sol = not sol_pela_manha     # -> False
chuva = not chuva_pela_tarde # -> True

sol_e_chuva = sol_pela_manha and chuva_pela_tarde         # -> False
sol_e_nao_chuva = sol_pela_manha and not chuva_pela_tarde # -> True

sol_ou_chuva = sol_pela_manha or chuva_pela_tarde         # -> True
sol_ou_nao_chuva = sol_pela_manha or not chuva_pela_tarde # -> True
nao_sol_ou_chuva = not sol_pela_manha or chuva_pela_tarde # -> False


cinco_maior_que_tres = 5 > 3 # -> True




"""################### EXERCíCIOS FINAIS ###################"""
""" Faça um algoritmo que solicite o nome do usuário e depois escreva o nome da pessoa no console. """
nome = input("Qual seu nome? ")
print(nome)

""" Faça um algoritmo que pergunte ao usuário quantos anos ele tem, depois disso, escreva `True` no console, 
caso ele já tenha alcançado a maioridade (18 anos), caso contrário escreva `False`."""
idade = int( input("Quantos anos você tem? ") )
maioridade = idade >= 18
print(maioridade)

""" Faça um algoritmo que solicite um número ao usuário, depois disso, escreva `True` no console, 
caso o número tenha dois dígitos (Esteja entre 10 e 99), caso contrário escreva `False`"""
numero = int( input("Digite um numero: ") )
dois_digitos = numero >= 10 and numero <= 99
print(dois_digitos)