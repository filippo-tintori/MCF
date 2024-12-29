import numpy as np
import pandas as pd
#from scipy import constants, fftpack
from scipy import constants, fft
import matplotlib.pyplot as plt

URL= ["/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/data_sample1.csv",
      "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/data_sample2.csv",
      "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/data_sample3.csv"]

def leggiCSV(file):
    df = pd.read_csv(file)
    # colonne time , meas
    return df

dfTot = []
for x in URL:
    dfTot.append(leggiCSV(x))

for x in dfTot:
    plt.plot(x["time"], x["meas"], label="Dati con rumore", color="coral")
    plt.xlabel("time")
    plt.ylabel("meas")
    plt.legend()
    plt.show()

four = []
for x in dfTot:
    four.append(fft.rfft(x['meas'].values))

for x in four:
    plt.plot(np.absolute(x[:x.size//2])**2, 'o', markersize=4)
    plt.xlabel('Indice')
    plt.ylabel(r'$|c_k|^2$')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

