"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for i in range(1, exponente + 1):
        resultado = base * resultado
    return resultado
print(potencia_ciclo(int(input("ingrese la base: ")),int(input("Ingrese el exponente: "))))

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente-1)
print(potencia_recursiva(int(input("ingrese la base: ")),int(input("Ingrese el exponente: "))))