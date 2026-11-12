print("Calculadora de operaciones matemáticas, con funciones definidas por el usuario")

# aca se definira la funcion de mostrar calculadora, que mostrara las opciones disponibles para el usuario
def mostrar_calculadora():

    print("Operaciones que puedes realizar:")
    print("#########")
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opc = int(input("Ingrese el número de la opción deseada: "))
    return opc

# aca se definira la funcion de valores, que pedira al usuario que ingrese dos numeros y los retornara
def valores():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2

# aca se definira la funcion de ejecutar operacion, que recibira la opcion del usuario y la variable salir, y ejecutara la operacion correspondiente
def ejecutar_operacion(opc, salir):

    if 1 <= opc <= 4:
        # aca se llamara a la funcion de valores, que pedira al usuario que ingrese dos numeros y los retornara
        num1, num2 = valores()

    # aca se definira la variable resultado, que sera utilizada para almacenar el resultado de la operacion
    resultado = 0

    if opc == 1: # Suma
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opc == 2: # Resta
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif opc == 3: # Multiplicación
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opc == 4: # División
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif opc == 5: # Salir
        salir = True
        print("Gracias por usar la calculadora. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    return salir


salir = False
while not salir:
    opcion = mostrar_calculadora()
    salir = ejecutar_operacion(opcion, salir)

