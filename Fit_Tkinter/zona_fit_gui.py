import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.configurar_ventana()

    def configurar_ventana(self):
        # Tamaño y titulo
        self.geometry("900x600")
        self.title("Zona Fit APP")
        self.configure(background=App.COLOR_VENTANA)

        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure(self, background = App.COLOR_VENTANA, foreground = "white")


# para inicializar la pantalla

if __name__ == "__main__":
    app = App()
    app.mainloop()