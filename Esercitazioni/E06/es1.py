import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import argparse


file_path = "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E06/vel_vs_time.csv"
data = pd.read_csv(file_path)

time = data["t"].values
vel = data["v"].values

# velcoità in funzione del tempo
plt.plot(time, vel, color="royalblue", label="Dati")
plt.xlabel("t")
plt.ylabel("v")
plt.legend(loc="best")
plt.show()

integrale = integrate.simpson(vel, x=time)
print(integrale)

x = []
for i in range(1,len(vel)-1):
    x.append(integrate.simpson(vel[:i+1], dx=time[i+1]- time[i]))

plt.plot(time[1:-1], x, color="royalblue", label="Dati")
plt.xlabel("t")
plt.ylabel("x")
plt.legend(loc="best")
plt.show()