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
teclado1 = Teclado("Logitech", "USB")
teclado2 = Teclado("Microsoft", "Bluetooth")
print(teclado1)  # Muestra la información del teclado 1
print(teclado2)  # Muestra la información del teclado 2