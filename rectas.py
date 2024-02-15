#este programa graficara un cierto numero de ractas aleatoriamente dentro de un cubo
#calcula el vector de cada una y las ecuaciones vectoriales, los guarda en un archivo de texto

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os

#generacion de puntos al azar
def puntos_aleatorios(t):
    puntos=[]
    for recta in range(int(t)*2):
        x = np.random.rand() * 100
        y = np.random.rand() * 100
        z = np.random.rand() * 100
        puntos.append((x, y, z))
    return puntos


def graficar(puntos,t):
    #archivo
    name = "ecuaciones.txt"#nombre del archivo
    dirc = "ruta donde se guardara el archivo"

    dir_com = os.path.join(dirc,name)

    # Define los vértices del cubo
    vertices = [
        [0, 0, 0],
        [100, 0, 0],
        [100, 100, 0],
        [0, 100, 0],
        [0, 0, 100],
        [100, 0, 100],
        [100, 100, 100],
        [0, 100, 100]
    ]

    # Define las caras del cubo utilizando los vértices
    caras = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[7], vertices[6], vertices[2], vertices[3]],
        [vertices[0], vertices[4], vertices[7], vertices[3]],
        [vertices[1], vertices[5], vertices[6], vertices[2]],
        [vertices[4], vertices[5], vertices[6], vertices[7]]
    ]

    # Crea una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Grafica el cubo
    ax.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Ajusta los límites de los ejes
    ax.set_xlim([0, 110])
    ax.set_ylim([0, 110])
    ax.set_zlim([0, 110])

    # Etiqueta los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    archivo = open(dir_com, 'w') #indica que a partir de aqui inica la escritura del archivo
    archivo.write('Ecuaciones vectoriales de las rectas 3D\n')
    count = 1

    for i in range(0, len(puntos), 2):
        x_inicial, y_inicial, z_inicial = puntos[i] #toma el primer vector del arreglo
        x_final, y_final, z_final = puntos[i + 1] #toma el valor siguiente del arreglo
        ax.plot([x_inicial, x_final], [y_inicial, y_final], [z_inicial, z_final], label='Recta {}'.format(count)) #grafica la recta de acuerdo a los dos vectores

        if int(t) < 100:
            ax.text(x_inicial,y_inicial,z_inicial,label = 'R{}'.format(count))

        #escribe en el archivo de texto
        archivo.write('\n----------------------------------------\n')
        archivo.write('Recta: {}'.format(count))
        count = count + 1

        #calculo del vector director
        XD = x_final-x_inicial
        YD = y_final-y_inicial
        ZD = z_final-z_inicial

        #escribe en el archivo de texto
        archivo.write('\npunto: ({:.2f},{:.2f},{:.2f})'.format(x_inicial,y_inicial,z_inicial))
        archivo.write('\nVector director: ({:.2f},{:.2f},{:.2f})'.format(XD,YD,ZD))
        archivo.write('\necuacion vetorial: ({:.2f},{:.2f},{:.2f})+t({:.2f},{:.2f},{:.2f})'.format(x_inicial,y_inicial,z_inicial,XD,YD,ZD))

    ax.set_title('Rectas')
    ax.legend(loc='upper left')

    archivo.close()
    # Muestra el gráfico
    plt.show()

flag = False
while(flag == False):
    t = input("\nintrodsuca un numero entero entre 1 a 10,000: ")
    if int(t) <= 10000 and int(t) > 0:
        puntos = puntos_aleatorios(t)
        graficar(puntos,t)
        flag = True
    else:
        print("\nel numero dado esta fuera del rango establecido")