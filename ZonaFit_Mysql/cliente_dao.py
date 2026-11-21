from conf import Conexion
from cliente import Cliente

class ClienteDAO:
    # Variables de las constantes utilizando metodos querys
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    # Metodo seleccionar
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            # REgrese todos los registros que tenemos en la lista de clientes o las tuplas
            registros = cursor.fetchall()
            # Mapeo de la clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error de: {e}")
        finally:
            # Si el objeto no tiene el valor de none se cierra el cursos y se libera la conexion
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    # Metodo insertar
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            # accedemos a la informacións
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            # aca agregamos el query que utilizaremos para enviarlo a la BD
            cursor.execute(cls.INSERTAR, valores)
            # guardad los cambios realizados
            conexion.commit()
            # cuantos registros se insertaron
            return cursor.rowcount
        except Exception as e:
            print(f"Error de ingreso de datos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # Insertar un nuevo registro
#    cliente1 = Cliente(nombre = "Sarai", apellido ="Villatoro", membresia=153)
    # ver cuantos se han incertado
#    clientes_insertados = ClienteDAO.insertar(cliente1)
#    print(f"Clientes agregados: {clientes_insertados}")

    # Seleccionar clientes
    # Nos mostrara un listado de clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
