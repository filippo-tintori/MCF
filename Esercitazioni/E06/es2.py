import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import argparse

def harmonic_potential(x, k=1):
    """Potenziale armonico: V(x) = (1/2) * k * x^2"""
    return 0.5 * k * x**2

def double_well_potential(x, a=1, b=1):
    """Potenziale doppio pozzo: V(x) = a * x^4 - b * x^2"""
    return a * x**4 - b * x**2

def quartic_potential(x, a=1):
    """Potenziale quartico simmetrico: V(x) = a * x^4"""
    return a * x**4

def calculate_period(V, x0, m=1, num_points=1000):
    """
    Calcola il periodo T integrando numericamente con il metodo di Simpson
    per un dato potenziale V(x) e il punto di partenza x0.
    """
    x_values = np.linspace(0, x0, num_points)
    V0 = V(x0)
    integrand = lambda x: 1 / np.sqrt(V0 - V(x))
    
    y_values = np.array([integrand(x) if V0 > V(x) else 0 for x in x_values])
    integral_value = simpson(y_values, x=x_values)
    T = np.sqrt(8 * m) * integral_value
    return T

def main():
    parser = argparse.ArgumentParser(description="Calcola il periodo T in funzione di x0 per vari potenziali.")
    parser.add_argument("--potential", type=str, choices=['harmonic', 'double_well', 'quartic'], default='harmonic',
                        help="Scegli il tipo di potenziale: harmonic, double_well o quartic.")
    parser.add_argument("--x0_max", type=float, default=2.0, help="Massimo valore per x0.")
    parser.add_argument("--num_points", type=int, default=100, help="Numero di punti per il calcolo.")
    args = parser.parse_args()

    # Scelta del potenziale
    if args.potential == 'harmonic':
        V = harmonic_potential
        potential_name = "Armonico"
    elif args.potential == 'double_well':
        V = double_well_potential
        potential_name = "Doppio Pozzo"
    elif args.potential == 'quartic':
        V = quartic_potential
        potential_name = "Quartico"
    
    # Range di x0
    x0_values = np.linspace(0.1, args.x0_max, args.num_points)
    T_values = []

    # Calcolo di T per ogni x0
    for x0 in x0_values:
        T = calculate_period(V, x0)
        T_values.append(T)

    # Grafico di T in funzione di x0
    plt.plot(x0_values, T_values, label=f"Potenziale {potential_name}")
    plt.xlabel("$x_0$")
    plt.ylabel("$T(x_0)$")
    plt.title("Periodo $T$ in funzione di $x_0$ per diversi potenziali")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()