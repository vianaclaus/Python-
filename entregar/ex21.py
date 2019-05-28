litros = float(input("Entre com a quantidade de litros a ser carregado: "))
tipo = input("Digite G para gasolina ou A para alcool: ")

if tipo == "g" or tipo == "G":
    if litros<=20:
        desc_por_litro = (3*2.5)/100
    else:
        desc_por_litro = (5*2.5)/100

    preco_total = (litros*2.5) - (desc_por_litro*litros)

    print("Valor a ser pago: {} ".format(preco_total))

elif tipo == "a" or tipo == "A":
    if litros<=20:
        desc_por_litro = (4*1.9)/100
    else:
        desc_por_litro = (6*1.9)/100

    preco_total = (litros*1.9) - (desc_por_litro*litros)  

    print("Valor a ser pago: {} ".format(preco_total))  
else:
    print("Esse tipo de combustível não está dispocnível") 



      



