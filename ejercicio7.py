# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def cantidad_digitos(numero):
    digitos = 0
    while True:
        numero //=10
        digitos+=1
        if numero == 0:
            break
    return digitos
    
resultado = cantidad_digitos(123456)
print(resultado)