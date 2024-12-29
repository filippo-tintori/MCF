import sys
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib import  transforms

def random_walk_2d(s, N):
    phi = np.random.uniform(low=0, high=2 * np.pi, size=N)
    
    deltaX = s * np.cos(phi)
    deltaY = s * np.sin(phi)
    
    x = np.cumsum(deltaX)
    y = np.cumsum(deltaY)
    
    x = np.insert(x, 0, 0)
    y = np.insert(y, 0, 0)
    
    return x, y

# Parametri
s = 1  
N1, N2, N3 = 10, 100, 1000
num_walkers = 100

# 2A
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
for i in range(5):
    x, y = random_walk_2d(s, N3)
    plt.plot(x, y, label=f"Walker {i+1}")
plt.title("5 Random Walkers - 1000 passi")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.legend()

# 2B
plt.subplot(1, 2, 2)
for N, marker, label in zip([N1, N2, N3], ['o', 's', 'd'], ['10 passi', '100 passi', '1000 passi']):
    positions = np.zeros((num_walkers, 2))
    for i in range(num_walkers):
        x, y = random_walk_2d(s, N)
        positions[i, :] = [x[-1], y[-1]]
    plt.scatter(positions[:, 0], positions[:, 1], label=label, alpha=0.6, marker=marker)
    print(x,y)
plt.title("Posizioni finali di 100 Random Walkers")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.legend()
# 3
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# 3A
for i in range(5):
    x, y = random_walk_2d(s, N3)
    axs[0].plot(x, y, label=f"Walker {i+1}")
axs[0].set_title("5 Random Walkers - 1000 passi")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].axis('equal')
axs[0].legend()

# 3B
for i in range(5):
    x, y = random_walk_2d(s, N3)
    d2 = x**2 + y**2
    axs[1].plot(range(N3 + 1), d2, label=f"Walker {i+1}")
axs[1].set_title("Distanza quadrata dal punto di partenza")
axs[1].set_xlabel("Numero di passi")
axs[1].set_ylabel("Distanza quadrata")
axs[1].legend()

plt.tight_layout()
plt.show()
