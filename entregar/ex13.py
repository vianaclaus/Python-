salary = float(input("Type the salary: "))
salary_inc = 0

if salary<=280.00:
    salary_inc = (salary*20)/100    
    print("Salario antes do reajuste: {}".format(salary))
    print("Percentual de aumento aplicado: 20%")
    print("Valor do aumento: {} ".format(salary_inc))
    print("Novo salário: {}".format(salary+salary_inc))    
elif salary > 280 and salary <= 700:
    salary_inc =(salary*15)/100   
    print("Salario antes do reajuste: {}".format(salary))
    print("Percentual de aumento aplicado: 15%")
    print("Valor do aumento: {} ".format(salary_inc))
    print("Novo salário: {}".format(salary+salary_inc))
elif salary > 700 and salary <= 1500:
    salary_inc = (salary*10)/100    
    print("Salario antes do reajuste: {}".format(salary))
    print("Percentual de aumento aplicado: 10%")
    print("Valor do aumento: {} ".format(salary_inc))
    print("Novo salário: {}".format(salary+salary_inc))
else:
    salary_inc = (salary*5)/100   
    print("Salario antes do reajuste: {}".format(salary))
    print("Percentual de aumento aplicado: 5%")
    print("Valor do aumento: {} ".format(salary_inc))
    print("Novo salário: {}".format(salary+salary_inc))