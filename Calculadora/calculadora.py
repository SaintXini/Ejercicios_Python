print("Calculadora de Operações Matemáticas")

operador1 = operador2 = resultado = 0
salir = False

while not salir:
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion in [1, 2, 3, 4]:
        operador1 = float(input("Ingrese el primer número: "))
        operador2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado = operador1 + operador2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = operador1 - operador2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = operador1 * operador2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        if operador2 != 0:
            resultado = operador1 / operador2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == 5:
        salir = True
        print("Gracias por usar la calculadora. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
