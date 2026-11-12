
class Monitor():

    contador_monitores = 0

    # Constructor de la clase
    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"Monitor [ID: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamano}]"

    # Prueba
if __name__ == "__main__":

    monitor1 = Monitor("Samsung", 24)
    monitor2 = Monitor("LG", 27)
    print(monitor1)  # Muestra la información del monitor 1
    print(monitor2)  # Muestra la información del monitor 2