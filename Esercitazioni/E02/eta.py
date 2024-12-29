from datetime import datetime

compl_str = input("Inserisci il tuo compleanno (gg/mm/aaaa): ")

compl = datetime.strptime(compl_str, '%d/%m/%Y')

timenow = datetime.now()

# Differenza
delta = timenow - compl

years = delta.days // 365
months = (delta.days % 365) // 30
days = (delta.days % 365) % 30

print(f"Il tempo trascorso è: {years} anni, {months} mesi e {days} giorni")
