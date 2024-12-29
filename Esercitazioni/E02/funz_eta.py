import math
from  datetime import datetime, timedelta

def RichiediCompleanno():
    compl = input("Inserisci il tuo compleanno (gg-mm-aaaa): ")
    compl = datetime.strptime(compl, "%d-%m-%Y")
    return compl

def Scelta(compl):
    scelta = {}
    str = input("Inserisci la tua scelta (int): ")

def funzione():
    adesso = datetime.now()
    compl = richiedi_eta()
    
    diff.day = adesso.day - compl.day
    
    diff.month = adesso.month - compl.month
    
    diff.year = adesso.year - compl.year
    
    if adesso.month < compl.month:
        diff.year = diff.year - 1
    if adesso.month == compl.month:
        if adesso.day < compl.day:
            diff.month = diff.month - 1


    #aggiuta giorni degli anni bisestile
    diff.day = diff.day + diff.year//4
    
    if diff.day > 30:
        diff.day -=30
        diff.month +=1

def secondi(diff):
    return diff.total_seconds()

def giorni(diff):
    return diff.days

def secoli(diff):
    return secondi(diff) / (100*365 + 100/4)


compl = RichiediCompleanno()
if __name__ == "__main__":
    Scelta(compl)