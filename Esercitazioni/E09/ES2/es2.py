#date_old	date	mean_co_ug/m3	mean_nh3_ug/m3	mean_no2_ug/m3	mean_o3_ug/m3	mean_pm10_ug/m3	mean_pm2p5_ug/m3	mean_so2_ug/m3

# Ammoniaca,       Diossido di azoto ,       Ozono,       PM10,        PM2.5,          Anidride solforosa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import matplotlib.dates as mdates
from datetime import datetime

dati = pd.read_csv("/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E09/ES2/copernicus_PG_selected.csv")

tempo = dati["date"].values - 58000
CO = dati["mean_co_ug/m3"].values

print(dati.head())

# 3. 
time_days = dati['date'].values
start_date = datetime(1858, 11, 16)
date = [start_date + pd.Timedelta(days=int(day)) for day in time_days]

# 4.
plt.figure(figsize=(7, 5))
plt.plot(date, CO, label='Concentrazione CO')
plt.xlabel('Tempo')
plt.ylabel('Concentrazione CO')
plt.title('Concentrazione di CO in funzione del tempo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 5.
N = len(CO)
freq = np.fft.fftfreq(N, d=1)
fourier = fft(CO)

# 6. 
spettro = np.abs(fourier)**2

plt.figure(figsize=(7, 5))
plt.plot(freq[:N//2], spettro[:N//2]) 
plt.xlabel('Frequenza (1/giorno)')
plt.ylabel('Spettro di potenza')
plt.title('Spettro di potenza della CO')
plt.grid(True)
plt.show()

# 7.
periods = 1 / freq

plt.figure(figsize=(7, 5))
plt.plot(periods[:N//2], spettro[:N//2])
plt.xlabel('Periodo (giorni)')
plt.ylabel('Spettro di potenza')
plt.title('Spettro di potenza della CO in funzione del periodo')
plt.grid(True)
plt.show()

# 8. 
sogliaFreq = 0.1 # carino anche 0.01, arrotonda molto di più
mask_fourier = fourier.copy()
mask_fourier[np.abs(freq) > sogliaFreq] = 0  

# 9. 
mask_signal = np.real(ifft(mask_fourier))

# segnale originale - segnale filtrato
plt.figure(figsize=(7, 5))
plt.plot(date, CO, label='Segnale originale', alpha=0.7)
plt.plot(date, mask_signal, label='Segnale filtratro', linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Concentrazione CO')
plt.title('Confronto tra segnale originale e segnale filtrato')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()