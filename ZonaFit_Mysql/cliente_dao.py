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
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # Seleccionar clientes
    # Nos mostrara un listado de clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
