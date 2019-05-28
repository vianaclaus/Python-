import math

def eq_seg_grau(a,b,c): 
    deltacalc = (b*b)-4*a*c 
    sqrt_value = math.sqrt(deltacalc)   
    root1 = (-b + sqrt_value)/2*a
    root2 = (-b - sqrt_value)/2*a
    roots = [root1, root2]
    return roots

def encerrado():
    print("Programa encerrado")

a = int(input("Entre com o valor de a: "))

if(a==0):    
    encerrado()

elif(a!=0):    
    b = int(input("Entre com o valor de b: "))
    c = int(input("Entre com o valor de c: "))
    bsquared = b*b
    four_ac = 4*a*c
    deltacalc = bsquared - four_ac    

    if(deltacalc<0):

        print("Delta: {} Não existem raízes reais para esses valores. Encerrando".format(deltacalc))

    elif(deltacalc==0):        
        list_raizes = eq_seg_grau(a,b,c)
        print("O valor da única raiz é {} ".format(list_raizes[0]))
    else:        
        list_raizes = eq_seg_grau(a,b,c)
        print("O valor da primeira raiz é {} ".format(list_raizes[0]))
        print("O valor da segunda raiz é {} ".format(list_raizes[1]))


             

