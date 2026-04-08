"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    multi = 1
    for i in range(1, n + 1):
        multi = multi * i
    return multi
print(factorial_ciclo(int(input("Ingrese un número: "))))    


def factorial_recursivo(n):
    pass
