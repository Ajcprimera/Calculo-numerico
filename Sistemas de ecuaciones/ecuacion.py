import random


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
            numero_a = int(input('Ingresa un numero que sea mayor al numero de rango menor'))
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