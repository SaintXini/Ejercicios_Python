from cliente_dao import ClienteDAO
from cliente import Cliente

print("############ Clientes de zona Fit ##############")

opc = None

while opc != 5:
    print(""" Menu:
    1. Listar clientes:
    2. Agregar clientes:
    3. Modificar clientes:
    4. Eliminar clientes:
    5. Salir
    """)

    opc = int(input("Escribe tú opcion a elegir entre (1-5): "))
    if opc == 1:
        clientes = ClienteDAO.seleccionar()
        print("\n Listado de clientes")
        for cliente in clientes:
            print(cliente)
            print("")
    elif opc == 2:
        nombre_var = input("Escribe el nombre del cliente: ")
        apellido_var = input("Escribe el apellido: ")
        membresia_var = int(input("Escribe la cantidad de la membresai: "))
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)

        cliente_agregados = ClienteDAO.insertar(cliente)
        print(f"clientes agregados: {cliente_agregados}")
    elif opc == 3:
        id_cliente_var = int(input("Escribe el valor del cliente a modificar: "))
        nombre_var = input("Escribe el nombre a modificar: ")
        apellido_var = input("Escribe el apellido a modificar: ")
        membresia_var = int(input("Escribe la cantidad a modificar: "))
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        cliente_actualizados = ClienteDAO.actualizar(cliente)
        print(f"cliente actualizado: {cliente_actualizados}")
    elif opc == 4:
        id_cliente_var = int(input("Escribe el id a eliminar: "))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f"clientes eliminados : {clientes_eliminados}")
else:
    print("Salimos de la apps")
