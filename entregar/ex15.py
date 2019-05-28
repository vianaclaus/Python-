#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
# de um semestre, e calcule a sua média. 

grade1 = float(input("Entre com a primeira nota"))
grade2 = float(input("Entre com a segunda nota"))

average = (grade1+grade2)/2
av = ""
if average>=9.00:
    av = "ENTRE 9.0 E 10.0"
    conceito = "A"
    situation = "APROVADO"
elif average >=7.5:
    av = "ENTRE 7.5 E 9.0"
    conceito = "B"
    situation = "APROVADO"
elif average >= 6.0:
    av = "ENTRE 6.0 E 7.5"
    conceito = "C"
    situation = "APROVADO"
elif average >= 4 and average<= 6.0:
    av = "ENTRE 4.0 E 6"
    conceito = "D"
    situation = "REPROVADO"
elif average <4:
    av = "ENTRE 0.0 E 4.0"
    conceito = "E"
    situation = "REPROVADO"
    
print("Notas: {} e {}".format(grade1, grade2))    
print("Média de Aproveitamento        Conceito") 
print("{}                {}               {}".format(av, conceito, situation))