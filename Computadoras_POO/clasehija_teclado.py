from clasePa_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    # Constructor de la clase Teclado, que hereda de DispositivoEntrada
    def __init__(self, marca, tipo_entrada):
        # Incrementar el contador de teclados y asignar un ID único a cada instancia
        Teclado.contador_teclados += 1
        # Asignar un ID único a cada instancia de Teclado
        self.id_teclado = Teclado.contador_teclados

        # Llamada al constructor de la clase padre (DispositivoEntrada)
        super().__init__(marca, tipo_entrada)

    # Sobrescribir el método __str__ para mostrar información del teclado
    def __str__(self):
        return f"Teclado [ID: {self.id_teclado}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}]"

# Prueba
# El bloque if __name__ == "__main__": se utiliza para ejecutar código de prueba solo cuando el archivo se ejecuta directamente, y no cuando se importa como módulo en otro archivo.
# Esto permite que el código de prueba se ejecute solo en el contexto de prueba y no afecte a otros módulos que puedan importar la clase Raton.
# En este caso, se crean dos instancias de la clase Raton (raton1 y raton2) con diferentes marcas y tipos de entrada, y se imprime su información utilizando el método __str__ sobrescrito.
# Esto permite verificar que la clase Raton funciona correctamente y que se pueden crear múltiples ratones con diferentes atributos.
if __name__ == "__main__":
    teclado1 = Teclado("Logitech", "USB")
    teclado2 = Teclado("Microsoft", "Bluetooth")
    print(teclado1)  # Muestra la información del teclado 1
    print(teclado2)  # Muestra la información del teclado 2