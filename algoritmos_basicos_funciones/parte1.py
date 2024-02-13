"""def factorial(numero):
    if (numero == 0):
        return 1
    else:
        return numero * factorial(numero -1)
    
resultado = factorial(5)
print(resultado)"""
 
def fibonacci(n):
    n0 = 0
    n1  = 1
    fib = 0 
    if(n == 0 or n == 1):
        fib = n
    else:
        i = 2
        while (i <= n):
            fib = n0 + n1
            n0 = n1
            n1 = fib
            i +=1

    return fib


resultado  = fibonacci(9)
print(resultado)