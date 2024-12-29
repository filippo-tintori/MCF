import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import csv
import argparse

def Vin(t):
    return 1 if int(t)%2==0 else -1

def dVout_dt(Vout, t, rc):
    return (Vin(t) - Vout) / rc

t = np.linspace(0, 10, 1000) 

Vout_0 = 0

# Valori di RC
RC = [4, 1, 0.25]

results = []

for ReCo in RC:
    Vout = odeint(dVout_dt, Vout_0, t, args=(ReCo,))
    Vout = Vout.flatten()  # array 1D
    results.append((ReCo, t, Vout))

URL = "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E08/ScritturaFile/result.csv"
with open(URL, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['t', 'RC', 'Vin', 'Vout'])
    for rc, t_values, Vout_values in results:
        for i in range(len(t_values)):
            writer.writerow([t_values[i], rc, Vin(t_values[i]), Vout_values[i]])

plt.figure()
for rc, t_values, Vout_values in results:
    plt.plot(t_values, Vout_values, label=rf"$V_OUT$ (RC={rc})")

VinVal = [Vin(ti) for ti in t]
plt.plot(t, VinVal, label=r'$V_{in}$', linestyle='--', color='black')

plt.title(r'Risultati di $V_{out}(t)$ per diversi valori di RC')
plt.xlabel('Tempo (t)')
plt.ylabel('Segnali')
plt.legend()
plt.grid()
plt.show()