# Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero.
def maximo_divisor(n1, n2):
    while n2 != 0:
        num = n1 % n2
        n1 = n2
        n2 = num

    return n1

resultado = maximo_divisor(150, 39)
print(resultado)
