
from snack import Snack


class Snacks:

    lista_snacks = [
        Snack("Chocolatina", 1.5),
        Snack("Galletas", 2.0),
        Snack("Papas fritas", 1.0),
        Snack("Refresco", 1.5)
    ]

    def agregar_snack(self, snack):
        Snacks.lista_snacks.append(snack)

    def __str__(self):
        snacks_str = "Snacks disponibles:\n"

        # aca se mostrara el id, nombre y precio de cada snack
        for snack in self.lista_snacks:
            snacks_str += "\n" + snack.__str__()

        return f"Snacks en el inventario {snacks_str}"
    