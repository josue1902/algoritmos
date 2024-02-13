# Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero. 
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro el número a calcular su raíz.
import math

def calcular_raiz(numero):
    solucion = math.sqrt(numero)
    return int(solucion)

resultado = calcular_raiz(36)
print(resultado)