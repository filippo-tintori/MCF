
# metodo semplice

# i=100
# somma = 0

# while i>0:
#     somma+=i
#     i-=1
    
# oppure
# i=0
# while i<=100:
#     somma+=i
#     i+=1 

somma = 0
for i in range(1,101):
    somma = somma + i
    

print("La somma dei primi 100 è", somma)

#formula di Gauss

sommaGauss = int(100*(100+1)/2)    #    n(n+1)/2

print("La somma dei primi 100 numeri naturali con la formula di Gauss è", sommaGauss)