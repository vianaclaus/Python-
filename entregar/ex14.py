#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

number_week = int(input("Entre com um numero correspondente a um dia da semana"))

if number_week == 1:
    print("Domingo")
elif number_week == 2:
    print("Segunda")
elif number_week == 3:
    print("Terça")
elif number_week == 4:
    print("Quarta")
elif number_week == 5:
    print("Quinta")
elif number_week == 6:
    print("Sexta")
elif number_week == 7:
    print("Sabado")
else:
    print("Valor inválido")
    