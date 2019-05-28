celsius = float(input("Entre com a temperatura em celsius"))  
fahr = float(input("Entre com a temperatura em fahrenheit"))

fahre = (celsius *1.8)+32  
cels = (fahr-32)/1.8

fahre = round(fahre, 2)
cels = round(cels, 2)
print("Em Fahreinheit essse valor é igual a {}".format(fahre))  
print("Em Celsius esse valor é igual a {}".format(cels))
    