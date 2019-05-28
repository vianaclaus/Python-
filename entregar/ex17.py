year = int(input("Digite um ano e diremos se ele foi bissexto"))

if year%4==0 and year%100!=0:
    print("Você digitou um ano bissexto")
else:

    print("Você não digitou um ano bissexto")    