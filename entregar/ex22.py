quant_maca = float(input("Insira quantos kg de maçãs vc precisa: "))
quant_morango = float(input("Insira quantos kg de morango vc precisa: "))
kg_total = quant_maca+quant_morango

if quant_maca<=5:
    value_maca = quant_maca*1.8
else:
    value_maca = quant_maca*1.5

if quant_morango<=5:
    value_morango = quant_morango*2.5
else:
    value_morango = quant_morango*2.2

value_total = value_maca+value_morango    
dez_percent = (value_total*10)/100

if kg_total>8 or   value_total>25:
    value_total = value_total - dez_percent

print("O valor total a ser pago eh de {}".format(value_total))    
