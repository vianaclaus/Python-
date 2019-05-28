height = float(input("Qual é a sua altura? "))
gender = input("Se você for homem digite H, se você for mulher, digite M")

if(gender=="M" or gender=="m"):
    ideal_weight = 62.1*height - 44.7
    
elif(gender=="H" or gender=="h"):
    ideal_weight = 72.7*height - 58.00
    
else:
    print("Esse valor não é valido")
    
print("O seu peso ideal é: {}".format(ideal_weight))    