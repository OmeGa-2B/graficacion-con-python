import numpy as np
import plotly.graph_objects as go
from scipy.misc import derivative
import sys

def f(x, y, a, b, c):

    return x**a + y**b + c*x + c*y

def derivadas_parciales(a, b, c, x0, y0):
    dx = 1e-6
    df_dx = derivative(lambda x: f(x, y0, a, b, c), x0, dx=dx)
    df_dy = derivative(lambda y: f(x0, y, a, b, c), y0, dx=dx)
    gradient = np.array([df_dx, df_dy])

    return gradient

def obtenerz(x0, y0, a, b, c):
    try:
        z0 = x0**a + y0**b + c*x0+c*y0
        return z0
    except Exception as e:
        print("\n")
        print(f"Se ha producido una excepción: {e}")
        print("\n")
        print("introdusca otrso valores")
        obtener_valores()

def comprobacion(x0, y0, a, b, c,ti,x1,y1):
    fc = (x0 + 0.1)**a + (y0 - 0.1)**b + c * (x0 + 0.1) + c * (y0 - 0.1)
    print(f"comprobacion funcion: {fc:.2f}")
    Zc = -x1*(x0+0.1)-y1*(y0-0.1)+ti
    print(f"comprobacion linealizacion: {Zc:.2f}")

def graficar(a, b, c, x0, y0):
    x, y = np.meshgrid(np.linspace(-500, 500, 100), np.linspace(-500, 500, 100))
    z = x**a + y**b + c*x + c*y

    fig = go.Figure(data=[go.Mesh3d(x=x.flatten(),
                                    y=y.flatten(),
                                    z=z.flatten(),
                                    opacity=0.3,
                                    color='rgba(244,22,100,0.6)')])

    z0 = obtenerz(x0, y0, a, b, c)
    fig.add_trace(go.Scatter3d(x=[x0], y=[y0], z=[z0], mode='markers', marker=dict(size=5, color='green')))

    gradient = derivadas_parciales(a, b, c, x0, y0)
    x1 = gradient[0] * -1
    y1 = gradient[1] * -1
    ti = z0+gradient[0]*(-1*x0)+gradient[1]*(-1*y0)

    fig.add_trace(go.Scatter3d(x=[x0], y=[y0], z=[z0], mode='markers', marker=dict(size=5, color='green')))
    print(f"{x1:.2f}x {y1:.2f}y + z = {ti:.2f}")
    print(f"Z = {ti:.2f} + ({-x1:.2f}x) + ({-y1:.2f}y)")

    # Graficación del plano
    x, y = np.meshgrid(np.linspace(-500, 500, 100), np.linspace(-500, 500, 100))
    zp = -x1*x - y1*y + ti
    fig.add_trace(go.Surface(z=zp, x=x, y=y, colorscale="greens", opacity=0.4))

    comprobacion(x0, y0, a, b, c,ti,x1,y1)

    z_limit = z0 + 300

    z[z > z_limit] = z_limit

    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=4, range=[-200, 200]),
            yaxis=dict(nticks=4, range=[-200, 200]),
            zaxis=dict(nticks=4, range=[-300, z_limit]),
        ),
        width=700,
        margin=dict(r=20, l=10, b=10, t=10)
    )

    fig.show()

def obtener_valores():
    # Input de valores
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    x0 = float(input("Ingrese el valor de x0: "))
    y0 = float(input("Ingrese el valor de y0: "))
    graficar(a, b, c, x0, y0)

obtener_valores()