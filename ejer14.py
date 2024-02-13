# Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def recorrer_lista(lista):
    lista_nueva = []
    if len(lista) == 1:
        return lista
    
    else:
        lista_nueva = lista[::-1]
        return lista_nueva

resultado = recorrer_lista([1, 2, 3, 4, 5,])
print(resultado)
