"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    lista = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            lista.append(i)
    return f"Existem {len(lista)} pares los cuales son {lista}"
print(contar_pares_ciclo(int(input("Ingrese un número positivo: "))))

def contar_pares_recursivo(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + contar_pares_recursivo(n - 1)
    else:
        return contar_pares_recursivo(n - 1)
print(contar_pares_recursivo(int(input("Ingrese un número positivo: "))))