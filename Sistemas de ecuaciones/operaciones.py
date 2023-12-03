import numpy as np
from ecuacion import Ecuacion

ec = Ecuacion()
matriz, vector = ec.generar_sistema()
class Graficacion():
    def __init__(self):
        self.punto= None
    
    def __str__(self):
        return self.punto

    def sol_ecuacion(self):
        self.punto = np.linalg.solve(matriz,vector)
        return self.punto
