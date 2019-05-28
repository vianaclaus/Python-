seq = input("Digite 5 numeros separados por virgula: ")
listSeq = seq.split(",")
listSeq = [float(i) for i in listSeq]
size = len(listSeq)

if size>5 or size<5:

    print("é indicado que você digite 5 numeros")

else: 
    sum = 0
    for i in listSeq:
        sum += i
    average = sum/5
    print("A soma dos numeros digitados eh {} e a média é:  {}".format(sum, average))

