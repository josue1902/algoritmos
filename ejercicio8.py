# Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def reverse_list(lista):
    inicio = 0
    fin = len(lista) -1
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]

        inicio+=1
        fin-=1
    return lista


lista_origina = [1, 2, 3, 4, 5]
print(reverse_list(lista_origina))