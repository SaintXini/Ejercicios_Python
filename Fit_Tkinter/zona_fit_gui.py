import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

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

    def mostrar_formulario(self):
        pass

    def mostrar_tabla(self):
        # creamos un frame para poder mostrar la tabla que ira del lado izq
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure("Treeview", background="gray", foreground="black", fieldbackground="gray", rowheight=30)
        columnas = ("ID", "NOMBRE", "APELLIDO", "MEMBRESIA")
        # esto hace que los cambios que se realizen solo afecte a la tabla y no a todo lo demas que se encuentra en dicha area
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")

        # mostrar la tabla
        self.tabla.grid(row=0, column=0)
        # mostramos el frame
        self.frame_tabla.grid(row=1, column=1, padx=30)


# para inicializar la pantalla

if __name__ == "__main__":
    app = App()
    app.mainloop()