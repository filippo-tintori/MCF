import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv"

data = pd.read_csv(url, comment='#')

"""
pl_orbper: Orbital Period [days]
pl_bmassj: Planet Mass or Mass*sin(i) [Jupiter Mass]
pl_orbsmax: Orbit Semi-Major Axis [au]
st_mass: Stellar Mass [Solar mass]
discoverymethod: Discovery Method
"""