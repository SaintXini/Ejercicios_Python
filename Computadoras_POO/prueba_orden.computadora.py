from clasehija_teclado import Teclado
from clasehija_raton import Raton
from claseAgre_monitor import Monitor
from clasePrin_computadora import Computadora
from orden import Orden


teclado1 = Teclado("Logitech", "USB")
raton1 = Raton("HP", "USB")
monitor1 = Monitor("Samsung", 24)
computadora1 = Computadora("PC Gamer", monitor1, teclado1, raton1)

computadora1 = [computadora1]
orden1 = Orden(computadora1)

print(orden1)
