valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = int(input("Qual a quantidade de horas trabalhadas no mes?"))

sal_bruto = valor_hora * horas_mes
ir = (sal_bruto*11)/100
inss = (sal_bruto*8)/100
sindicato = (sal_bruto*5)/100
descontos = ir+inss+sindicato
sal_liq = sal_bruto - descontos



print("+ Salário bruto: R$ {}".format(sal_bruto))
print("- IR:            R$ {}".format(ir))
print("- INSS:          R$ {}".format(inss))
print("- Sindicato:     R$ {}".format(sindicato))
print("- Sal. Líquido   R$ {}".format(sal_liq))

