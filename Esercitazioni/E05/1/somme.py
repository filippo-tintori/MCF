import math


def sommeN(n):
    somma = 0
    for i in range(1,n+1):
        somma += i
    return somma


def radiceSommeN(n):
    somma = 0
    for i in range(1, n+1):
        somma += math.sqrt(i)
    return somma

def pot(n, a=1):
    somma = 0
    for i in range(1, n+1):
        somma += i**a
    return somma