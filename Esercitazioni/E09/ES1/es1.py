import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.optimize import curve_fit

# funzione per il fit k / f^beta
def funz(f, beta, k):
    return k / f**beta

# leggi i file csv
data1 = pd.read_csv("/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/ES1/data_sample1.csv")
data2 = pd.read_csv("/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/ES1/data_sample2.csv")
data3 = pd.read_csv("/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/ES1/data_sample3.csv")

# estrai i segnali e il tempo
time1, sig1 = data1['time'], data1['meas']
time2, sig2 = data2['time'], data2['meas']
time3, sig3 = data3['time'], data3['meas']

# calcola la trasformata di fourier
def compute_fft(time, sig):
    dt = np.mean(np.diff(time))  
    n = len(sig)  
    freq = np.fft.fftfreq(n, d=dt)  
    fft_values = np.abs(fft(sig))**2  
    return freq[:n // 2], fft_values[:n // 2]

# calcola spettri di potenza
freq1, pot1 = compute_fft(time1, sig1)
freq2, pot2 = compute_fft(time2, sig2)
freq3, pot3 = compute_fft(time3, sig3)

# definisci range di frequenze per il fit
freq_min = 1e-2

# applica la maschera per il range delle frequenze
mask1 = (freq1 > freq_min) 
mask2 = (freq2 > freq_min)
mask3 = (freq3 > freq_min)

freq1_fit, pot1_fit = freq1[mask1], pot1[mask1]
freq2_fit, pot2_fit = freq2[mask2], pot2[mask2]
freq3_fit, pot3_fit = freq3[mask3], pot3[mask3]

# fit degli spettri di potenza
popt1, _ = curve_fit(funz, freq1_fit, pot1_fit)
popt2, _ = curve_fit(funz, freq2_fit, pot2_fit)
popt3, _ = curve_fit(funz, freq3_fit, pot3_fit)

# plot dei segnali
plt.figure()
plt.plot(time1, sig1, label='Segnale 1')
plt.plot(time2, sig2, label='Segnale 2')
plt.plot(time3, sig3, label='Segnale 3')
plt.title("Segnali di ingresso")
plt.xlabel("tempo")
plt.ylabel("meas")
plt.legend()
plt.show()

# plot degli spettri di potenza
plt.figure()
plt.loglog(freq1, pot1, label="Spettro 1")
plt.loglog(freq2, pot2, label="Spettro 2")
plt.loglog(freq3, pot3, label="Spettro 3")
plt.title("Spettro di potenza")
plt.xlabel("frequenza")
plt.ylabel("potenza")
plt.legend()
plt.show()

# plot dei fit
plt.figure()
plt.loglog(freq1_fit, funz(freq1_fit, *popt1), label=f"Fit spettro 1, beta={popt1[0]:.2f}")
plt.loglog(freq2_fit, funz(freq2_fit, *popt2), label=f"Fit spettro 2, beta={popt2[0]:.2f}")
plt.loglog(freq3_fit, funz(freq3_fit, *popt3), label=f"Fit spettro 3, beta={popt3[0]:.2f}")
plt.title("Fit degli spettri di potenza")
plt.xlabel("frequenza")
plt.ylabel("potenza")
plt.legend()
plt.show()

# confronto fit e spettri
plt.figure()
plt.loglog(freq1, pot1, label="spettro 1")
plt.loglog(freq1_fit, funz(freq1_fit, *popt1), label=f"fit spettro 1, beta={popt1[0]:.2f}")
plt.title("Confronto spettro 1 e fit")
plt.xlabel("frequenza")
plt.ylabel("potenza")
plt.legend()
plt.show()

plt.figure()
plt.loglog(freq2, pot2, label="spettro 2")
plt.loglog(freq2_fit, funz(freq2_fit, *popt2), label=f"fit spettro 2, beta={popt2[0]:.2f}")
plt.title("Confronto spettro 2 e fit")
plt.xlabel("frequenza")
plt.ylabel("potenza")
plt.legend()
plt.show()

plt.figure()
plt.loglog(freq3, pot3, label="spettro 3")
plt.loglog(freq3_fit, funz(freq3_fit, *popt3), label=f"fit spettro 3, beta={popt3[0]:.2f}")
plt.title("Confronto spettro 3 e fit")
plt.xlabel("frequenza")
plt.ylabel("potenza")
plt.legend()
plt.show()

# Crea il grafico per visualizzare il rapporto tra frequenza e potenza su scala logaritmica
plt.figure()
plt.scatter(freq1_fit, pot1_fit, s=10, label="Spettro 1")
plt.scatter(freq2_fit, pot2_fit, s=10, label="Spettro 2")
plt.scatter(freq3_fit, pot3_fit, s=10, label="Spettro 3")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Frequenza [1/yr]")
plt.ylabel("|c_k|²")
plt.title("Spettro di potenza")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()

def identifica(i):
    if i == 0:
        return "rumore bianco"
    if i==1:
        return "rumore rosa"
    if i==2:
        return "rumore browniano"
    if i==3:
        return "rumore blu"
    return "rumore non identificato"
    
print("Primo spettro indentifica un",identifica(round(popt1[0], 0)))
print("Secondo spettro indentifica un",identifica(round(popt2[0], 0)))
print("Terzo spettro indentifica un",identifica(round(popt3[0], 0)))
