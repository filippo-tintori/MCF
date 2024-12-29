import numpy as np
import pandas as pd
import time
import math
import scipy as sc
import matplotlib.pyplot as plt
import os

url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"


data = pd.read_csv(url)
"""
print("Valori del CSV:\n")
print(data)

print("Le colonne del CSV sono:\n",data.columns)

plt.plot(data["TIME"], data["PDCSAP_FLUX"] )
plt.xlabel("TIME")
plt.ylabel("Flusso")
plt.show()

plt.plot(data["TIME"], data["PDCSAP_FLUX"], "o" )
plt.show()

plt.errorbar(data["TIME"], data["PDCSAP_FLUX"], yerr = data["PDCSAP_FLUX_ERR"] )
#####plt.savefig(os.path.join(os.path.abspath(__file__), "\Sub GraficoErrori.pdf"))
#plt.savefig("/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/Esercitazione3/GraficoErrori.pdf")
plt.show()
"""

ind = data["PDCSAP_FLUX"].idxmin()
print("Indice del valore minimo:", ind)

t = data["TIME"][ind]
print("Tempo correlato al valore minimo dell'indice", t)

dataNuova = data.loc[(data["TIME"] > t - 2) & (data["TIME"] < t + 2)] 

plt.plot( dataNuova["TIME"], dataNuova["PDCSAP_FLUX"] )
plt.xlabel("TIME")
plt.ylabel("Flusso")
plt.show()


fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(data["TIME"], data["PDCSAP_FLUX"], yerr = data["PDCSAP_FLUX_ERR"])
plt.show()
ins_ax = ax.inset_axes([dataNuova["TIME"], dataNuova["PDCSAP_FLUX"]]) 
ins_ax.errorbar( yerr= dataNuova["PDCSAP_FLUX_ERR"])
plt.show()