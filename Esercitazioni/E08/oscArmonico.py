import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import argparse

def oscArm(y, t, omega):
    x, v = y
    dydt = [v, -omega**2 * x**3]
    return dydt

omega = 1.0
t = np.linspace(0, 20, 1000)

condIniz = [
    # x    v
    (1.0, 0.0),
    (0.5, 0.0),
    (1.0, 0.5),
    (0.5, 0.5)
]

plt.figure()

for x0, v0 in condIniz:
    y0 = [x0, v0]
    solution = odeint(oscArm, y0, t, args=(omega,))
    x = solution[:, 0]
    plt.plot(t, x, label=fr'$x_0$={x0}, $v_0$={v0}')

plt.title('Oscillatore anarmonico')
plt.xlabel('Tempo (s)')
plt.ylabel('Posizione x(t)')
plt.legend(loc="best")
plt.grid()
plt.show()