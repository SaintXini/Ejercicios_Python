class Snack:

    contador_snacks = 0

    # Constructor
    def __init__(self, nombre, precio):
        Snack.contador_snacks += 1
        self.id_snack = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Snack [ID: {self.id_snack}, Nombre: {self.nombre}, Precio: ${self.precio}]"
    