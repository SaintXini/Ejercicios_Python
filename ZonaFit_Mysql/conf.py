from mysql.connector import pooling, Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = 3306
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                # se activa esto si no tiene el objeto, si en dado caso lo tiene solo lo inicializas
                # estamos crando un objeto de pool de conexiones
                # y esta va administrar todas las pool conexiones
                # es la que nos libera y nos asigna pool conexiones
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                print(f"Nombre del pool: {cls.pool.pool_name}")
                print(f"Tamño del pool: {cls.pool.pool_size}")
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al establecer un pool: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()


# esto hace que solo este archivo se ejecute, si en dado caso lo levanto desde otro este no funcionara por decirlo así, si estan conectados varios archivos
if __name__ == '__main__':
    # creación del objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    # obtener un objeto conexion
    cnx1 = Conexion.obtener_conexion