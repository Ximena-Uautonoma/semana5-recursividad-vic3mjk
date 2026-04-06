def contar_ciclo(n):
    num = []
    for i in range(1, n + 1):
         num.append(i)
    return num
print(contar_ciclo(10))

def contar_recursivo(n):
    if n <= 0:
        return []
    return contar_recursivo(n - 1) + [n]
print(contar_recursivo(10))
