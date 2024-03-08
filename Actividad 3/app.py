from sympy import symbols,Eq,solve #Importamos las librerias Sympy y numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def read_root():
    x,y,z=symbols("x y z")
    ecuacion1=Eq((2*x-4*y+6*z),20)
    ecuacion2=Eq((5*x-3*y+4*z),20)
    ecuacion3=Eq((3*x-7*y+5*z),20) # Definimos las 3 ecuaciones 

    print("Ecuacion 1:", ecuacion1) 
    print("Ecuacion 2:", ecuacion2)
    print("Ecuacion 3:", ecuacion3)

    solucion=solve((ecuacion1,ecuacion2,ecuacion3),(x,y,z))
    x_valores=[solucion[x].evalf()]
    y_valores=[solucion[y].evalf()]
    z_valores=[solucion[z].evalf()]

    x_mesh, y_mesh = np.meshgrid(np.linspace(-10, 10, 50), np.linspace(-10, 10, 50))
    z_mesh1 = (20 - 2*x_mesh + 4*y_mesh) / 6
    z_mesh2 = (20 - 5*x_mesh + 3*y_mesh) / 4
    z_mesh3 = (20 - 3*x_mesh + 7*y_mesh) / 5 #Operamos las ecuaciones 

    figura=plt.figure()
    ax=figura.add_subplot(111,projection="3d")

    ax.plot_surface(x_mesh, y_mesh, z_mesh1, alpha=0.5)
    ax.plot_surface(x_mesh, y_mesh, z_mesh2, alpha=0.5)
    ax.plot_surface(x_mesh, y_mesh, z_mesh3, alpha=0.5)


    ax.scatter(x_valores,y_valores,z_valores,c="r",marker="o")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()
read_root()