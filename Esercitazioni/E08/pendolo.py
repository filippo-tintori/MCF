import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import csv
import argparse

def eq_pend(y, t, l):
    theta, omega = y
    dydt = [omega, -(g / l) * np.sin(theta)]
    return dydt
g = 9.81 # acc

l = 0.5
theta0 = np.radians(45)
omega0 = 0
y0 = [theta0, omega0]

t = np.linspace(0,10, 1000)

sol = odeint(eq_pend, y0, t, args=(l,))

# theta e omega
theta = sol[:, 0]
omega = sol[:, 1]


plt.figure(figsize=(10, 6))
plt.plot(t, np.degrees(theta), label=r"$\theta(t)$ (in gradi)")
plt.title("Moto del pendolo semplice")
plt.xlabel("Tempo (s)")
plt.ylabel(r"Angolo $\Theta$ (gradi)")
plt.legend()
plt.grid()
plt.show()

# confronto casi aggiuntivi
casi = [(1.0, 45),
        (0.5, 30)]

plt.figure(figsize=(10, 6))
for l, theta_deg in casi:
    theta0 = np.radians(theta_deg)
    y0 = [theta0, 0]
    solution = odeint(eq_pend, y0, t, args=(l,))
    theta = solution[:, 0]
    plt.plot(t, np.degrees(theta), label=f"l={l} m, θ₀={theta_deg}°")

plt.title("Confronto del moto del pendolo per diverse condizioni iniziali")
plt.xlabel("Tempo (s)")
plt.ylabel("Angolo $\Theta$ (gradi)")
plt.legend()
plt.grid()
plt.show()
