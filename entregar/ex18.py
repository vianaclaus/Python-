def encerra():
    print("Você digitou um valor maior que o esperado. Encerrado") 

num = int(input("Insira um valor menor 1000")) 
if num > 1000:
    encerra()
    
elif num>=100:
    centenas = num//100
    resto = num%100
    dezenas = resto//10
    unidades = resto%10
    
    if centenas>1:
        if dezenas>1:
            if unidades>1:                                
                print("{} centenas, {} dezenas e {} unidades.".format(centenas,dezenas,unidades))
                
            elif unidades == 0:               
                print("{} centenas e {} dezenas.".format(centenas,dezenas))   
                
        elif dezenas==0 and unidades==0: 
            print("{} centenas.".format(centenas)) 
            
        elif dezenas==0 and unidades==1:
            print("{} centenas e {} unidade.".format(centenas,unidades))
            
        elif dezenas==0 and unidades>1:            
            print("{} centenas e {} unidades.".format(centenas,unidades))           
                      
        elif dezenas==1 and unidades==1:
            print("{} centenas, {} dezena e {} unidade.".format(centenas,dezenas,unidades))
        elif dezenas==1 and unidades == 0:
            print("{} centenas e {} dezena".format(centenas,dezenas))
            
    elif centenas==1:
        if dezenas == 1 and unidades == 1:
            print("{} centena, {} dezena e {} unidade.".format(centenas,dezenas,unidades) ) 
            
        elif dezenas == 0 and unidades == 1:
            print("{} centena e {} unidade.".format(centenas,unidades))
            
        elif dezenas == 0 and unidades == 0:
            print("{} centena.".format(centenas))
            
        elif dezenas == 1 and unidades == 0:
            print("{} centena e {} dezena.".format(centenas, dezenas))          
            
else:    
    dezenas = num//10
    unidades = num%10    
     
    if dezenas>1 and unidades>1:
        print("{} dezenas e {} unidades.".format(dezenas, unidades))
    elif dezenas == 1 and unidades== 0:                      
        print("{} dezena.".format(dezenas))            
    elif dezenas>1 and unidades == 1:
        print("{} dezenas e {} unidade.".format(dezenas,unidades)) 
    elif dezenas>1 and unidades == 0:
        print("{} dezenas.".format(dezenas))
    elif dezenas == 0 and unidades == 1:
        print("{} unidade.".format(unidades))            
    elif dezenas == 0 and unidades>1:
        print("{} unidades.".format(unidades))          
    elif dezenas == 1 and unidades>1:  
        print("{} dezena e {} unidades.".format(dezenas,unidades))
    elif dezenas == 1 and unidades == 1:
        print("{} dezena e {} unidade.".format(dezenas,unidades))
                    
             


          