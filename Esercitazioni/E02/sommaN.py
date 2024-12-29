max = input("Inserisci il valore N per cui fare la somma dei numeri precedenti: ")

somma = 0
for i in range (1,max+1):
    somma = somma + i
    
print(somma)