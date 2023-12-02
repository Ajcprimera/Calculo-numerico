import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

class Ecuacion:
    def __init__(self):
        self.matriz = []
        self.vector = []
        self.filas = 0
        self.columnas = 0

    def __str__(self):
        return self.vector
    
    def __str__(self):
        return self.matriz

    def generar_matriz(self, filas = 3, columnas = 3, value = None):
        self.filas = filas
        self.columnas = columnas
        numero_b = int(input('Ingresa el rango bajo del numero =>'))
        numero_a = int(input('Ingresa el rango alto del numero =>'))
        while numero_a < numero_b:
            numero_a = int(input('Ingresa un numero que sea mayor al numero de rango menor:'))
        self.matriz = [[None for i in range(columnas)] for j in range(filas)]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                value = random.randint(numero_b, numero_a)
                self.matriz[i][j] = value

        self.vector = [0]*columnas
        for i in range(columnas):
            value = random.randint(numero_b, numero_a)
            self.vector[i] = value

        return self.matriz, self.vector
    
ecuacion = Ecuacion()

matriz, vector = ecuacion.generar_matriz()
print(vector)
print(matriz)

class Graficacion:
    def __init__(self):
        self.punto=np.linalg.solve(matriz,vector)

    def __str__(self):

        return self.punto

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

ax.scatter(Graficacion().punto[0], Graficacion().punto[1], Graficacion().punto[2], color='red')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

   


    


