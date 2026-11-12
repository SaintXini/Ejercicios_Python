class DispositivoEntrada:
    def __init__(self, tipo):
        self.tipo = tipo

    def leer_entrada(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")