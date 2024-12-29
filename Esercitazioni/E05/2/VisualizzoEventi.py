import matplotlib.pyplot as plt
import reco
import numpy as np
from AnalizzoHit import process_data, create_events 


file_paths = [
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M0.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M1.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M2.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M3.csv"
]

# lista di eventi
hits = process_data(file_paths)
events = create_events(hits, window=500)  # finestra temporale di 500 ns per separare gli eventi

# visualizzare graficamente i primi 10 eventi con informazione temporale basata sul "colore"
def plot_first_events(events, num_events=10):
    # PROFFFFF NON VA UN CAZZO
    # Coordinate centro Moduli [m]
    xmod = [-5, 5, -5, 5]
    ymod = [5, 5, -5, -5]
    
    # Coordinate dei Sensori [m]
    xdet = [-2.5, 2.5, 0, -2.5, 2.5]
    ydet = [2.5, 2.5, 0, -2.5, -2.5]

    for i, event in enumerate(events[:num_events]):
        plt.figure()
        
        # estraggo i timestamp di tutti gli Hit per normalizzare il colore
        timestamps = [hit.timestamp for hit in event.hits]
        norm = plt.Normalize(min(timestamps), max(timestamps))  # normalizzazione dell'insieme temporale
        
        # Plot di ogni Hit con colore in base al timestamp
        for hit in event.hits:
            # # calcolo x e y per ogli HIt
            x = xmod[hit.module_id] + xdet[hit.sensor_id]
            y = ymod[hit.module_id] + ydet[hit.sensor_id]
            
            # determino colore in base al timestrap
            plt.scatter(x, y, c=[hit.timestamp], cmap='viridis', norm=norm, s=100, alpha=0.8)
        
        cbar = plt.colorbar(label="Tempo di rilevazione (ns)")
        cbar.set_label("Timestamp (ns)", rotation=270, labelpad=15)
        
        # faccio un plot di tuttigli hit che mi interessano
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.xlabel("X [m]")
        plt.ylabel("Y [m]")
        plt.title(f"Evento {i + 1} - Numero di Hit: {event.num_hits}")
        plt.show()

plot_first_events(events)