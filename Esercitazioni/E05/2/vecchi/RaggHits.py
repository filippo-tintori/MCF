import reco 
import numpy as np
import matplotlib.pyplot as plt

def group_hits_into_events(hits, time_window):
    hits.sort() 
    events = []
    current_event_hits = [hits[0]]

    for i in range(1, len(hits)):
        time_diff = hits[i] - hits[i - 1]
        if time_diff <= time_window:
            current_event_hits.append(hits[i])
        else:
            events.append(reco.Event(current_event_hits))
            current_event_hits = [hits[i]]
    
    if current_event_hits:
        events.append(reco.Event(current_event_hits))
    
    return events

def read_hits_from_file(file_path):
    data = pd.read_csv(file_path, header=None, names=['module_id', 'sensor_id', 'time'])
    data['time'] = pd.to_numeric(data['time'], errors='coerce')
    data = data.dropna()
    hits = [reco.Hit(row['module_id'], row['sensor_id'], row['time']) for _, row in data.iterrows()]
    return hits

# Parametri
time_window = 10000  # Tempo in ns per separare eventi (da calibrare)

# Lettura e combinazione degli Hit
files = [
    "/path/to/hit_times_M0.csv",  # Modifica con il percorso corretto
    "/path/to/hit_times_M1.csv",
    "/path/to/hit_times_M2.csv",
    "/path/to/hit_times_M3.csv"
]

all_hits = []
for file in files:
    all_hits.extend(read_hits_from_file(file))

# Creazione degli eventi
events = group_hits_into_events(all_hits, time_window)

# Stampa i primi 10 eventi
for event in events[:10]:
    print(event)

# Istogrammi richiesti
def plot_event_statistics(events):
    num_hits = [event.num_hits for event in events]
    durations = [event.duration for event in events]
    time_diffs = np.diff([event.start_time for event in events])

    # Istogramma del numero di Hit per evento
    plt.hist(num_hits, bins=20, color='blue', alpha=0.7)
    plt.xlabel("Numero di Hit per Evento")
    plt.ylabel("Conteggio")
    plt.title("Istogramma del numero di Hit per Evento")
    plt.show()

    # Istogramma della durata degli eventi
    plt.hist(durations, bins=20, color='green', alpha=0.7)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma della durata degli Eventi")
    plt.show()

    # Istogramma delle differenze di tempo fra eventi consecutivi
    plt.hist(time_diffs, bins=20, color='purple', alpha=0.7)
    plt.xlabel("Differenza di Tempo tra Eventi (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma delle differenze di tempo fra Eventi consecutivi")
    plt.show()

    # Grafico 2D del numero di hit in funzione della durata
    plt.scatter(durations, num_hits, c='red', alpha=0.5)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Numero di Hit")
    plt.title("Numero di Hit vs Durata dell'Evento")
    plt.show()

plot_event_statistics(events)