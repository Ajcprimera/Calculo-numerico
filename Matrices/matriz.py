import random

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 20))  # Números aleatorios del 1 al 20
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz_a = crear_matriz(filas, columnas)
matriz_b = crear_matriz(filas, columnas)

print("La primera matriz es:")
for fila in matriz_a:
    print(fila)

print("\nLa segunda matriz es:")
for fila in matriz_b:
    print(fila)

resultado_suma = sumar_matrices(matriz_a, matriz_b)
if resultado_suma:
    print("\nLa suma de las matrices es:")
    for fila in resultado_suma:
        print(fila)
