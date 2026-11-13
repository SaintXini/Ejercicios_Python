import os
class CatalogoPeliculas:
    nombre_archivo = "peliculas.txt"

    # Este metodo se asocia con la clase misma y no con objetos
    @classmethod
    # cls se agrega debido al funcionamiento de este mismo
    def agregar_pelicula(cls, pelicula):
        # se agrega las instancias que se utilizanran en el archivo y se utiliza utf8 para que pueda aceptar cualquier parametro
        with open(cls.nombre_archivo, 'a', encoding='utf8') as archivo:
            # Acá se agregarian los atributos que tendría la clase, pero en esta caso solo agregue el nombre solo nombre utilizara
            archivo.write(f"{pelicula.nombre}\n")

    # Otro metodo de clase
    @classmethod
    def listar_peliculas(cls):
        # se abre el archivo y se especifica el tipo de lineamientos que utiliza para leer
        with open(cls.nombre_archivo, 'r', encoding='utf8') as archivo:
            print("Listado de las peliculas")
            print(archivo)

    @classmethod
    def elimnar_peliculas(cls):
        # importamos el metodo operatin system
        os.remove(cls.nombre_archivo)
        print(f"Archvio eliminado: {cls.nombre_archivo}")