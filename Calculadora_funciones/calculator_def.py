print("Calculadora de operaciones matemáticas, con funciones definidas por el usuario")

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

def valores():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2