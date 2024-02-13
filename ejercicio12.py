def calcular_termino(n, a1, r):
    if n == 1:
        return a1
    else:
        return r * calcular_termino(n-1, a1, r)

res = calcular_termino(1, 2, -3)
print(res)