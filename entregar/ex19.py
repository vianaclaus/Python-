sacar = int(input("Que valor você deseja sacar?"))

if sacar<=600 and sacar>=10:
    cem = sacar//100 
    resto_dos_cem = sacar%100
    cinq = resto_dos_cem//50
    resto_dos_cinq = resto_dos_cem%50
    dez = resto_dos_cinq//10
    resto_dos_dez = resto_dos_cinq%10
    cinco= resto_dos_dez//5
    resto_dos_cinco = resto_dos_dez%5

    print("{} notas de cem, {} notas de cinquenta, {} notas de dez, {} notas de cinco {} notas de um".format(cem, cinq, dez, cinco, resto_dos_cinco))
else:
    print("Por favor, digite um valor entre 10 e 600")