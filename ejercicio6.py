# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def numro_binario(numero):
    lista = []
    while True:
        residuo = numero % 2
        
        lista.append(residuo)
        numero//=2
        if numero <= 0:
            break
    lista.reverse()
    return lista
    
resultado = numro_binario(450)
print(f"El numero convertdio a binario es {resultado}")