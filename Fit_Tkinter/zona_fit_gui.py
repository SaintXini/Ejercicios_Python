import tkinter as tk
from tkinter import ttk

from cliente_dao import ClienteDAO

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botons()

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
        self.frame_f = ttk.Frame()
        # NOmbre
        nombre_label = ttk.Label(self.frame_f, text="Nombre: ")
        nombre_label.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_f)
        self.nombre_t.grid(row=0, column=1)

        # Apellido
        apellido_label = ttk.Label(self.frame_f, text="Apellido: ")
        apellido_label.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_f)
        self.apellido_t.grid(row=1, column=1)

        # Membresia
        membresia_label = ttk.Label(self.frame_f, text="Membresia: ")
        membresia_label.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_f)
        self.membresia_t.grid(row=2, column=1)     

        # Publicamos el frame
        self.frame_f.grid(row=1, column=0)

    def mostrar_tabla(self):
        # creamos un frame para poder mostrar la tabla que ira del lado izq
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure("Treeview", background="gray", foreground="black", fieldbackground="gray", rowheight=30)
        columnas = ("Id", "Nombre", "Apellido", "Membresia")
        # esto hace que los cambios que se realizen solo afecte a la tabla y no a todo lo demas que se encuentra en dicha area
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")

        # agregamos los acabeceros ot itulos
        # y aca definimos donde se mostrara y en que posición se encontrara de la columna
        self.tabla.heading("Id", text="ID", anchor=tk.CENTER)
        self.tabla.heading("Nombre", text="NOMBRE", anchor=tk.W)
        self.tabla.heading("Apellido", text="APELLIDO", anchor=tk.W)
        self.tabla.heading("Membresia", text="MEMBRESIA", anchor=tk.W)

        # definimos las columnas
        self.tabla.column("Id", anchor=tk.CENTER, width=80)
        self.tabla.column("Nombre", anchor=tk.W, width=120)
        self.tabla.column("Apellido", anchor=tk.W, width=120)
        self.tabla.column("Membresia", anchor=tk.W, width=120)

        # Cargar los datos de los clientes de la BD
        clientes = ClienteDAO.seleccionar()
        # en la variable c tenemos el objeto cliente que esta recorriendo, pór cada uno de los datos que tenemos
        for c in clientes:
            self.tabla.insert(parent="",
                              index=tk.END,
                              values=(c.id, c.nombre, c.apellido, c.membresia))


        # agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # mostrar la tabla
        self.tabla.grid(row=0, column=0)
        # mostramos el frame
        self.frame_tabla.grid(row=1, column=1, padx=30)

    def mostrar_botons(self):
        self.frame_b = ttk.Frame()
        # Creamos los botonoes
        # Agregar
        agregar_b = ttk.Button(self.frame_b, text="Guardar", command=self.validar_cliente)
        agregar_b.grid(row=0, column=0, padx=30)
        
        # Eliminar
        eliminar_b = ttk.Button(self.frame_b, text="Eliminar", command=self.eliminar_cliente)
        eliminar_b.grid(row=0, column=1, padx=30)
        
        # limpiar la información
        limpiar_b = ttk.Button(self.frame_b, text="Limpiar", command=self.limpiar_datos)
        limpiar_b.grid(row=0, column=2, padx=30)
        
        # aplicamos un estilo al estar pocisionados sobre el boton
        # ojo tengo que utilizar comilla simple áca, debido a que no se si ingrese mal algo o es por las comillas, pero no me aparecía hasta que cambie
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # que se pueda ver
        self.frame_b.grid(row=2, column=0, columnspan=2, pady=40)

    def validar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        pass

# para inicializar la pantalla

if __name__ == "__main__":
    app = App()
    app.mainloop()