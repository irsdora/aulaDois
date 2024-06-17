
"""
Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela!
"""

print ("Bem vindo ao programa, Squad 4 da Comunidade !")
nome_usuario = str(input("Digita o seu nome: "))
altura = float(input("Digite a sua altura: "))
idade = int (input("Digite a sua idade: "))

print(f" Boa noite, {nome_usuario} ! Você possui {idade} anos e sua altura é {altura} m. Deseja brincar mais?")

nota_um = float(input("Digite a nota um: "))
nota_dois = float(input("Digite a nota dois: "))

total_notas = nota_um + nota_dois
media_total = total_notas/2


print ("A nota final é resulta da soma de duas notas dividido por 2")