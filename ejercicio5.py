# Dada una secuencia de caracteres, obtener dicha secuencia invertida.
# primera forma
cadena = "josue"
cadena_invertida = ""
for letra in reversed(cadena):
    cadena_invertida +=letra

print(cadena_invertida)

# segunda forma
cadena = "josue"
cadena_invertida = cadena[::-1]
print(cadena_invertida)


# llevada a la funcion
def invertir_cadena(palabra):
    cadena = palabra[::-1]
    return cadena

resultado = invertir_cadena(1234)
print(resultado)