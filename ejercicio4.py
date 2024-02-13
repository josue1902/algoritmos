# Desarrollar una función que permita convertir un número romano en un número decimal.
def numero_romano(num):
    num_convertido = 0
    
    diccionario = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    prev_valor = 0

    for letra in reversed(num):
        valor = diccionario[letra]

        if valor < prev_valor:
            num_convertido -= valor
        else:
            num_convertido += valor

        prev_valor = valor

    return num_convertido

resultado = numero_romano("DXXD")
print(resultado)
