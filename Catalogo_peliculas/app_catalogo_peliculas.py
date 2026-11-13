from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as catalogo

print("Catalogo de peliculas")

opc = None

while opc != 4:
    try:
        print("Opciones a elegir: ")
        print("1. Agregar peliculas")
        print("2. Listar peliculas")
        print("3. Eliminar catalogo de peliculas")
        print ("4. Salir")
        opc = int(input("Escribe la opción a elegir (1-4): "))

        if opc == 1: # agregar peliculas
            nombre_pelicula = input("Dame el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opc == 2: # ver peliculas
            catalogo.listar_peliculas()
        elif opc == 3: # eliminar peliculas
            catalogo.elimnar_peliculas()            
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        opc = None

else:
    print("Salimos del programa :c.....")