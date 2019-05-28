class Conversao:
    
    def convCtoF(self, celsius):        
    
        fahre = (celsius *1.8)+32        
        return fahre
    
    def convFtoC(self, fahr):
        
        cels = (fahr-32)/1.8
        return cels
    
    
celsius = [50.0, 78.9, 3, 89.6, 23.1, 67.5]     
conv = Conversao()
print(list(map(conv.convCtoF, celsius)))

fahr = [23,67,28,12]
print(list(map(conv.convFtoC, fahr)))