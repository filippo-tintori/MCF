import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(file_path):
    # Legge il file e assegna nomi alle colonne
    data = pd.read_csv(file_path, header=None, names=['module_id', 'sensor_id', 'time'])
    # Converte la colonna 'time' in numerico per evitare errori
    data['time'] = pd.to_numeric(data['time'], errors='coerce')
    return data

# istogramma dei tempi degli Hit 
def plot_time_histogram(data):
    plt.hist(data['time'].dropna(), bins=50, color='blue', alpha=0.7)
    plt.xlabel("Tempo (ns)")
    plt.ylabel("Conteggio degli Hit")
    plt.title("Istogramma dei tempi per il modulo")
    plt.show()

# istogramma delle differenze di tempo fra Hit consecutivi 
def plot_time_diff_histogram(data):
    time_diffs = np.diff(data['time'].dropna().values) 
    plt.hist(time_diffs, bins=50, color='green', alpha=0.7)
    plt.xlabel("Differenze di tempo (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma delle differenze di tempo fra Hit consecutivi")
    plt.show()

if __name__ == "__main__":
    file_path = "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M0.csv"
    
    data = read_data(file_path)

    plot_time_histogram(data)
    plot_time_diff_histogram(data)