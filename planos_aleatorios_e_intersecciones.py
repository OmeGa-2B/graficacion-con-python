import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def son_iguales(plano1, plano2):
    return np.allclose(plano1, plano2, atol=1e-2)  # Tolerancia para manejar pequeñas diferencias numéricas, si son muy cercanas el plano se condidera le mismo

def graficar(n):
    name = "Intersecciones_planos.txt"
    dirc = "direccion donde se guardara el archivo"

    dir_com = os.path.join(dirc, name)

    planos = []
    for _ in range(int(n)):
        A, B, C, D = np.random.rand(4)
        planos.append((A, B, C, D))

    def interseccion_planos(plano1, plano2):
        A1, B1, C1, D1 = plano1
        A2, B2, C2, D2 = plano2
        archivo.write("\nPlano: {:.2f}x+{:.2f}y+{:.2f}z={:.2f}".format(A1,B1,C1,D1))
        archivo.write("\nPlano: {:.2f}x+{:.2f}y+{:.2f}z={:.2f}\n".format(A2,B2,C2,D2))

        # Encontrar la dirección de la recta de intersección
        direccion = np.array([B1 * C2 - B2 * C1, A2 * C1 - A1 * C2, A1 * B2 - A2 * B1])

        punto_interseccion = np.array([
            (B1 * D2 - B2 * D1) / (A1 * B2 - A2 * B1),
            (A2 * D1 - A1 * D2) / (A1 * B2 - A2 * B1),
            0  # Aquí asumimos que z = 0, ya que estamos en el plano XY
        ])

        return direccion, punto_interseccion

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for plano in planos:
        A, B, C, D = plano
        x, y = np.meshgrid(range(-100, 100), range(-100, 100))
        z = (D - A * x - B * y) / C
        ax.plot_surface(x, y, z, alpha=0.3)

    archivo = open(dir_com, 'w')

    archivo.write('Puntos de Interseccion de un plano con otro\n')
    count = 0

    # Calcular e graficar las rectas de intersección
    for i in range(int(n)):
        count += 1
        archivo.write('\n----------------------------------------------------\n')
        archivo.write('Plano {}\n'.format(count))
        for j in range(i+1, int(n)):
            archivo.write('\nInterseccion con el plano {}\n'.format(j))

            if son_iguales(planos[i], planos[j]):
                archivo.write('Los planos son iguales.\n')
            else:
                direccion, punto_interseccion = interseccion_planos(planos[i], planos[j])
                #si todos los elementos en el vector director
                # son cero, la dirección de la línea es nula o no está definida.
                if not np.any(direccion):
                    archivo.write('Los planos son paralelos y no se intersecan.\n')
                else:
                    archivo.write('Dirección de la recta: {}\n'.format(direccion))
                    archivo.write('Punto de intersección: {}\n'.format(punto_interseccion))
                    t = np.linspace(-200, 200, 1000)
                    recta = np.outer(punto_interseccion, np.ones(t.shape)) + np.outer(direccion, t)
                    ax.plot(recta[0], recta[1], recta[2], label='interc. P{} con P{}'.format(i+1,j+1))

    ax.legend(loc='lower right')
    archivo.close()
    plt.show()


flag = 0
while flag == 0:
    n = input("\nIntroduzca un número entre 1 y 20 para el número de planos: ")
    if int(n) >= 1 and int(n) <= 20:
        graficar(n)
        flag = 1
    else:
        print("\nNúmero está fuera del rango permitido")
