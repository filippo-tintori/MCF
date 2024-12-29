import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import argparse
import sys


parser = argparse.ArgumentParser(description="Seleziona il grafico da visualizzare o il file da leggere.")
parser.add_argument(
    "--file",
    type=str,
    default="/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E06/vel_vs_time.csv",
    help="Percorso del file CSV da leggere"
)
parser.add_argument(
    "--plot",
    choices=["vel", "x", "both"],
    default="both",
    help="Seleziona il grafico da visualizzare: 'vel' per velocità, 'x' per posizione, 'both' per entrambi"
)
args = parser.parse_args(args=[] if sys.argv[1:] == [] else None)  # Esegue il parser solo se ci sono argomenti

# Lettura dei dati dal file specificato
data = pd.read_csv(args.file)

# Estrazione dei dati di tempo e velocità
time = data["t"].values
vel = data["v"].values

# Funzione per visualizzare il grafico della velocità
def plot_velocity():
    plt.plot(time, vel, color="royalblue", label="Dati")
    plt.xlabel("t")
    plt.ylabel("v")
    plt.legend(loc="best")
    plt.title("Grafico della Velocità")
    plt.show()

# Funzione per visualizzare il grafico della posizione
def plot_position():
    # Calcolo e grafico della posizione integrando la velocità
    integrale = integrate.simpson(vel, x=time)
    print("Integrale totale (distanza percorsa):", integrale)

    # Calcolo della posizione cumulativa a partire dalla velocità
    x = [integrate.simpson(vel[:i+1], dx=time[i+1] - time[i]) for i in range(1, len(vel)-1)]

    plt.plot(time[1:-1], x, color="royalblue", label="Dati")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.legend(loc="best")
    plt.title("Grafico della Posizione")
    plt.show()

# Selezione dei grafici da visualizzare in base all'argomento o al default
if args.plot == "vel":
    plot_velocity()
elif args.plot == "x":
    plot_position()
elif args.plot == "both":
    plot_velocity()
    plot_position()