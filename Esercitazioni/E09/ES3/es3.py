# Date(UTC)	        Julian Date        	TS	           Photon Flux [0.1-100 GeV](photons cm-2 s-1)	            Photon Flux Error(photons cm-2 s-1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.optimize import curve_fit

sources = {
    "4FGL_J2202.7+4216": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2202.7%2B4216_weekly_9_15_2023_mcf.csv", "class": "BLL"},
    "4FGL_J0721.9+7120": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J0721.9%2B7120_weekly_9_15_2023_mcf.csv", "class": "BLL"},
    "4FGL_J0428.6-3756": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv", "class": "BLL"},
    "4FGL_J1256.1-0547": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv", "class": "FSRQ"},
    "4FGL_J2253.9+1609": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2253.9%2B1609_weekly_9_15_2023_mcf.csv", "class": "FSRQ"},
    "4FGL_J2232.6+1143": {"url": "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2232.6%2B1143_weekly_9_15_2023_mcf.csv", "class": "FSRQ"},
}

colors = {"BLL": "blue", "FSRQ": "red"}

dataframes = {}
for name, info in sources.items():
    dataframes[name] = pd.read_csv(info["url"])
    dataframes[name]["class"] = info["class"]


plt.figure(figsize=(10, 6))
for name, df in dataframes.items():
    plt.plot(df["Julian Date"], df["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"], label=name, color=colors[df["class"][0]])
plt.xlabel("Julian Date")
plt.ylabel("Photon Flux [photons cm$^{-2}$ s$^{-1}$]")
plt.title("Curves of Light - All Sources")
plt.legend()
plt.show()

fig, axes = plt.subplots(6, 1, figsize=(10, 14), sharex=True)
for ax, (name, df) in zip(axes, dataframes.items()):
    ax.plot(df["Julian Date"], df["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"], color=colors[df["class"][0]])
    ax.set_title(name)
    ax.set_ylabel("Photon Flux")
plt.xlabel("Julian Date")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(6, 1, figsize=(10, 14), sharex=True)
freq_data = {}
for ax, (name, df) in zip(axes, dataframes.items()):
    flux = df["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].fillna(0)
    fft_result = fft(flux)
    power = np.abs(fft_result)**2
    freq = fftfreq(len(flux), d=1)
    freq_data[name] = (freq, power)
    ax.plot(freq[:len(freq)//2], power[:len(freq)//2], label=name, color=colors[df["class"][0]])
    ax.set_title(name)
    ax.set_ylabel("Power Spectrum")
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()

# soettri 
plt.figure(figsize=(10, 6))
for name, (freq, power) in freq_data.items():
    plt.plot(freq[:len(freq)//2], power[:len(freq)//2], label=name, color=colors[dataframes[name]["class"][0]])
plt.xlabel("Frequency")
plt.ylabel("Power Spectrum")
plt.title("Power Spectra - All Sources")
plt.legend()
plt.show()

# spettro normalizzato
plt.figure(figsize=(10, 6))
for name, (freq, power) in freq_data.items():
    norm_power = power / power[0]
    plt.plot(freq[:len(freq)//2], norm_power[:len(freq)//2], label=name, color=colors[dataframes[name]["class"][0]])
plt.xlabel("Frequency")
plt.ylabel("Normalized Power Spectrum")
plt.title("Normalized Power Spectra - All Sources")
plt.legend()
plt.show()