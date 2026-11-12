from claseAgre_monitor import Monitor
from clasehija_teclado import Teclado
from clasehija_raton import Raton


class Computadora:

    contador_computadoras = 0  # Atributo de clase para contar instancias

    # Constructor de la clase
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return (
            f"Computadora [ID: {self._id_computadora}, Nombre: {self._nombre}, "
            f"Monitor: {self._monitor}, Teclado: {self._teclado}, Raton: {self._raton}]"
        )

# Prueba
# El bloque if __name__ == "__main__": se utiliza para ejecutar código de prueba solo cuando el archivo se ejecuta directamente, y no cuando se importa como módulo en otro archivo.
# Esto permite que el código de prueba se ejecute solo en el contexto de prueba y no afecte a otros módulos que puedan importar la clase Raton.
# En este caso, se crean dos instancias de la clase Raton (raton1 y raton2) con diferentes marcas y tipos de entrada, y se imprime su información utilizando el método __str__ sobrescrito.
# Esto permite verificar que la clase Raton funciona correctamente y que se pueden crear múltiples ratones con diferentes atributos.
if __name__ == "__main__":
    teclado1 = Teclado("Logitech", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("Samsung", 24)
    computadora1 = Computadora("PC Gamer", monitor1, teclado1, raton1)
    print(computadora1)

