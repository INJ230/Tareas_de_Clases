def encontrar_mayor(a, b, c):
    # Encontrar el mayor valor entre a, b y c
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def encontrar_menor(a, b, c):
    # Encontrar el menor valor entre a, b y c
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

def main():
    # Leer tres valores
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    C = float(input("Ingrese el valor de C: "))
    
    # Llamar a las funciones para encontrar el mayor y el menor
    mayor = encontrar_mayor(A, B, C)
    menor = encontrar_menor(A, B, C)

    # Imprimir el resultado
    print(f"El mayor valor es: {mayor}")
    print(f"El menor valor es: {menor}")

# Llamar a la función principal
main()
