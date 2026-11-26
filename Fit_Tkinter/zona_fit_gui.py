import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()

    def configurar_ventana(self):
        # Tamaño y titulo
        self.geometry("900x600")
        self.title("Zona Fit APP")
        #  fijarse siempre en la escritura que ahora no me sale el autocomepletado de palabras
        self.configure(background=App.COLOR_VENTANA)

        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure(self, background = App.COLOR_VENTANA, foreground = "white")

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
       etiqueta = ttk.Label(self, text = "Zona Fit(GYM)", font=("Arial", 30), background=App.COLOR_VENTANA, foreground="white") 
       etiqueta.grid(row=0, column=0, columnspan=2, pady=30)
# para inicializar la pantalla

if __name__ == "__main__":
    app = App()
    app.mainloop()