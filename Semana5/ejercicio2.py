"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    suma = 0
    for i in range(1 , n + 1):
        suma = suma + i
    return f"la suma es {suma}"
print(suma_ciclo(int(input("Ingresa un número: "))))


def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    pass
