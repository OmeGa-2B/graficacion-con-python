import plotly.graph_objects as go
import numpy as np
from scipy.misc import derivative
import numdifftools as nd
import sys


def graficar(a, b, c, n, x0, y0):
    x, y = np.meshgrid(np.linspace(-20, 20, 100),np.linspace(-20, 20, 100))

    z = x**a + y**b + c*x*y

    fig = go.Figure(data=[go.Mesh3d(x=x.flatten(),
                                    y=y.flatten(),
                                    z=z.flatten(),
                                    opacity=0.3,
                                    color='rgba(244,22,100,0.6)'
                                    )])

    z_values = []
    x_values = []
    y_values = []

    z0 = obtener_z0(x0,y0,a,b,c)
    z_values.append(z0)
    x_values.append(y0)
    y_values.append(x0)
    fig.add_trace(go.Scatter3d(x=[x0], y=[y0], z=[z0], mode='markers', marker=dict(size=5, color='green')))
    print(f"punto 1 {x0, y0, z0}")
    for i in range(n-1):
        gradient = derivadas_parciales(a, b, c, x0, y0)
        xt, yt = normalizar(gradient)
        print(f"normalizado: {xt},{yt}")

        x0 = x0 + xt
        y0 = y0 + yt
        print(f"punto {i+2} {x0, y0, z0}")
        z0 = obtener_z0(x0,y0,a,b,c)

        if z0 == False:
            break

        z_values.append(z0)
        x_values.append(y0)
        y_values.append(x0)

        fig.add_trace(go.Scatter3d(x=[x0], y=[y0], z=[z0], mode='markers', marker=dict(size=5, color='red')))




    z_limit = max(z_values) + 20
    z[z > z_limit] = z_limit

    x_limit = max(x_values) + 20
    x[x > x_limit] = x_limit

    y_limit = max(y_values) + 20
    y[y > y_limit] = y_limit

    fig.update_layout(
        scene = dict(
            xaxis = dict(nticks=4, range=[-x_limit,x_limit],),
                        yaxis = dict(nticks=4, range=[-y_limit,y_limit],),
                        zaxis = dict(nticks=4, range=[-z_limit,z_limit],),),
        width=700,
        margin=dict(r=20, l=10, b=10, t=10))

    fig.show()

def obtener_z0(x0,y0,a,b,c):
    try:
        z0 = x0**a + y0**b + c*x0*y0

        if z0 == np.inf or z0 == np.nan:
            print(f"se ha topado con un punto critico en ({x0},{y0})")
            return False
        else:
            return z0

    except Exception as e:
        print(f"Se ha producido una excepción: {e}")
        sys.exit()

def normalizar(gradient):
    magnitude = np.linalg.norm(gradient)
    if magnitude == 0:
        return gradient
    else:
        normalized = gradient / magnitude
        return normalized



def derivadas_parciales(a, b, c, x0, y0):
    dx = 1e-6
    try:
        df_dx = derivative(lambda x: f(x, y0, a, b, c), x0, dx=dx)
        df_dy = derivative(lambda y: f(x0, y, a, b, c), y0, dx=dx)

    except Exception as e:
        print(f"Se ha producido una excepción: {e}")
        sys.exit()

    gradient = np.array([df_dx, df_dy])

    return gradient

def f(x, y, a, b, c):
    return x**a + y**b + c*x*y

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
n = int(input("Ingrese el numero de iteraciones: "))
x0 = float(input("Ingrese el valor de x0: "))
y0 = float(input("Ingrese el valor de y0: "))

graficar(a, b, c, n, x0, y0)