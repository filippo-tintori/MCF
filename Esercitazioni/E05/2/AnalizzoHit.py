import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import reco

# leggo Hit dai file
def read_hits_from_file(file_path):
    data = pd.read_csv(file_path, header=None, names=['module_id', 'sensor_id', 'time'])
    data['time'] = pd.to_numeric(data['time'], errors='coerce')
    data = data.dropna()
    hits = [reco.Hit(row['module_id'], row['sensor_id'], row['time']) for _, row in data.iterrows()]
    return hits

# raggruppo gli Hit in una finestra temporale
def group_hits_into_events(hits, time_window):
    hits.sort()  # ordino gli Hit per timestamp
    events = []
    current_event_hits = [hits[0]]

    for i in range(1, len(hits)):
        time_diff = hits[i] - hits[i - 1]
        if time_diff <= time_window:
            current_event_hits.append(hits[i])
        else:
            events.append(reco.Event(current_event_hits))
            current_event_hits = [hits[i]]
    
    # + ultimo evento
    if current_event_hits:
        events.append(reco.Event(current_event_hits))
    
    return events

def process_data(file_paths):
    all_hits = []
    for file in file_paths:
        all_hits.extend(read_hits_from_file(file))
    return all_hits

def create_events(hits, window=500):
    return group_hits_into_events(hits, window)

# Param
time_window = 10000  # Tempo in ns per separare eventi - DEVO MODIFICARE l'AMPIEZZA se non mi piace

# lista dei file
files = [
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M0.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M1.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M2.csv",
    "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E05/2/hit_times_M3.csv"
]

all_hits = []
for file in files:
    all_hits.extend(read_hits_from_file(file))

# creo eventi
events = group_hits_into_events(all_hits, time_window)

# stampa i primi 10 eventi - richista prof
for event in events[:10]: 
    print(event)

def plot_event_statistics(events):
    num_hits = [event.num_hits for event in events]
    durations = [event.duration for event in events]
    time_diffs = np.diff([event.start_time for event in events])

    plt.hist(num_hits, bins=20, color='blue', alpha=0.7)
    plt.xlabel("Numero di Hit per Evento")
    plt.ylabel("Conteggio")
    plt.title("Istogramma del numero di Hit per Evento")
    plt.show()

    plt.hist(durations, bins=20, color='green', alpha=0.7)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma della durata degli Eventi")
    plt.show()

    plt.hist(time_diffs, bins=20, color='purple', alpha=0.7)
    plt.xlabel("Differenza di Tempo tra Eventi (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma delle differenze di tempo fra Eventi consecutivi")
    plt.show()

    # Grafico del numero di hit in funzione della durata
    plt.scatter(durations, num_hits, c='red', alpha=0.5)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Numero di Hit")
    plt.title("Numero di Hit vs Durata dell'Evento")
    plt.show()

plot_event_statistics(events)