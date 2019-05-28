import math


area_pintar = float(input("Digite, o valor em metros quadrados a ser pintado. "))
litros_necessarios = area_pintar/6

resto_latas = math.ceil(litros_necessarios%18)
resto_galoes = math.ceil(litros_necessarios%3.6)

galoes = math.ceil(litros_necessarios/3.6)
latas = math.ceil(litros_necessarios/18)

add_lata = latas
add_galao = 0

preco_latas = latas*80.0
preco_galao = galoes*25
preco_mix = preco_latas

preco_so_lata = math.ceil(preco_latas)
preco_so_galao = math.ceil(preco_galao)
quant_so_latas = math.ceil(litros_necessarios/18)
quant_so_galao = math.ceil(litros_necessarios/3.6)

if(resto_latas>10.8): 
    
    add_lata+=1
    preco_mix += 80
    
    print("É necessário comprar {}L de tinta".format(litros_necessarios))
    print("Comprando apenas latas de 18L cada, você vai usar {} latas e gastar R${}".format(quant_so_latas, preco_so_lata))
    print("Comprando apenas galões de 3,6L cada, você vai usar {} galões e gastar R${}".format(quant_so_galao, preco_so_galao))
    print("No seu caso não é indicado comprar galões misturados com latas")

elif(resto_latas<=10.8): 
    
    if(resto_latas<3.6): 
        
        add_galao += 1
        preco_mix += 25
        print("É necessário comprar {}L de tinta".format(litros_necessarios))
        print("Comprando apenas latas de 18L cada, você vai usar {} latas e gastar R${}".format(quant_so_latas, preco_so_lata))
        print("Comprando apenas galões de 3,6L cada, você vai usar {} galões e gastar R${}".format(quant_so_galao, preco_so_galao))
        print("Comprando {} latas e {} galão você paga o valor de R$ {}".format(add_lata, add_galao, preco_mix))
    
    elif(resto_latas<=7.2 and resto_latas>3.6):
        
        add_galao += 2
        preco_mix += 50
        
        print("É necessário comprar {}L de tinta".format(litros_necessarios))
        print("Comprando apenas latas de 18L cada, você vai usar {} latas e gastar R${}".format(quant_so_latas, preco_so_lata))
        print("Comprando apenas galões de 3,6L cada, você vai usar {} galões e gastar R${}".format(quant_so_galao, preco_so_galao))
        print("Comprando {} latas e {} galões você paga o valor de R$ {}".format(add_lata, add_galao, preco_mix))
    
    elif(resto_latas<=10.8 and resto_latas>7.2):
        
        add_galao += 3
        preco_mix += 75
        print("É necessário comprar {}L de tinta".format(litros_necessarios))
        print("Comprando apenas latas de 18L cada, você vai usar {} latas e gastar R${}".format(quant_so_latas, preco_so_lata))
        print("Comprando apenas galões de 3,6L cada, você vai usar {} galões e gastar R${}".format(quant_so_galao, preco_so_galao))
        print("Comprando {} latas e {} galão você paga o valor de R$ {}".format(add_lata, add_galao, preco_mix))
    


