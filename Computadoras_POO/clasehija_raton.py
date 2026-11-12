from clasePa_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    # Constructor de la clase Raton, que hereda de DispositivoEntrada
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones

        # Llamada al constructor de la clase padre (DispositivoEntrada)
        # super() se utiliza para llamar al constructor de la clase padre y pasarle los parámetros necesarios.
        # Esto permite que la clase Raton herede los atributos de la clase DispositivoEntrada (marca y tipo_entrada) y los inicialice correctamente.
        super().__init__(marca, tipo_entrada)

    # Sobrescribir el método __str__ para mostrar información del ratón
    # El método __str__ se utiliza para definir cómo se representará un objeto de la clase Raton cuando se convierta a una cadena de texto (por ejemplo, al imprimirlo).
    # En este caso, se devuelve una cadena que incluye el ID del ratón, la marca y el tipo de entrada.
    # Esto permite que al imprimir un objeto de la clase Raton, se muestre información relevante sobre el ratón en lugar de la representación predeterminada del objeto.
    def __str__(self):
        return f"Raton [ID: {self.id_raton}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}]"


# Prueba
# El bloque if __name__ == "__main__": se utiliza para ejecutar código de prueba solo cuando el archivo se ejecuta directamente, y no cuando se importa como módulo en otro archivo.
# Esto permite que el código de prueba se ejecute solo en el contexto de prueba y no afecte a otros módulos que puedan importar la clase Raton.
# En este caso, se crean dos instancias de la clase Raton (raton1 y raton2) con diferentes marcas y tipos de entrada, y se imprime su información utilizando el método __str__ sobrescrito.
# Esto permite verificar que la clase Raton funciona correctamente y que se pueden crear múltiples ratones con diferentes atributos.
if __name__ == "__main__":
    raton1 = Raton("Logitech", "USB")
    print(raton1)  # Muestra la información del ratón
    raton2 = Raton("Microsoft", "Bluetooth")
    print(raton2)  # Muestra la información del ratón