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
teclado1 = Teclado("Logitech", "USB")
raton1 = Raton("Logitech", "USB")
monitor1 = Monitor("Samsung", 24)
computadora1 = Computadora("PC Gamer", monitor1, teclado1, raton1)
print(computadora1)

