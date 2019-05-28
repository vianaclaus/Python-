grade1 = float(input("Digite a primeira nota"))
grade2 = float(input("Digite a segunda nota"))

average = (grade1+grade2)/2.00

if average == 10.00:
    print("Aprovado com distinção")
elif average >= 7.00:
    print("Aprovado")
else:
    print("Reprovado")
    
    
