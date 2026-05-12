import numpy as np

def resolver_con_polinomio_local():
    # 1. Selección de vecinos más cercanos a x = 2.25
    # Usamos 4 puntos para un polinomio de grado 3 (local)
    x_vecinos = np.array([1.9, 2.1, 2.4, 2.6])
    f_vecinos = np.array([1.3961, 1.5432, 1.7349, 1.8423])
    
    x_eval = 2.25
    h = 0.15 # Distancia de 2.25 a 2.1 y 2.4
    
    # 2. Ajuste del polinomio interpolante (grado 3)
    coefs = np.polyfit(x_vecinos, f_vecinos, 3)
    polinomio = np.poly1d(coefs)
    
    # 3. Derivadas exactas del polinomio (para comparar)
    d1_poly = np.polyder(polinomio, 1)
    d2_poly = np.polyder(polinomio, 2)
    
    # 4. Valores necesarios para Diferencias Finitas
    f_x = polinomio(x_eval)          # f(2.25)
    f_x_h_der = polinomio(x_eval + h)  # f(2.4)
    f_x_h_izq = polinomio(x_eval - h)  # f(2.1)
    
    # --- CÁLCULOS DE DERIVACIÓN NUMÉRICA ---
    # Primera Derivada
    d1_adelante = (f_x_h_der - f_x) / h
    d1_atras = (f_x - f_x_h_izq) / h
    d1_centrada = (f_x_h_der - f_x_h_izq) / (2 * h)
    
    # Segunda Derivada
    d2_centrada = (f_x_h_der - 2*f_x + f_x_h_izq) / (h**2)

    # --- SALIDA DE RESULTADOS ---
    print(f"--- Análisis Local en x = {x_eval} (Grado 3) ---")
    print(f"Puntos usados: {x_vecinos}")
    
    print(f"\n1. PRIMERA DERIVADA f'({x_eval}):")
    print(f"  - Por Polinomio (Exacto):   {d1_poly(x_eval):.8f}")
    print(f"  - Diferencia hacia Adelante: {d1_adelante:.8f}")
    print(f"  - Diferencia hacia Atrás:    {d1_atras:.8f}")
    print(f"  - Diferencia Centrada:       {d1_centrada:.8f}")
    
    print(f"\n2. SEGUNDA DERIVADA f''({x_eval}):")
    print(f"  - Por Polinomio (Exacto):   {d2_poly(x_eval):.8f}")
    print(f"  - Diferencia Centrada:       {d2_centrada:.8f}")

if __name__ == "__main__":
    resolver_con_polinomio_local()
