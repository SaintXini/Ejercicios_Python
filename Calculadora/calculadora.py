print("Calculadora de Operações Matemáticas")

operador1 = operador2 = 0
salir = False

while not salir:
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        resultado = operador1 + operador2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = operador1 - operador2
        print(f"El resultado de la resta es: {resultado}")