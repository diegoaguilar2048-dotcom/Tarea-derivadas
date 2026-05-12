import numpy as np

def resolver_ejercicio_grado_5():
    # 1. Datos completos de la tabla (6 puntos -> Grado 5)
    x_datos = np.array([1.5, 1.9, 2.1, 2.4, 2.6, 3.1])
    f_datos = np.array([1.0628, 1.3961, 1.5432, 1.7349, 1.8423, 2.0397])
    
    x_eval = 2.25
    h = 0.15  # Mantenemos h = 0.15 para usar los puntos f(2.1) y f(2.4)
    
    # 2. Ajuste del polinomio interpolante de grado 5
    coefs = np.polyfit(x_datos, f_datos, 5)
    polinomio = np.poly1d(coefs)
    
    # 3. Derivadas analíticas del polinomio
    d1_poly = np.polyder(polinomio, 1)
    d2_poly = np.polyder(polinomio, 2)
    
    # 4. Valores para Métodos de Diferencias Finitas
    # Evaluamos el polinomio en los puntos clave
    f_x = polinomio(x_eval)            # f(2.25)
    f_x_h_der = polinomio(x_eval + h)    # f(2.4)
    f_x_h_izq = polinomio(x_eval - h)    # f(2.1)
    
    # --- CÁLCULOS ---
    # Primera Derivada
    d1_adelante = (f_x_h_der - f_x) / h
    d1_atras = (f_x - f_x_h_izq) / h
    d1_centrada = (f_x_h_der - f_x_h_izq) / (2 * h)
    
    # Segunda Derivada
    d2_centrada = (f_x_h_der - 2*f_x + f_x_h_izq) / (h**2)

    # --- SALIDA ---
    print(f"--- Análisis con Polinomio Global de Grado 5 ---")
    print(f"Puntos usados: Todos ({len(x_datos)} puntos)")
    
    print(f"\n1. PRIMERA DERIVADA f'({x_eval}):")
    print(f"  - Analítica (Polinomio):    {d1_poly(x_eval):.8f}")
    print(f"  - Diferencia Adelante:      {d1_adelante:.8f}")
    print(f"  - Diferencia Atrás:         {d1_atras:.8f}")
    print(f"  - Diferencia Centrada:      {d1_centrada:.8f}")
    
    print(f"\n2. SEGUNDA DERIVADA f''({x_eval}):")
    print(f"  - Analítica (Polinomio):    {d2_poly(x_eval):.8f}")
    print(f"  - Diferencia Centrada:      {d2_centrada:.8f}")

if __name__ == "__main__":
    resolver_ejercicio_grado_5()
