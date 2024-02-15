import matplotlib.pyplot as plt
import numpy as np


def graficar(v1,v2,v3,v4,v5,v6,v7,v8, vr1, vr2, vr3, vr4):
    # Crear una figura y dos ejes (planos cartesianos)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Configurar el primer plano (ax1)
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(0, color='black', linewidth=1)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.set_xlabel('Eje X')
    ax1.set_ylabel('Eje Y')
    ax1.set_title('PLantilla 1')

    #graficacionde los vectores
    ax1.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax1.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax1.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax1.quiver(0, 0, v4[0], v4[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax1.quiver(0, 0, vr1[0], vr1[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax1.quiver(0, 0, vr2[0], vr2[1], angles='xy', scale_units='xy', scale=1, color='darkred')

    #muestra las coordenadas de los vectores en el primer plano
    ax1.text(vr1[0],vr1[1],'R1 = ({}, {})'.format(vr1[0],vr1[1]))
    ax1.text(vr2[0],vr2[1],'R2 = ({}, {})'.format(vr2[0],vr2[1]))

    # Configurar el segundo plano (ax2)
    ax2.axhline(0, color='black', linewidth=1)
    ax2.axvline(0, color='black', linewidth=1)
    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-10, 10)
    ax2.set_xlabel('Eje X')
    ax2.set_ylabel('Eje Y')
    ax2.set_title('Plantilla 2')

    #graficacionde los vectores
    ax2.quiver(0, 0, v5[0], v5[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax2.quiver(0, 0, v6[0], v6[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax2.quiver(0, 0, v7[0], v7[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax2.quiver(0, 0, v8[0], v8[1], angles='xy', scale_units='xy', scale=1, color='b')
    ax2.quiver(0, 0, vr3[0], vr3[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax2.quiver(0, 0, vr4[0], vr4[1], angles='xy', scale_units='xy', scale=1, color='darkred')

    #muestra las coordenadas de los vectores en el segundo plano
    ax2.text(vr3[0],vr3[1],'R1 = ({:.2f}, {:.2f})'.format(vr3[0],vr3[1]))
    ax2.text(vr4[0],vr4[1],'R2 = ({:.2f}, {:.2f})'.format(vr4[0],vr4[1]))
    # Mostrar los planos cartesianos
    plt.tight_layout()
    plt.grid()
    plt.show()

def calculo():
    a = input("introdusca un numero entero para a: ")
    b = input("introdusca un numero entero para b: ")
    c = input("introdusca un numero entero para c: ")
    d = input("introdusca un numero entero para d: ")

    #vectores que se grafican por defecto
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    v3 = np.array([-1, 0])
    v4 = np.array([0, -1])

    #en este caso los vectores se graficaran de acuerdo con la siguiente operacion de vectores
    #segun los vectores del primer plano
    vr1 = (float(a)*v1) + (float(b)*v2) + (float(c)*v3) + (float(d)*v4)
    vr2 = -(float(a)*v1) + (float(b)*v2) - (float(c)*v3) + (float(d)*v4)

    #vectores por defecto del segundo plano
    v5 = np.array([1, 1])
    v6 = np.array([-1, 1])
    v7 = np.array([-1, -1])
    v8 = np.array([1, -1])

    #en este caso los vectores se graficaran de acuerdo con la siguiente operacion de vectores
    #segun los vectores del segundo plano
    vr3 = (float(a)*v5) + (float(b)*v6) + (float(c)*v7) + (float(d)*v8)
    vr4 = -(float(a)*v5) + (float(b)*v6) - (float(c)*v7) + (float(d)*v8)

    graficar(v1,v2,v3,v4,v5,v6,v7,v8, vr1, vr2, vr3, vr4 )

calculo()

