giorni = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]* int(31/7+1)
giorni = giorni[:32]

numeri = [0]*31
for i in range(1,32):
    numeri[i-1] =i
print("{:-^40}".format(""))
print("{: ^40}".format("Giorni di ottobre:\n"))
for n, g in zip(numeri, giorni[1:]):
    print("{: ^37}".format("{:<9} {:02} ottobre").format(g,n))


print("{:-^40}".format(""))
print("{: ^40}".format("Giorni di ottobre:\n"))
for n, g in zip(numeri, giorni[1:]):
    print("%9s %4.2s %s" %(g,n, "ottobre"))