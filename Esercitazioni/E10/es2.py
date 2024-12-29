import numpy as np
import matplotlib.pyplot as plt

def distribuzione_probabilita_phi(phi):

    return (1/4) * np.sin(phi / 2)

def calcola_cumulativa_inversa(s):
    # Calcolo dell'inversa della cumulativa C^(-1)(s)
    # C(phi) = 1/2 (1 - cos(phi/2))
    # C^(-1)(s) = 2 * arccos(1 - 2s)
    return 2 * np.arccos(1 - 2 * s)

# par
num_punti = 10000

# calcola la cumulativa inversa
s = np.random.uniform(0, 1, num_punti)
phi = calcola_cumulativa_inversa(s)

# istogramma per distribuzione con teoria
plt.hist(phi, bins=50, density=True, alpha=0.6, color='g', label="Istogramma dati")

phi_teorico = np.linspace(0, 2 * np.pi, 1000)
p_phi_teorico = distribuzione_probabilita_phi(phi_teorico)
plt.plot(phi_teorico, p_phi_teorico, color='r', label="p(phi) teorica")
plt.xlabel("phi")
plt.ylabel("p(phi)")
plt.legend()
plt.title("Distribuzione dei valori di phi")
plt.show()

num_passi = 1000
num_camminatori = 5
x = np.zeros((num_camminatori, num_passi))
y = np.zeros((num_camminatori, num_passi))

s_x = 0.1 # spostamento costante verso DX

# parto da (0,0)
for i in range(1, num_passi):
    phi = calcola_cumulativa_inversa(np.random.uniform(0, 1, num_camminatori))
    x[:, i] = x[:, i-1] + np.cos(phi) + s_x
    y[:, i] = y[:, i-1] + np.sin(phi)

plt.figure(figsize=(10, 7))
plt.subplot(2,1,1)
for i in range(num_camminatori):
    plt.plot(x[i], y[i], label=f"Walker {i+1}")

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Traiettorie di 5 random walker (asimmetriche) - $s_x=0.1$")
plt.legend()
plt.axis('equal')

s_x = 0.01 # s

for i in range(1, num_passi):
    phi = calcola_cumulativa_inversa(np.random.uniform(0, 1, num_camminatori))
    x[:, i] = x[:, i-1] + np.cos(phi) + s_x
    y[:, i] = y[:, i-1] + np.sin(phi)

plt.subplot(2,1,2)
for i in range(num_camminatori):
    plt.plot(x[i], y[i], label=f"Walker {i+1}")

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Traiettorie di 5 random walker (asimmetriche) - $s_x=0.01$")
plt.legend()
plt.axis('equal')
plt.show()

# lunghezza dei passi per ogni camminatore
passi = np.zeros(num_passi - 1)
for i in range(1, num_passi):
    dx = x[:, i] - x[:, i-1]  
    dy = y[:, i] - y[:, i-1] 
    passi[i-1] = np.mean(np.sqrt(dx**2 + dy**2))  # lunghezza del passo medio

# Grafico della lunghezza del passo medio
plt.plot(range(1, num_passi), passi, label="$s_x=0.01$")
plt.xlabel("Passo")
plt.ylabel("Lunghezza del passo medio")
plt.legend()
plt.title("Lunghezza del passo medio in funzione del numero di passi")
plt.grid()
plt.show()