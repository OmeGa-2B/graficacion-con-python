import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D


def plot_parabola(x, y, z, h_max, tangent_length=3.0):
    name = "Parabola.txt"
    dirc = "direccion donde se guardara el archivo"
    dir_com = os.path.join(dirc,name)

    magnitud = np.linalg.norm([x, y, z])
    t = np.linspace(0, 1, 100)  # Valores de t desde 0 a 1

    # Parámetros de la parábola
    a = 4*h_max
    b = -a

    # Parametrización de la parábola
    x_t = x * t
    y_t = y * t
    z_t = a * t * (1 - t) + z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x_t, y_t, z_t, label='Parábola')

    ax.scatter([0], [0], [0], color='blue')
    ax.scatter([x], [y], [z], color='green')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.text(x, y, z, 'punto impacto', color='black', fontsize=12, verticalalignment='bottom')

    archivo = open(dir_com, 'w')

    if(x==0 and y == 0):
        archivo.write('Ecuacion del tiro vertical')
        archivo.write("(0,0,0)+t(0,0,{})".format(h_max))
    elif(y==0 and x != 0):
        r_a,r_b = valores(x,y,h_max)
        archivo.write('Ecuacion vectoriales de las rectas 3D\n')
        archivo.write("\nLa ecuación de la parabola es= F(t)= (t, {}t/{} , {}t^2 + {}t )".format(y,x,r_a,r_b))
    else:
        r_a,r_b = valores(x,y,h_max)
        archivo.write('Ecuacion vectoriales de las rectas 3D\n')
        archivo.write("\nLa ecuacion de la parabola es= F(t)= ({}t/{}, t , {}t^2 + {}t )".format(x,y,r_a,r_b))

    # Calcular y graficar las rectas tangentes
    t_values = [0, 0.25, 0.5, 0.75, 1]
    colors = ['khaki', 'darksalmon', 'cyan', 'chartreuse', 'aquamarine']
    for i, t in enumerate(t_values):
        x_tangent = x * t
        y_tangent = y * t
        z_tangent = a * t * (1 - t) + z
        dx_dt = x #esto pasa ya que x cambia a una ritmo constante al igual que su valor, movimiento rectilinio uniforme
        dy_dt = y
        dz_dt = a * (1 - 2 * t)#la derivada es una funcion de t y cambia a una velocidad que depende de t y a
        tangent_vector = np.array([dx_dt, dy_dt, dz_dt])
        tangent_vector /= np.linalg.norm(tangent_vector)  # Normalizar el vector

        #x(t) = x_t + t * (dx/dt)
        #y(t) = y_t + t * (dy/dt)
        #z(t) = z_t + t * (dz/dt)

        x_parametric = f'x(t) = {x_tangent} + {dx_dt}t'
        y_parametric = f'y(t) = {y_tangent} + {dy_dt}t'
        z_parametric = f'z(t) = {z_tangent} + {dz_dt}t'

        archivo.write("\n------------------------------\n")
        archivo.write("Tangente en ({},{},{})\n".format(x_tangent,y_tangent,z_tangent))
        archivo.write("\n")
        archivo.write(x_parametric)
        archivo.write("\n")
        archivo.write(y_parametric)
        archivo.write("\n")
        archivo.write(z_parametric)

        # Multiplicar el vector por el factor tangent_length para hacerlo más grande
        tangent_vector *= tangent_length

        ax.scatter([x_tangent], [y_tangent], [z_tangent], color='green')
        ax.plot([x_tangent - tangent_vector[0], x_tangent + tangent_vector[0]],
                [y_tangent - tangent_vector[1], y_tangent + tangent_vector[1]],
                [z_tangent - tangent_vector[2], z_tangent + tangent_vector[2]], color=colors[i],linestyle='--')

    arc_length = calculate_arc_length(x, y, z, h_max)
    archivo.write("\n------------------------------------------------------------------\n")
    archivo.write("\nLongitud de arco de la parabola: {:.2f}".format(arc_length))

    archivo.close()
    ax.legend()
    plt.show()

def valores(x,y,h_max):
    if (y != 0):
        b1=y/2
        b2=y
        c1=h_max
        c2=0

        d1=(y/2)*(y/2)
        e1=y/2
        d2=(y)*(y)
        e2=y

        D1=d1*e2-e1*d2
        D2=c1*e2-e1*c2
        D3=d1*c2-c1*d2
        r_a=D2/D1
        r_b=D3/D1
    else:
        b1=x/2
        b2=x
        c1=h_max
        c2=0

        d1=(x/2)*(x/2)
        e1=x/2
        d2=(x)*(x)
        e2=x

        D1=d1*e2-e1*d2
        D2=c1*e2-e1*c2
        D3=d1*c2-c1*d2
        r_a=D2/D1
        r_b=D3/D1

    valores_a_b = np.array([r_a,r_b])
    return valores_a_b

def calculate_arc_length(x, y, z, h_max):
    a = 4 * h_max
    t_values = np.linspace(0, 1, 100)
    arc_length = 0 #contador

    for i in range(1, len(t_values)):
        t1, t2 = t_values[i - 1], t_values[i] #optiene los valores de t adyacentes en la curva. t1 es el valor anterior y t2 es el valor actual.
        dx_dt = x                             #los obtine para despues calcular la longitud e ir sumandolos
        dy_dt = y
        dz_dt = a * (1 - 2 * t2)
        #Calcula la longitud del segmento de línea entre t1 y t2
        ds = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2) * (t2 - t1)
        arc_length += ds

    return arc_length



x = float(input("Ingrese la coordenada x del punto de impacto: "))
y = float(input("Ingrese la coordenada y del punto de impacto: "))
z = 0
h_max = float(input("Ingrese la altura máxima de la parábola: "))

plot_parabola(x, y, z, h_max, tangent_length=6.0)




