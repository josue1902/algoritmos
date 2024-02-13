# Implementar una función para calcular el producto de dos números enteros dados.

def calcular_producto(n1, n2):
    return n1 * n2

resultado = calcular_producto(5, 5)
print(resultado)




print("""
    Elige una opcion
    1) anadir libro
    2) Buscar libro
    3) Prestar libro
    4) Devolver libro
    5) Listar libros


""")


biblioteca = []

while True:
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        titulo = input("Ingrese el título del libro (o 'fin' para terminar): ")

        if titulo.lower() == 'fin':
            break

        autor = input("Ingrese el autor del libro: ")
        anio_publicacion = input("Ingrese el año de publicación del libro: ")
        

        libro_actual = [titulo, autor, anio_publicacion]

        biblioteca.append(libro_actual)
        

    elif opcion == 2:
        titulo_libro = input("Ingrese el nombre del libro: ")
        for libro in biblioteca:
            if titulo in libro[0]:
                print("Informacion del libro", libro)

        else:
            print("No se ha encontrado el libro")


print(biblioteca)