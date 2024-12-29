import math


def sommeN(n):
    somma = 0
    for i in range(n):
        somma += i
    return somma


def radiceSommeN(n):
    somma = 0
    for i in range(n):
        somma += math.sqrt(i)
    return somma
