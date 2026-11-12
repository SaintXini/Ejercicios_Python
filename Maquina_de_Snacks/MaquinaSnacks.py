# aca utilizare una lista para almacenar los snacks disponibles en la maquina,en un diccionario se almacenara el nombre del snack y su precio, y en la lista se almacenara el diccionario de cada snack
snacks = [{"id": 1, "nombre": "Chocolatina", "precio": 1.5}, 
          {"id": 2, "nombre": "Galletas", "precio": 2.0}, 
          {"id": 3, "nombre": "Papas fritas", "precio": 1.0}, 
          {"id": 4, "nombre": "Refresco", "precio": 1.5}]

# Lista de productos, utilizando una lista vacia
productos = []

print("Bienvenido a la máquina de snacks")
print("Estos son los snacks disponibles:")
for snack in snacks:
    # aca se mostrara el id, nombre y precio de cada snack
    print(f"- {snack['id']}: {snack['nombre']}: Q {snack['precio']:.2f}")

## def son utilizadas para definir funciones, en este caso se definira la funcion de la maquina de productos, que recibira como parametros la lista de snacks y la lista de productos
def maquina_productos(snacks, productos):

    salir = False

    while not salir:
        print("\nSeleccione una opción:")
        print("1. Comprar snack")
        print("2. Ver productos comprados")
        print("3. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            ver_productos(productos)
        elif opcion == 3:
            salir = True
            print("Gracias por usar la máquina de snacks. ¡Hasta luego!")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# aca se definira la funcion de comprar producto, que recibira como parametros la lista de snacks y la lista de productos
def comprar_producto(snacks, productos):
    pass

# aca se definira la funcion de ver productos, que recibira como parametro la lista de productos
def ver_productos(productos):
    pass


# LLamamos la funcion de la maquina de productos, pasandole como parametros la lista de snacks y la lista de productos
maquina_productos(snacks, productos)
