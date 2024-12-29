import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from reco import Hit

# Funzione per leggere un file e creare un array di oggetti Hit
def load_hits_from_file(file_path):
    data = pd.read_csv(file_path, header=None, names=['module_id', 'sensor_id', 'time'])
    hits = [Hit(row['module_id'], row['sensor_id'], row['time']) for _, row in data.iterrows()]
    return hits

# Funzione per combinare e ordinare tutti gli hit
def combine_and_sort_hits(file_paths):
    all_hits = []
    for file_path in file_paths:
        all_hits.extend(load_hits_from_file(file_path))
    # Ordina gli Hit basandosi sui metodi di confronto definiti in Hit
    all_hits.sort()
    return all_hits

# Funzione per calcolare le differenze temporali fra Hit consecutivi e creare un istogramma
def plot_hit_time_diffs(hits):
    timestamps = np.array([hit.timestamp for hit in hits])
    time_diffs = np.diff(timestamps)
    plt.hist(time_diffs, bins=50, color='purple', alpha=0.7)
    plt.xlabel("Differenze di tempo (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma delle differenze di tempo fra Hit consecutivi")
    plt.show()

# Esecuzione dello script
if __name__ == "__main__":
    # Elenco dei file di dati
    file_paths = ["/mnt/data/hit_times_M0.csv", "/mnt/data/hit_times_M1.csv",
                  "/mnt/data/hit_times_M2.csv", "/mnt/data/hit_times_M3.csv"]

    # Carica e combina tutti gli Hit
    hits = combine_and_sort_hits(file_paths)

    # Produce un istogramma delle differenze temporali fra Hit consecutivi
    plot_hit_time_diffs(hits)