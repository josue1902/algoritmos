# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado

def suma_numeros(suma):
    if suma == 0 or suma == 1:
        return suma
    else:
        return suma + suma_numeros(suma -1)
    
resultado = suma_numeros(10)
print(resultado)