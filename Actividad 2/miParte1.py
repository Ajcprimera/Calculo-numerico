import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib import pyplot as plt
#clase Spline
class SplineInterpolacion:
    '''
    + x: un array  de las primeras posiciones de cada punto
    + y: un array de las segundas posiciones de cada punto
    + spline_cubico: el valor resultante del spline cubico
    '''
    def __init__(self, puntos):
        self.x = np.array([float(p[0]) for p in puntos])
        self.y = np.array([float(p[1]) for p in puntos])
        self.spline_cubico = CubicSpline(self.x, self.y, bc_type= 'natural')
    #metodo que retorna el spline cubico de los puntos ingresados
    def evaluar(self, punto):
        return self.spline_cubico(punto)
    #metodos get
    def getX(self):
        return self.x
    def getY(self):
        return self.y
#INICIO DEL PROGRAMA
#inicializacion de variables
puntos = []
#entrada de datos
# Ejemplo de uso:
puntos = [[0,0], [1,1], [2,0], [3,-1]]
spline = SplineInterpolacion(puntos)
# Evaluar el spline en un punto
valor = spline.evaluar(1.5)
print("Valor interpolado en x=1.5:", valor)
#representamos
plt.plot(spline.getX(),spline.getY(),'o')
plt.show()