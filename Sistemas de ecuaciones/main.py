from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from operaciones import Graficacion,vector,matriz

def main():
    graficacion = Graficacion()
    punto = graficacion.sol_ecuacion()
    print(matriz)
    print(vector)
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in matriz]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y = np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z1 = (vector[0] - matriz[0][0]*X - matriz[0][1]*Y) / matriz[0][2]
    Z2 = (vector[1] - matriz[1][0]*X - matriz[1][1]*Y) / matriz[1][2]
    Z3 = (vector[2] - matriz[2][0]*X - matriz[2][1]*Y) / matriz[2][2]
    ax.plot_surface(X, Y, Z1, alpha=0.5)
    ax.plot_surface(X, Y, Z2, alpha=0.5)
    ax.plot_surface(X, Y, Z3, alpha=0.5)

    ax.scatter(punto[0], punto[1], punto[2], color='red')


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':
    main()