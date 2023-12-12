import numpy as np
from scipy.integrate import simps
def funcion(x):
    return np.sin(x) + 0.5*np.cos(x) + 0.25*np.sin(2*x) + 0.1*np.cos(3*x) + 0.05*np.sin(4*x)+x
  

a = 0  
b = 4

n = 10  

x = np.linspace(a, b, n+1)  
y = funcion(x)  

print("Este es un ejemplo de la integral de la función:")
print("f(x) = sin(x) + 0.5*cos(x) + 0.25*sin(2*x)+0.1*cos(3*x) + 0.05*sin(4*x)+x")

print("Métodos disponibles:")
print("1. Método del trapecio") 
print("2. Método de Simpson")

metodo = int(input("Elija el método (1/2): "))

if metodo == 1:
    
    Integral = np.trapz(y, x)  
    print("Valor aproximado de la integral (trapecio): ", Integral)
    
elif metodo == 2:  
  
    Integral = simps(y, x)  
    print("Valor aproximado de la integral (Simpson): ", Integral)


x_precisa = np.linspace(a, b, 10001)  
y_precisa = funcion(x_precisa) 

if(metodo==1):
   valor_real = np.trapz(y_precisa, x_precisa)  
   print("Valor real de la integral: ", valor_real)

if(metodo==2):
   valor_real = simps(y_precisa, x_precisa) 
   print("Valor real de la integral: ", valor_real)