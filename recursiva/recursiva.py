def sumarecursiva(n):
    if n <= 9:
        return n
    else:
        return sumarecursiva(n // 10) + n % 10

n = int(input("Ingresa un número entero: "))
resultado = sumarecursiva(n)
print("La suma de los dígitos de", n, "es:", resultado)

