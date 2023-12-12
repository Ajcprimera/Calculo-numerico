import random

from user import user

class Ecuacion:
    def __init__(self, user):
        self.matriz = []
        self.vector = []
        self.filas = user
        self.columnas = user


    def generar_sistema(self, value = None):
        '''self.filas = filas
        self.columnas = columnas'''
        numero_b = int(input('Ingresa el rango bajo del numero =>'))
        numero_a = int(input('Ingresa el rango alto del numero =>'))
        while numero_a < numero_b:
            numero_a = int(input('Ingresa un numero que sea mayor al numero de rango menor:'))
        self.matriz = [[None for i in range(self.columnas)] for j in range(self.filas)]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                value = random.randint(numero_b, numero_a)
                self.matriz[i][j] = value

        self.vector = [0]*self.columnas
        for i in range(self.columnas):
            value = random.randint(numero_b, numero_a)
            self.vector[i] = value

        return self.matriz, self.vector
    
