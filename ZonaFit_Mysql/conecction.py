from mysql.connector import pooling, Error

class Conexion:

    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 2
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea un nuevo objeto pooll
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
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al establecer un pool: {e}")
        else:
            return cls.pool

