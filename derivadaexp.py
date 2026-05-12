import numpy as np
import sympy as sp

def calcular_derivadas_tablas():
    # 1. Entrada de datos
    x_sym = sp.Symbol('x')
    func_input = input("Introduce la función (ej. x**4 + 2*x**2): ")
    
    try:
        expr = sp.sympify(func_input)
        f_np = sp.lambdify(x_sym, expr, 'numpy')
        
        # Derivadas exactas para el error
        d1_exacta = sp.lambdify(x_sym, sp.diff(expr, x_sym), 'numpy')
        d2_exacta = sp.lambdify(x_sym, sp.diff(expr, x_sym, 2), 'numpy')
        
        x_val = float(input("Introduce el valor de x: "))
    except Exception as e:
        print(f"Error: {e}")
        return

    h_list = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
    v_real1 = d1_exacta(x_val)
    v_real2 = d2_exacta(x_val)

    # --- TABLA PRIMERA DERIVADA ---
    print(f"\nANÁLISIS DE LA PRIMERA DERIVADA f'(x)")
    print("-" * 105)
    print(f"{'h':>6} | {'f(x) 6 dec':>15} | {'f(x) 8 dec':>15} | {'Err 6%':>15} | {'Err 8%':>15}")
    print("-" * 105)
    
    for h in h_list:
        d1_num = (f_np(x_val + h) - f_np(x_val - h)) / (2 * h)
        err1 = abs((d1_num - v_real1) / v_real1) * 100 if v_real1 != 0 else 0
        
        print(f"{h:6.3f} | {d1_num:15.6f} | {d1_num:15.8f} | {err1:15.6f} | {err1:15.8f}")

    # --- TABLA SEGUNDA DERIVADA ---
    print(f"\nANÁLISIS DE LA SEGUNDA DERIVADA f''(x)")
    print("-" * 105)
    print(f"{'h':>6} | {'f''(x) 6 dec':>15} | {'f''(x) 8 dec':>15} | {'Err 6%':>15} | {'Err 8%':>15}")
    print("-" * 105)
    
    for h in h_list:
        d2_num = (f_np(x_val + h) - 2*f_np(x_val) + f_np(x_val - h)) / (h**2)
        err2 = abs((d2_num - v_real2) / v_real2) * 100 if v_real2 != 0 else 0
        
        print(f"{h:6.3f} | {d2_num:15.6f} | {d2_num:15.8f} | {err2:15.6f} | {err2:15.8f}")

if __name__ == "__main__":
    calcular_derivadas_tablas()
