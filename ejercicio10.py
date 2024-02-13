# Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.
def suma_digito(numero):
    suma = 0
    while numero!=0:
        digito = numero % 10
        suma +=digito
        numero//=10
    return suma

resultado = suma_digito(11)
print(resultado)