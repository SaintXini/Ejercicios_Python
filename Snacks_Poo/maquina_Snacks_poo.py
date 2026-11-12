from snacks import Snacks
from snack import Snack

# Lista de productos, utilizando una lista vacia
productos = []

print("Bienvenido a la máquina de snacks")
print("Estos son los snacks disponibles:")

snacks = Snacks()
print(snacks)

## def son utilizadas para definir funciones, en este caso se definira la funcion de la maquina de productos, que recibira como parametros la lista de snacks y la lista de productos
def maquina_productos(snacks, productos):

    salir = False

    while not salir:
        print("\nSeleccione una opción:")
        print("1. Comprar snack")
        print("2. Ver productos comprados")
        print("3. Agregar nuevo producto")
        print("4. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            ver_productos(productos)
        elif opcion == 3:
            agregar_snack(snacks)
        elif opcion == 4:
            salir = True
            print("Gracias por usar la máquina de snacks. ¡Hasta luego!")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def comprar_producto(snacks, productos):
    id_snack = int(input("Ingrese el ID del snack que desea comprar: "))
    # REcorremos la lista de snacks
    snack_encontrado = None

    # Para encontrar el id que el usuario a proporcionado
    for snack in snacks.lista_snacks:
        if id_snack == snack.id_snack:
            # Si existe se le asigna a la variable "snack_encontrado"
            snack_encontrado = snack
            break

        # Se vuelve a revisar si el valor no tinene "None"
        if snack_encontrado is not None:
            # Se agrega a la lista de productos
            productos.append(snack_encontrado)
            print(f"Ok, snack agregado: {snack_encontrado}")
        else:
            print(f"El id del snack es incorrecto: {id_snack}")


# aca se definira la funcion de ver productos, que recibira como parametro la lista de productos
def ver_productos(productos):
    ticket = "\nTicket de compra:\n"
    total = 0

    for producto in productos:
        ticket += f"- {producto.nombre}: Q  {producto.precio:.2f}\n"
        total += producto.precio
    ticket += f"Total: Q {total:.2f}"
    print(ticket)

# funcion agregar snack
def agregar_snack(snacks):
    nombre = input("Dame el nombre del snack: ")
    precio = int(input("dame el precio del snack: "))
    nuevo_snack = Snack(nombre, precio)
    snacks.agregar_snack(nuevo_snack)
    print(f"Tu snack {nuevo_snack} se ha agregado correctamente")
    print(snacks)

# LLamamos la funcion de la maquina de productos, pasandole como parametros la lista de snacks y la lista de productos
maquina_productos(snacks, productos)
