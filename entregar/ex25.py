seq = input("Digite 5 numeros separados por virgula: ")

listSeq = seq.split(",")

listSeq = [float(i) for i in listSeq]
greater = max(listSeq)
print(greater)        