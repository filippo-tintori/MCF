import numpy as np
from tqdm import tqdm
import time

class MWPC:
    def __init__(self, spessore_camera, numero_fili):
        self.spessore_camera = spessore_camera
        self.numero_fili = numero_fili

    def genera_coppie(self, n_medio):
        return np.random.poisson(n_medio)

    def posizione_coppie(self, numero_coppie):
        return np.random.uniform(0, self.spessore_camera, numero_coppie)

class Simulazione:
    def __init__(self, mwpc, passo_diffusione, probabilita_assorbimento):
        self.mwpc = mwpc
        self.passo_diffusione = passo_diffusione
        self.probabilita_assorbimento = probabilita_assorbimento

    def simula_elettrone(self, posizione_iniziale):
        posizione = posizione_iniziale
        tempo = 0

        while posizione < self.mwpc.spessore_camera:
            posizione += self.passo_diffusione
            tempo += 1
            if np.random.random() < self.probabilita_assorbimento:
                return None, tempo

        return posizione, tempo

    def simula_evento(self, n_medio):
        numero_coppie = self.mwpc.genera_coppie(n_medio)
        posizioni_iniziali = self.mwpc.posizione_coppie(numero_coppie)

        risultati = []
        for posizione in posizioni_iniziali:
            risultato = self.simula_elettrone(posizione)
            if risultato[0] is not None:
                risultati.append(risultato)

        return risultati

mwpc = MWPC(spessore_camera=10, numero_fili=5)
simulazione = Simulazione(mwpc, passo_diffusione=0.1, probabilita_assorbimento=0.05)

# Aggiunta della barra di avanzamento con tqdm
risultati = []
for i in tqdm(range(1000)): 
    risultato_evento = simulazione.simula_evento(n_medio=20)
    risultati.extend(risultato_evento)

# Stampa dei risultati
for risultato in risultati:
    print("Posizione finale:", risultato[0], "- Tempo di deriva:", risultato[1])