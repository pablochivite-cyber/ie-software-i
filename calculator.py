def calcular(a, operador, b):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            return "Error: no se puede dividir entre 0"
        return a / b
    else:
        return "Error: operador no válido"


print("Calculadora básica (escribe 'salir' para terminar)")

while True:
    entrada = input("\nPrimer número: ")
    if entrada.lower() == "salir":
        break

    try:
        a = float(entrada)
        operador = input("Operador (+, -, *, /): ")
        b = float(input("Segundo número: "))
    except ValueError:
        print("Error: introduce un número válido")
        continue

    print("Resultado:", calcular(a, operador, b))

print("¡Hasta luego!")

