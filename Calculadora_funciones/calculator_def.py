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

def ejecutra_operacion(opc, salir):
    pass
dsaf

# Codigo principa
# aca se definira la variable salir, que sera utilizada para salir del bucle while
salir = False

while not salir:
    opcion = mostrar_calculadora()
    salir = ejecutra_operacion(opcion, salir)

