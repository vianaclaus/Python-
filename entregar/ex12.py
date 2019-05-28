num1 = int(input("Type the value a"))
num2 = int(input("Type the value b"))
num3 = int(input("Type the value c"))


if(num1==num2):
    if(num1>num3):
        print("Os maiores numeros são {} e {}".format(num1, num2))
    else:
        print("{} eh o maior valor".format(num3))
        
elif(num1==num3):
    if num1>num2:
        print("Os maiores numeros são {} e {}".format(num1, num3))
    else:
        print("{} eh o maior valor")
        
elif(num2==num3):
    if num2>num1:
        print("Os maiores numeros são {} e {}".format(num2, num3))
    else:
        print("{} é o maior valor".format(num1))
        
elif(num1>num2):
    if(num1>num3):
        print("{} é o maior valor".format(num1))
    elif(num3>num1):
        print("{} é o maior valor".format(num3))
        
elif(num2>num1):
    if(num2>num3):
        print("{} é o maior valor".format(num2))
    if(num3>num2):
        print("{} é o maior valor".format(num3))

